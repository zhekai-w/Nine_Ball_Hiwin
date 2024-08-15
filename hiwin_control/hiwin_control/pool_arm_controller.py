#!/usr/bin/env python3
import time
import yaml
import configparser

import rclpy
from enum import Enum
from threading import Thread
from rclpy.node import Node
from rclpy.task import Future
from typing import NamedTuple
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64MultiArray, String
from hiwin_interfaces.srv import RobotCommand

import numpy as np
import math
import quaternion as qtn
import hiwin_control.transformations as transformations
import hiwin_control.nine_ball_strat as table2
import hiwin_control.pool_strat_v2 as pool
import matplotlib.pyplot as plt

CUE_TOOL = 12

DEFAULT_VELOCITY = 100
DEFAULT_ACCELERATION = 100

LIGHT_PIN = 6
HITSOFT_PIN = 4
HITMID_PIN = 5
HITHEAVY_PIN = 1
HEAVY_PIN = 2

# FIX_ABS_CAM = [36.326, 376.998, 411.897, 180.0, 0.0, 90.0]
# FIX_ABS_RIGHT_CAM = [186.326, 376.998, 411.897, 180.0, 0.0, 90.0]
# FIX_ABS_LEFT_CAM = [-114.326, 376.998, 411.897, 180.0, 0.0, 90.0]
END_TURN_RIGHT = [90.00, 0.00, 0.00, 0.00, -90.00, 0.00] #手臂TURN右
END_TURN_HALL=[0.00, 44.832, 408.491, -179.999, -30.972, 89.998]
TOOL_TO_CAM = [-36.715, 77.5046, -68.49]

# CAM_TO_TABLE = 480
CALI_HIGHT = 80.0

# Read tool to camera vector
config = configparser.ConfigParser()
config.read('eye_in_hand_calibration.ini')
tm = config['hand_eye_calibration']
TOOL_TO_CAM[0] = float(tm['y'])*1000
TOOL_TO_CAM[1] = float(tm['x'])*1000
TOOL_TO_CAM[2] = -float(tm['z'])*1000

# Read table pot hole position and camera to table height
with open('arm.yaml', 'r') as file:
    data = yaml.safe_load(file)

FIX_ABS_CAM = data['armpos']
FIX_ABS_RIGHT_CAM = [FIX_ABS_CAM[0]+150, 376.998, 411.897, 180.0, 0.0, 90.0]
FIX_ABS_LEFT_CAM = [FIX_ABS_CAM[0]-150, 376.998, 411.897, 180.0, 0.0, 90.0]
CAM_TO_TABLE = data['zoff']

class States(Enum):
    INIT = 0
    FINISH = 1
    MOVE_TO_PHOTO_POSE = 2
    STEP_CALI = 3
    STRATEGY = 4
    HITPOINT_TOP = 5
    HITPOINT_ANGLE = 6
    HITBALL_POSE = 7
    HITBALL = 8
    AF_HITPOINT_ANGLE = 9
    AF_HITPOINT_TOP = 10
    CHECK_POSE = 11
    CLOSE_ROBOT = 12
    OPEN_SEC_IO = 13
    LOCK_INFO = 14
    MOVE_TO_LOWER = 15
    FIX_LEFT_PHOTO_POSE = 16
    FIX_RIGHT_PHOTO_POSE = 17
    LOCK_CUE = 18

def check_mid_pose(all_ball_pose):
    mid_error = []
    for i in range(0,len(all_ball_pose),2):
        dev_x = all_ball_pose[i] - 1920/2
        dev_y = all_ball_pose[i+1] - 1080/2
        temp_error = math.sqrt((dev_x)**2+(dev_y)**2)
        mid_error.append(temp_error)
    # print("mid error:", mid_error)
    min_error_index = mid_error.index(min(mid_error))
    # print("min index:", min_error_index)
    mid_x = all_ball_pose[2*min_error_index]
    mid_y = all_ball_pose[2*min_error_index+1]

    return mid_x, mid_y

def mid_point_error(mid_ball: list) -> float:
    dev_x = mid_ball[0] - 1920/2
    dev_y = mid_ball[1] - 1080/2
    mid_error = math.sqrt((dev_x)**2+(dev_y)**2)

    return mid_error

def pixel_mm_convert(cam_to_table_h, pixels):
    fov_x = 69/2
    fov_y = 42/2
    p_x = 1920/2
    p_y = 1080/2

    cam_to_table_x = cam_to_table_h/math.tan(math.radians(90-fov_x))
    cam_to_table_y = cam_to_table_h/math.tan(math.radians(90-fov_y))

    dev_x = cam_to_table_x/p_x*(pixels[0]-p_x)
    dev_y = cam_to_table_y/p_y*(pixels[1]-p_y)
    cam_to_ball_pose = [dev_x, dev_y, 1.0]

    return cam_to_ball_pose

def yaw_angle(vectorx, vectory):
    vectorlength = math.sqrt((vectorx**2)+(vectory**2))
    rad = math.acos((-1*vectory)/(vectorlength*1))
    theta = rad*180/math.pi
    if vectorx >= 0:
        return theta, rad
    elif vectorx < 0:
        return -theta, -rad

def convert_arm_pose(ball_pose, arm_pose):
    base2tool = np.array(arm_pose)
    base2tool[:3] /= 1000

    # tool to camera quaternion
    tool2cam_quaternion = [0.007269923959234842, -0.0032559856852129544, 0.7024893071973962, 0.7116497172318463]
    tool2cam_trans = [0.07750464277165502, -0.03671563427202898, 0.06849008934693676]

    tool2cam_rot = qtn.as_rotation_matrix(np.quaternion(tool2cam_quaternion[3],
                                                        tool2cam_quaternion[0],
                                                        tool2cam_quaternion[1],
                                                        tool2cam_quaternion[2]))
    tool2cam_trans = np.array([tool2cam_trans])

    # print("tool2cam_trans = {}".format(tool2cam_trans))

    tool2cam_mat = np.append(tool2cam_rot, tool2cam_trans.T, axis=1)
    tool2cam_mat = np.append(tool2cam_mat, np.array([[0., 0., 0., 1.]]), axis=0)

    quat = transformations.quaternion_from_euler(base2tool[3]*3.14/180,
                                                 base2tool[4]*3.14/180,
                                                 base2tool[5]*3.14/180,axes= "sxyz")

    base2tool_rot = qtn.as_rotation_matrix(np.quaternion(quat[3],
                                                         quat[0],
                                                         quat[1],
                                                         quat[2]))

    base2tool_trans = np.array([base2tool[:3]])

    base2tool_mat = np.append(base2tool_rot, base2tool_trans.T, axis=1)
    base2tool_mat = np.append(base2tool_mat, np.array([[0., 0., 0., 1.]]), axis=0)


    cam2ball_trans = np.array([[ball_pose[0]/1000,
                                ball_pose[1]/1000,
                                ball_pose[2]]])
    unit_matrix = np.identity(3)
    cam2ball_mat = np.append(unit_matrix, cam2ball_trans.T, axis=1)
    cam2ball_mat = np.append(cam2ball_mat, np.array([[0., 0., 0., 1.]]), axis=0)

    base2cam_mat = np.matmul(base2tool_mat, tool2cam_mat)
    base2ball_mat = np.matmul(base2cam_mat, cam2ball_mat)

    ax, ay, az = transformations.euler_from_matrix(base2ball_mat)
    base2ball_translation = transformations.translation_from_matrix(base2ball_mat)*1000.0

    calibrated_ball_pose = [base2ball_translation[0],
                            base2ball_translation[1],
                            base2ball_translation[2],
                            ax*180/3.14,
                            ay*180/3.14,
                            az*180/3.14]

    return calibrated_ball_pose

class Hiwin_Controller(Node):
    def __init__(self):
        super().__init__('hiwin_controller')
        self.hiwin_client = self.create_client(RobotCommand, 'hiwinmodbus_service')
        self.yolo_subscriber = self.create_subscription(Float64MultiArray, 'center_data_coords', self.yolo_callback, 10)
        self.yolo_label_subscriber = self.create_subscription(String, 'center_data_labels', self.label_callback, 10)
        # self.stategy_subscriber = self.create_subscription(Float64MultiArray, 'strategy_hitpoint',self.strategy_callback, 10)
        self.object_pose = None
        self.object_cnt = 0
        self.all_ball_pose = []
        self.strategy_info = []
        self.ball_pose_buffer = []
        self.target_cue = []
        self.all_label = []
        self.label_buffer = []
        self.fix_z = 90.
        self.table_z = FIX_ABS_CAM[2] + TOOL_TO_CAM[2] - CAM_TO_TABLE

    # def strategy_callback(self, msg):
    #     _ = msg.data

    def label_callback(self, msg):
        self.all_label = eval(msg.data)

    def yolo_callback(self, msg):
        if not msg.data:
            rclpy.logwarn("Received empty data in yolo_callback")
        else:
            self.all_ball_pose = msg.data
            self.target_cue = [self.all_ball_pose[:2], self.all_ball_pose[-2:]]
            self.data_received.set()


    def _state_machine(self, state: States) -> States:
        if state == States.INIT:
            self.get_logger().info('MOVING TO PREPARE POSE...')
            # joints=[float('inf')]*6,
            print("fix cam joint", END_TURN_RIGHT)
            # req = self.generate_robot_request(
            #     cmd_type=RobotCommand.Request.JOINTS_CMD,
            #     joints = END_TURN_RIGHT,
            #     #不想讓手臂停止才做事(下面if/else不用，直接給下一步的狀態就好)
            #     #hold=Flase
            #     )
            # res = self.call_hiwin(req)
            pose = Twist()
            [pose.linear.x, pose.linear.y, pose.linear.z] = END_TURN_HALL[0:3]
            [pose.angular.x, pose.angular.y, pose.angular.z] = END_TURN_HALL[3:6]
            print("fix cam pose", END_TURN_HALL)
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.PTP,
                pose = pose
                )
            res = self.call_hiwin(req)
            """
            need to place arm in initial position.
            1) first joint 90 degrees to the left or right
            2) fifth joint is on top of first joint
            """
            self.get_logger().info('INIT/WAIT FOR BUTTON')
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.READ_DI,
                digital_input_pin = 1,
                holding=True,
            )
            res = self.call_hiwin(req)
            last_state = res.digital_state

            while True:
                res = self.call_hiwin(req)
                current_state = res.digital_state
                self.get_logger().info('CURRENT STATE:%d'%current_state)
                self.get_logger().info('LAST STATE:%d'%last_state)
                if current_state != last_state:
                    break
                else:
                    continue
            nest_state = States.MOVE_TO_PHOTO_POSE

        elif state == States.MOVE_TO_PHOTO_POSE:
            # value need to be reset every time
            self.updated_target_cue = []
            self.updated_balls_x = []
            self.updated_balls_y = []
            self.index = 0

            self.get_logger().info('TUNING LIGHTS ON/MOVING TO CAMERA POSE...')
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.DIGITAL_OUTPUT,
                digital_output_cmd = RobotCommand.Request.DIGITAL_ON,
                digital_output_pin = LIGHT_PIN
            )
            self.call_hiwin(req)
            pose = Twist()
            [pose.linear.x, pose.linear.y, pose.linear.z] = FIX_ABS_CAM[0:3]
            [pose.angular.x, pose.angular.y, pose.angular.z] = FIX_ABS_CAM[3:6]
            print("fix cam pose", FIX_ABS_CAM)
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.PTP,
                pose = pose
                )
            res = self.call_hiwin(req)
            if res.arm_state == RobotCommand.Response.IDLE:
                nest_state = States.LOCK_INFO
            else:
                nest_state = None

        elif state == States.FIX_RIGHT_PHOTO_POSE:
            self.fix_check_point = []
            self.get_logger().info('MOVING TO RIGHT PHOTO POSE...')
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.DIGITAL_OUTPUT,
                digital_output_cmd = RobotCommand.Request.DIGITAL_ON,
                digital_output_pin = LIGHT_PIN
            )
            self.call_hiwin(req)
            self.fix_check_point = FIX_ABS_RIGHT_CAM
            pose = Twist()
            [pose.linear.x, pose.linear.y, pose.linear.z] = self.fix_check_point[0:3]
            [pose.angular.x, pose.angular.y, pose.angular.z] = self.fix_check_point[3:6]
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.PTP,
                pose = pose
                )
            res = self.call_hiwin(req)
            if res.arm_state == RobotCommand.Response.IDLE:
                nest_state = States.LOCK_CUE
            else:
                nest_state = None

        elif state == States.FIX_LEFT_PHOTO_POSE:
            self.fix_check_point = []
            self.get_logger().info('MOVING TO RIGHT PHOTO POSE...')
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.DIGITAL_OUTPUT,
                digital_output_cmd = RobotCommand.Request.DIGITAL_ON,
                digital_output_pin = LIGHT_PIN
            )
            self.call_hiwin(req)
            self.fix_check_point = FIX_ABS_LEFT_CAM
            pose = Twist()
            [pose.linear.x, pose.linear.y, pose.linear.z] = self.fix_check_point[0:3]
            [pose.angular.x, pose.angular.y, pose.angular.z] = self.fix_check_point[3:6]
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.PTP,
                pose = pose
                )
            res = self.call_hiwin(req)
            if res.arm_state == RobotCommand.Response.IDLE:
                nest_state = States.LOCK_CUE
            else:
                nest_state = None

        elif state == States.LOCK_CUE:
            time.sleep(0.3)
            self.get_logger().info('LOCKING CUE BALL INFO...')

            self.ball_pose_buffer = self.all_ball_pose
            self.label_buffer = self.all_label
            if 'white' in self.label_buffer:
                print("white ball seen")
                temp_ball_pose_mm = pixel_mm_convert(CAM_TO_TABLE, self.ball_pose_buffer[-2:])
                temp_actual_pose = convert_arm_pose(temp_ball_pose_mm, self.fix_check_point)
                self.ball_pose.append(temp_actual_pose)
                self.fix_check_point = FIX_ABS_CAM
                nest_state = States.STEP_CALI

            else:
                print("MOVING TO FIX LEFT POSE...")
                nest_state = States.FIX_LEFT_PHOTO_POSE

        elif state == States.LOCK_INFO:
            time.sleep(1)
            self.ball_pose = []
            self.get_logger().info('LOCKING INFO FOR STRATEGY AND CALIBRATION...')
            # input("Enter to continue...")
            self.ball_pose_buffer_1d = np.array(self.all_ball_pose)
            n = int(len(self.ball_pose_buffer_1d)/2)
            self.ball_pose_buffer = self.ball_pose_buffer_1d.reshape(n,2)
            print("All array ball:", self.ball_pose_buffer)
            self.label_buffer = self.all_label
            if 'white' in self.label_buffer:
                for ball in self.ball_pose_buffer:
                    temp_ball_pose_mm = pixel_mm_convert(CAM_TO_TABLE, ball)
                    temp_actual_pose = convert_arm_pose(temp_ball_pose_mm, FIX_ABS_CAM)
                    self.ball_pose.append(temp_actual_pose[0:2])

                nest_state = States.STEP_CALI

            else:
                print("Fuck Cue ball")
                for ball in self.ball_pose_buffer:
                    print("target:", ball)
                    temp_ball_pose_mm = pixel_mm_convert(CAM_TO_TABLE, ball)
                    temp_actual_pose = convert_arm_pose(temp_ball_pose_mm, FIX_ABS_CAM)
                    self.ball_pose.append(temp_actual_pose[0:2])
                nest_state = States.FIX_RIGHT_PHOTO_POSE

        elif state == States.STEP_CALI:
            print("Actual ball pose:", self.ball_pose)
            self.get_logger().info('STEP CALI FOR TEST STRATEGY...')
            self.obj_ballx = []
            self.obj_bally = []
            cuex = None
            cuey = None
            ball_to_cali = []
            for ball in self.ball_pose:
                self.obj_ballx.append(ball[0])
                self.obj_bally.append(ball[1])
            cuex = self.obj_ballx[-1]
            cuey = self.obj_bally[-1]

            # Route returns
            # score,cuefinalvector,cue,cuetoivector, objectballi, itok2vector, objectballk2 ,k2tok1vector, objectballk1, toholevector,n
            valid_route, bestrouteindex, obstacle_flag = pool.main(self.obj_ballx[:-1], self.obj_bally[:-1], cuex, cuey)
            self.strategy_info = pool.route_process(valid_route, bestrouteindex, obstacle_flag)

            print("OBJ ballx:", self.obj_ballx)
            print("OBJ bally:", self.obj_bally)
            best_route = valid_route[bestrouteindex]
            self.interrupt_ball_n = best_route[-1]
            # print(self.interrupt_ball_n)
            # if self.interrupt_ball_n == 0:
            #     ball_to_cali.append(best_route[4])
            #     ball_to_cali.append([cuex, cuey])
            # elif self.interrupt_ball_n == 1:
            #     ball_to_cali.append(best_route[4])
            #     ball_to_cali.append(best_route[6])
            #     ball_to_cali.append([cuex, cuey])
            # elif self.interrupt_ball_n == 2:
            #     ball_to_cali.append(best_route[4])
            #     ball_to_cali.append(best_route[6])
            #     ball_to_cali.append(best_route[8])
            #     ball_to_cali.append([cuex, cuey])
            # else:
            #     ball_to_cali.append([cuex, cuey])

            '''
            Only calibrate cueball
            '''
            ball_to_cali = [cuex, cuey]

            # Turn off light
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.DIGITAL_OUTPUT,
                digital_output_cmd = RobotCommand.Request.DIGITAL_OFF,
                digital_output_pin = LIGHT_PIN
            )
            self.call_hiwin(req)
            print(ball_to_cali)
            if self.index < len(ball_to_cali):
                self.get_logger().info('MOVING TO CALIBRATION POSE...')
                self.get_logger().info('Camera moving to index_{} ball'.format(self.index))
                pose = Twist()
                [pose.linear.x, pose.linear.y, pose.linear.z] = [ball_to_cali[self.index][0] - TOOL_TO_CAM[0],
                                                                 ball_to_cali[self.index][1] - TOOL_TO_CAM[1],
                                                                 self.fix_z]
                # change
                [pose.angular.x, pose.angular.y, pose.angular.z] = FIX_ABS_CAM[3:6]

                req = self.generate_robot_request(
                cmd_mode=RobotCommand.Request.PTP,
                pose = pose,
                )
                res = self.call_hiwin(req)
                if res.arm_state == RobotCommand.Response.IDLE:
                    time.sleep(0.3)
                    print('STEP CALIBRATION...')

                req = self.generate_robot_request(cmd_mode=RobotCommand.Request.CHECK_POSE)
                res = self.call_hiwin(req)
                cali_point = res.current_position

                self.data_recieved.wait()
                mid_x, mid_y = check_mid_pose(self.all_ball_pose)
                self.mid_mm = pixel_mm_convert(self.fix_z - abs(TOOL_TO_CAM[2]) + abs(self.table_z), [mid_x, mid_y])

                self.updated_balls_x.append(cali_point[0] + TOOL_TO_CAM[0] + self.mid_mm[0])
                self.updated_balls_y.append(cali_point[1] + TOOL_TO_CAM[1] - self.mid_mm[1])
                self.index += 1

                if res.arm_state == RobotCommand.Response.IDLE and self.index < len(ball_to_cali):
                    nest_state = States.STEP_CALI
                else:
                    nest_state = States.OPEN_SEC_IO

        elif state == States.OPEN_SEC_IO:
            self.get_logger().info('Opening second IO\n')
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.DIGITAL_OUTPUT,
                digital_output_cmd = RobotCommand.Request.DIGITAL_ON,
                digital_output_pin = HEAVY_PIN
            )
            res = self.call_hiwin(req)
            # time.sleep(0.5)
            if res.arm_state == RobotCommand.Response.IDLE:
                nest_state = States.STRATEGY
            else:
                nest_state = None

        elif state == States.STRATEGY:
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.DIGITAL_OUTPUT,
                digital_output_cmd = RobotCommand.Request.DIGITAL_OFF,
                digital_output_pin = LIGHT_PIN
            )
            self.call_hiwin(req)

            self.get_logger().info('CALCULATE PATH')
            # pool.main returns -> [bestscore, bestvx, bestvy, countobs, final_self.hitpointx, final_self.hitpointy]
            print(self.updated_balls_x)
            print(self.updated_balls_y)
            # if self.interrupt_ball_n == -1:
            #     for i in range(len(self.obj_ballx[:-1])):
            #         self.obj_ballx[i] += self.mid_mm[0]
            #         self.obj_bally[i] -= self.mid_mm[1]
            #     valid_route, bestrouteindex, obstacle_flag = pool.main(self.obj_ballx[:-1], self.obj_bally[:-1],
            #                                 self.updated_balls_x[0], self.updated_balls_y[0])
            #     updated_strategy_info = pool.route_process(valid_route, bestrouteindex, obstacle_flag)
            #     self.updated_hitpointx = updated_strategy_info[4]
            #     self.updated_hitpointy = updated_strategy_info[5]
            #     self.updated_vx = updated_strategy_info[1]
            #     self.updated_vy = updated_strategy_info[2]

            # else:
            #     valid_route, bestrouteindex, obstacle_flag = pool.main(self.updated_balls_x[:-1], self.updated_balls_y[:-1],
            #                                 self.updated_balls_x[-1], self.updated_balls_y[-1])
            #     updated_strategy_info = pool.route_process(valid_route, bestrouteindex, obstacle_flag)
            #     self.updated_hitpointx = updated_strategy_info[4]
            #     self.updated_hitpointy = updated_strategy_info[5]
            #     self.updated_vx = updated_strategy_info[1]
            #     self.updated_vy = updated_strategy_info[2]

            '''
            Only calibrate cueball
            '''
            for i in range(len(self.obj_ballx[:-1])):
                self.obj_ballx[i] += self.mid_mm[0]
                self.obj_bally[i] -= self.mid_mm[1]
            valid_route, bestrouteindex, obstacle_flag = pool.main(self.obj_ballx[:-1], self.obj_bally[:-1],
                                        self.updated_balls_x[0], self.updated_balls_y[0])
            updated_strategy_info = pool.route_process(valid_route, bestrouteindex, obstacle_flag)
            self.updated_hitpointx = updated_strategy_info[4]
            self.updated_hitpointy = updated_strategy_info[5]
            self.updated_vx = updated_strategy_info[1]
            self.updated_vy = updated_strategy_info[2]

            nest_state = States.HITPOINT_TOP

        elif state == States.HITPOINT_TOP:
            self.score = self.strategy_info[0]
            self.obstacle = self.strategy_info[3]
            self.get_logger().info('MOVING TO HITPOINT TOP...')
            self.hitpointx = self.updated_hitpointx
            self.hitpointy = self.updated_hitpointy
            vx = self.updated_vx
            vy = self.updated_vy

            # yaw, _ = yaw_angle(vx, vy)
            pose = Twist()
            [pose.linear.x, pose.linear.y, pose.linear.z] = [self.hitpointx, self.hitpointy, -70.0]
            if self.obstacle == 0:
                [pose.angular.x, pose.angular.y, pose.angular.z] = [-180., 10., 90.]
            else:
                [pose.angular.x, pose.angular.y, pose.angular.z] = [-180., 20., 90.]
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.PTP,
                holding=False,
                tool = CUE_TOOL,
                pose = pose
            )
            res = self.call_hiwin(req)
            nest_state = States.HITPOINT_ANGLE
            # if res.arm_state == RobotCommand.Response.IDLE:
            #     nest_state = States.HITPOINT_ANGLE
            # else:
            #     nest_state = None

        elif state == States.HITPOINT_ANGLE:
            self.get_logger().info('TURNINING YAW ANGLE...')
            self.hitpointx = self.strategy_info[4]
            self.hitpointy = self.strategy_info[5]
            vx = self.strategy_info[1]
            vy = self.strategy_info[2]
            yaw, _ = yaw_angle(vx, vy)
            pose = Twist()
            [pose.linear.x, pose.linear.y, pose.linear.z] = [self.hitpointx, self.hitpointy, -70.0]
            if self.obstacle == 0:
                [pose.angular.x, pose.angular.y, pose.angular.z] = [-180., 0., yaw-90.]
            else:
                [pose.angular.x, pose.angular.y, pose.angular.z] = [-180., 20., yaw-90.]
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.PTP,
                # holding=False,
                tool = CUE_TOOL,
                pose = pose
            )
            res = self.call_hiwin(req)
            if res.arm_state == RobotCommand.Response.IDLE:
                nest_state = States.CHECK_POSE
            else:
                nest_state = None

        elif state == States.CHECK_POSE:
            self.get_logger().info('CHECK_POSE')
            req = self.generate_robot_request(
                cmd_mode=RobotCommand.Request.CHECK_POSE
                )
            res = self.call_hiwin(req)
            self.current_pose = res.current_position
            nest_state = States.HITBALL_POSE
            # if res.arm_state == RobotCommand.Response.IDLE:
            #     nest_state = States.HITBALL_POSE
            # else:
            #     nest_state = None

        elif state == States.HITBALL_POSE:
            self.get_logger().info('GOING TO HIT BALL...')
            pose = Twist()
            if self.obstacle == 0:
                [pose.linear.x, pose.linear.y, pose.linear.z] = [self.hitpointx, self.hitpointy, -133.]
            else:
                [pose.linear.x, pose.linear.y, pose.linear.z] = [self.hitpointx, self.hitpointy, -120.642]
            [pose.angular.x, pose.angular.y, pose.angular.z] = self.current_pose[3:6]
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.PTP,
                tool = CUE_TOOL,
                pose = pose
            )
            res = self.call_hiwin(req)
            if res.arm_state == RobotCommand.Response.IDLE:
                nest_state = States.HITBALL
            else:
                nest_state = None

        elif state == States.HITBALL:
            if self.score <= 3000 or self.score == 0:
                hitpin = HITHEAVY_PIN
            elif self.score > 3000 and self.score <=6000:
                hitpin = HITMID_PIN
            else:
                hitpin = HITSOFT_PIN
            self.get_logger().info('OPEN PIN TO HIT BALL')
            print("hit pin IO:", hitpin)
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.DIGITAL_OUTPUT,
                digital_output_cmd = RobotCommand.Request.DIGITAL_ON,
                digital_output_pin = hitpin
            )
            self.call_hiwin(req)

            self.get_logger().info('MOVING BACK TO HIT POINT TOP WITH YAW ANGLE...')
            self.hitpointx = self.strategy_info[4]
            self.hitpointy = self.strategy_info[5]
            vx = self.strategy_info[1]
            vy = self.strategy_info[2]
            yaw, _ = yaw_angle(-vx, -vy)
            pose = Twist()
            [pose.linear.x, pose.linear.y, pose.linear.z] = [self.hitpointx, self.hitpointy, -70.0]
            [pose.angular.x, pose.angular.y, pose.angular.z] = self.current_pose[3:6]
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.PTP,
                holding=False,
                tool = CUE_TOOL,
                pose = pose
            )
            res = self.call_hiwin(req)

            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.DIGITAL_OUTPUT,
                digital_output_cmd = RobotCommand.Request.DIGITAL_OFF,
                digital_output_pin = hitpin
            )
            res = self.call_hiwin(req)

            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.DIGITAL_OUTPUT,
                digital_output_cmd = RobotCommand.Request.DIGITAL_OFF,
                digital_output_pin = HEAVY_PIN
            )
            res = self.call_hiwin(req)
            nest_state = States.AF_HITPOINT_TOP


        elif state == States.AF_HITPOINT_TOP:
            self.get_logger().info('TURNING YAW ANGLE TO HOME...')
            self.hitpointx = self.strategy_info[4]
            self.hitpointy = self.strategy_info[5]
            vx = self.strategy_info[1]
            vy = self.strategy_info[2]
            yaw, _ = yaw_angle(-vx, -vy)
            pose = Twist()
            [pose.linear.x, pose.linear.y, pose.linear.z] = [self.hitpointx, self.hitpointy, -70.0]
            [pose.angular.x, pose.angular.y, pose.angular.z] = [-180., 0., 90.]
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.PTP,
                holding=False,
                tool = CUE_TOOL,
                pose = pose
            )
            res = self.call_hiwin(req)
            nest_state = States.INIT
            # if res.arm_state == RobotCommand.Response.IDLE:
            #     nest_state = States.MOVE_TO_PHOTO_POSE
            # else:
            #     nest_state = None


        elif state == States.CLOSE_ROBOT:
            self.get_logger().info('CLOSE_ROBOT')
            req = self.generate_robot_request(cmd_mode=RobotCommand.Request.CLOSE)
            res = self.call_hiwin(req)
            nest_state = States.FINISH

        else:
            nest_state = None
            self.get_logger().error('Input state not supported!')
            # return
        return nest_state

    def _main_loop(self):
        state = States.INIT
        while state != States.FINISH:
            state = self._state_machine(state)
            if state == None:
                break
        self.destroy_node()

    def _wait_for_future_done(self, future: Future, timeout=-1):
        time_start = time.time()
        while not future.done():
            time.sleep(0.01)
            if timeout > 0 and time.time() - time_start > timeout:
                self.get_logger().error('Wait for service timeout!')
                return False
        return True

    def generate_robot_request(
            self,
            holding=True,
            cmd_mode=RobotCommand.Request.PTP,
            cmd_type=RobotCommand.Request.POSE_CMD,
            velocity=DEFAULT_VELOCITY,
            acceleration=DEFAULT_ACCELERATION,
            tool=1,
            base=0,
            digital_input_pin=0,
            digital_output_pin=0,
            digital_output_cmd=RobotCommand.Request.DIGITAL_OFF,
            pose=Twist(),
            joints=[float('inf')]*6,
            circ_s=[],
            circ_end=[],
            jog_joint=6,
            jog_dir=0
            ):
        request = RobotCommand.Request()
        request.digital_input_pin = digital_input_pin
        request.digital_output_pin = digital_output_pin
        request.digital_output_cmd = digital_output_cmd
        request.acceleration = acceleration
        request.jog_joint = jog_joint
        request.velocity = velocity
        request.tool = tool
        request.base = base
        request.cmd_mode = cmd_mode
        request.cmd_type = cmd_type
        request.circ_end = circ_end
        request.jog_dir = jog_dir
        request.holding = holding
        request.joints = joints
        request.circ_s = circ_s
        request.pose = pose
        return request

    def call_hiwin(self, req):
        while not self.hiwin_client.wait_for_service(timeout_sec=2.0):
            self.get_logger().info('service not available, waiting again...')
        future = self.hiwin_client.call_async(req)
        if self._wait_for_future_done(future):
            res = future.result()
        else:
            res = None
        return res

    def start_main_loop_thread(self):
        self.main_loop_thread = Thread(target=self._main_loop)
        self.main_loop_thread.daemon = True
        self.main_loop_thread.start()

def main(args=None):
    rclpy.init(args=args)

    stratery = Hiwin_Controller()
    stratery.start_main_loop_thread()

    rclpy.spin(stratery)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
