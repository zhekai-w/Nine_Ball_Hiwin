#!/usr/bin/env python3
import time
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
import matplotlib.pyplot as plt

CUE_TOOL = 12 #撞球末段點(製具句換長度)


DEFAULT_VELOCITY = 50 #速度(感覺可改成直接可以打的方式)
DEFAULT_ACCELERATION = 50

LIGHT_PIN = 6 #開控燈
HITSOFT_PIN = 4 #擊球力道大
HITMID_PIN = 5 #擊球力道中
HITHEAVY_PIN = 1 #擊球力道小
HEAVY_PIN = 2 #充電

#加上控制開關的pin腳P.684
#igital_input_pin=

tablewidth = 1920
tableheight = 932 #914

# [1.5683861280265246, -0.0021305364693475553, -3.056812207597806]
FIX_ABS_CAM = [36.326, 376.998, 411.897, 180.0, 0.0, 90.0] #原本手臂拍照的點位
FIX_ABS_RIGHT_CAM = [186.326, 376.998, 411.897, 180.0, 0.0, 90.0] #手臂拍照右 x加減150
FIX_ABS_LEFT_CAM = [-114.326, 376.998, 411.897, 180.0, 0.0, 90.0] #手臂拍照左
END_TURN_RIGHT = [90.00, 0.00, 0.00, 0.00, -90.00, 0.00] #手臂TURN右
# tool_to_cam = [-34.829, 126.788, -66.624]
tool_to_cam = [-36.715, 77.5046, -68.49] #末端點到相機的位移 

CAM_TO_TABLE = 480 #相機到桌子的高度 單位:mm
# CAM_TO_TABLE = 500
CALI_HIGHT = 80.0 #二次校正的高度


class States(Enum):
    INIT = 0
    FINISH = 1
    MOVE_TO_PHOTO_POSE = 2
    DYNAMIC_CALI = 3
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
    MOVE_TO_REPARE_POSE = 19

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

def mid_point_error(mid_ball: list) -> list:
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

#開始控手臂程式
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
        self.table_z = FIX_ABS_CAM[2] + tool_to_cam[2] - CAM_TO_TABLE
    
    # def strategy_callback(self, msg):
    #     _ = msg.data

    def label_callback(self, msg):
        self.all_label = eval(msg.data)

    def yolo_callback(self, msg):
        self.all_ball_pose = msg.data
        self.target_cue = [self.all_ball_pose[:2], self.all_ball_pose[-2:]]
        # self.cue = self.all_ball_pose[-2:]
        # self.target_ball = self.all_ball_pose[:2]

    def _state_machine(self, state: States) -> States:
        if state == States.INIT:
            self.get_logger().info('INIT/TURNING LIGHTS ON')

            nest_state = States.MOVE_TO_REPARE_POSE
        elif state == States.MOVE_TO_REPARE_POSE:
            self.get_logger().info('MOVING TO PREPARE POSE...')
            # joints=[float('inf')]*6,
            print("fix cam joint", END_TURN_RIGHT)
            req = self.generate_robot_request(
                cmd_type=RobotCommand.Request.JOINTS_CMD,
                joints = END_TURN_RIGHT, 
                #不想讓手臂停止才做事(下面if/else不用，直接給下一步的狀態就好)
                #hold=Flase
                )
            res = self.call_hiwin(req)
            if res.arm_state == RobotCommand.Response.IDLE: #讓手臂狀態停止才去做下一件事情
                nest_state = States.MOVE_TO_PHOTO_POSE #存一份topic傳送來的資料
                print("fix cam pose", States)
            else:
                nest_state = None
        elif state == States.MOVE_TO_PHOTO_POSE:
            # value need to be reset every time
            self.updated_target_cue = []
            self.index = 0

            self.get_logger().info('MOVING TO CAMERA POSE...')
            #用到下面generate_robot_reques就要這樣做
            #這裡主要較手臂開燈
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.DIGITAL_OUTPUT,
                digital_output_cmd = RobotCommand.Request.DIGITAL_ON,
                digital_output_pin = LIGHT_PIN
            )
            self.call_hiwin(req) #把上面一整個設定給手臂 call_hiwin
            pose = Twist() #給值之前一定初始化資料型態
            [pose.linear.x, pose.linear.y, pose.linear.z] = FIX_ABS_CAM[0:3]
            [pose.angular.x, pose.angular.y, pose.angular.z] = FIX_ABS_CAM[3:6]
            print("fix cam pose", FIX_ABS_CAM)
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.PTP,
                pose = pose
                #不想讓手臂停止才做事(下面if/else不用，直接給下一步的狀態就好)
                #hold=Flase
                )
            res = self.call_hiwin(req)
            if res.arm_state == RobotCommand.Response.IDLE: #讓手臂狀態停止才去做下一件事情
                nest_state = States.LOCK_INFO #存一份topic傳送來的資料
                print("fix cam pose", States)
            else:
                nest_state = None
        #如果去右邊看球
        elif state == States.FIX_RIGHT_PHOTO_POSE:
            self.fix_check_point = []
            self.get_logger().info('MOVING TO RIGHT PHOTO POSE...')
            #開燈
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.DIGITAL_OUTPUT,
                digital_output_cmd = RobotCommand.Request.DIGITAL_ON,
                digital_output_pin = LIGHT_PIN
            )
            self.call_hiwin(req)
            self.fix_check_point = FIX_ABS_RIGHT_CAM #把右邊的點位給手臂
            pose = Twist()
            [pose.linear.x, pose.linear.y, pose.linear.z] = self.fix_check_point[0:3]
            [pose.angular.x, pose.angular.y, pose.angular.z] = self.fix_check_point[3:6]
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.PTP,
                pose = pose
                )
            res = self.call_hiwin(req)
            if res.arm_state == RobotCommand.Response.IDLE:
                nest_state = States.LOCK_CUE #把白球點位鎖住
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
        #如果鎖定到球就去做動態較正
        elif state == States.LOCK_CUE:
            time.sleep(0.3)
            self.get_logger().info('LOCKING CUE BALL INFO...')
            self.ball_pose_buffer = self.all_ball_pose
            self.label_buffer = self.all_label
            if 'white' in self.label_buffer:
                print("white ball seen")
                temp_ball_pose_mm = pixel_mm_convert(CAM_TO_TABLE, self.ball_pose_buffer[-2:])
                temp_actual_pose = convert_arm_pose(temp_ball_pose_mm, self.fix_check_point)
                self.ball_pose[1] = temp_actual_pose
                self.fix_check_point = FIX_ABS_CAM
                nest_state = States.DYNAMIC_CALI
        
            else:
                print("MOVING TO FIX LEFT POSE...")
                nest_state = States.FIX_LEFT_PHOTO_POSE
            
        elif state == States.LOCK_INFO:
            time.sleep(1)
            self.ball_pose = []
            # input("press enter to lock info...")
            self.get_logger().info('LOCKING INFO FOR STRATEGY AND CALIBRATION...')
            self.ball_pose_buffer = self.all_ball_pose #所有按照順序
            self.label_buffer = self.all_label
            self.target_cue = [self.ball_pose_buffer[:2], self.ball_pose_buffer[-2:]] #x,y,x,y擺第一顆球和最後一個球
            print("target and cue:", self.target_cue)
            #確認是否有白球
            if 'white' in self.label_buffer:
                print("Cue ball seen")
                for target in self.target_cue:
                    print("target:", target)
                    #相機點位轉到手臂點位:做temp的動作
                    temp_ball_pose_mm = pixel_mm_convert(CAM_TO_TABLE, target) #從球相對相機點位
                    temp_actual_pose = convert_arm_pose(temp_ball_pose_mm, FIX_ABS_CAM) #手臂的姿態轉換為手臂的點位
                    self.ball_pose.append(temp_actual_pose[0:2])
                nest_state = States.DYNAMIC_CALI
            #沒有白球
            else:
                print("Fuck Cue ball")
                for target in self.target_cue:
                    print("target:", target)
                    temp_ball_pose_mm = pixel_mm_convert(CAM_TO_TABLE, target)
                    temp_actual_pose = convert_arm_pose(temp_ball_pose_mm, FIX_ABS_CAM)
                    self.ball_pose.append(temp_actual_pose[0:2])
                nest_state = States.FIX_RIGHT_PHOTO_POSE

            
          
        #開始做動態校正
        elif state == States.DYNAMIC_CALI:
            Kp = 0.25 # Proportion constant, P controller
            #這裡把燈關掉
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.DIGITAL_OUTPUT,
                digital_output_cmd = RobotCommand.Request.DIGITAL_OFF,#再看看開著官著哪個會比較好
                digital_output_pin = LIGHT_PIN
            )
            self.call_hiwin(req)
            #開始校正兩顆球(長度小於2)
            if self.index < len(self.target_cue): #初始index=0;target_cue=>2*2矩正
                self.get_logger().info('MOVING TO CALIBRATION POSE...')
                self.get_logger().info('Camera moving to index_{} ball'.format(self.index))
                pose = Twist()
                #先看目標球，直直下去看
                [pose.linear.x, pose.linear.y, pose.linear.z] = [self.ball_pose[self.index][0] - tool_to_cam[0],
                                                                 self.ball_pose[self.index][1] - tool_to_cam[1],
                                                                 self.fix_z]
                # change
                [pose.angular.x, pose.angular.y, pose.angular.z] = FIX_ABS_CAM[3:6]
                print("Pose:", pose)
                # input("Press Enter to continue...")

                req = self.generate_robot_request(
                    cmd_mode = RobotCommand.Request.DIGITAL_OUTPUT,
                    digital_output_cmd = RobotCommand.Request.DIGITAL_ON,
                    digital_output_pin = HEAVY_PIN #在動態校正的時候就開始為了擊大力的球充電
                )
                res = self.call_hiwin(req) #手臂開始下去

                req = self.generate_robot_request(
                cmd_mode=RobotCommand.Request.PTP,
                pose = pose,
                )
                res = self.call_hiwin(req)
                if res.arm_state == RobotCommand.Response.IDLE:
                    print("START DYNAMIC CALIBRATION")
                
                #檢查手臂姿態位置 res可以檢查姿態
                req = self.generate_robot_request(cmd_mode=RobotCommand.Request.CHECK_POSE)
                res = self.call_hiwin(req)
                second_photo = res.current_position 

                #進迴圈到誤差值小於多少
                while True:    
                    # req = self.generate_robot_request(cmd_mode=RobotCommand.Request.CHECK_POSE)
                    # res = self.call_hiwin(req)
                    # second_photo = res.current_position 

                    #check_mid_pose看相機裡面所有球哪一個點離我的相機點位最近
                    #可以直接改成較傳送出點位的那一顆球(學長好像有試過，好像不行)而且校正都校正對ㄟ
                    mid_x, mid_y = check_mid_pose(self.all_ball_pose) 
                    mid_error = mid_point_error([mid_x, mid_y])
                    #傳換成相對於相機相差的長度 
                    ball_relative_cam = pixel_mm_convert(self.fix_z - abs(tool_to_cam[2]) + abs(self.table_z), [mid_x, mid_y])

                    # mid_error = mid_point_error(self.target_cue[self.index])
                    # ball_relative_cam = pixel_mm_convert(self.fix_z - abs(tool_to_cam[2]) + abs(self.table_z), self.target_cue[self.index])
                    #x相加y相減
                    [pose.linear.x, pose.linear.y, pose.linear.z] = [second_photo[0] + Kp*ball_relative_cam[0],
                                                                    second_photo[1] - Kp*ball_relative_cam[1],
                                                                    self.fix_z]
                    [pose.angular.x, pose.angular.y, pose.angular.z] = FIX_ABS_CAM[3:6]
                    
                    # input("Press Enter to continue...")
                    req = self.generate_robot_request(
                    cmd_mode=RobotCommand.Request.PTP,
                    # holding = False,
                    pose = pose
                    )
                    res = self.call_hiwin(req)

                    second_photo[0] += Kp*ball_relative_cam[0] #kp目前0.25
                    second_photo[1] -= Kp*ball_relative_cam[1]

                    # finish calibration condition
                    if abs(mid_error) <= 3: #誤差小於3跳出點位的動作
                        # cv2.destroyAllWindows()
                        break
                
                # update ball position
                ball_relative_cam = pixel_mm_convert(self.fix_z - abs(tool_to_cam[2]) + abs(self.table_z), self.target_cue[self.index])
                req = self.generate_robot_request(cmd_mode=RobotCommand.Request.CHECK_POSE)
                res = self.call_hiwin(req)
                #second_photo代替update_ball
                self.updated_target_cue.append(second_photo[0] + tool_to_cam[0] + ball_relative_cam[0])
                self.updated_target_cue.append(second_photo[1] + tool_to_cam[1] - ball_relative_cam[1])
                #update_ball = res.current_position
                # #self.updated_target_cue.append(update_ball[0] + tool_to_cam[0] + ball_relative_cam[0])
                #self.updated_target_cue.append(update_ball[1] + tool_to_cam[1] - ball_relative_cam[1])
               
                self.index += 1

                if res.arm_state == RobotCommand.Response.IDLE and self.index < len(self.target_cue):
                    nest_state = States.DYNAMIC_CALI
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
         #開始用撞球程式
         #maybe this is a big trouble 
         #決策是用手臂坐標系      
        elif state == States.STRATEGY:
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.DIGITAL_OUTPUT,
                digital_output_cmd = RobotCommand.Request.DIGITAL_OFF,
                digital_output_pin = LIGHT_PIN
            )
            self.call_hiwin(req)
            actual_x = []
            actual_y = []
            self.get_logger().info('UPDATE BALL POSITION')
            for i in range(0, len(self.ball_pose_buffer), 2):
                i_rela_to_cam = pixel_mm_convert(CAM_TO_TABLE, self.ball_pose_buffer[i:i+2]) #把球轉成手臂坐標系
                actual_ball_pose = convert_arm_pose(i_rela_to_cam, FIX_ABS_CAM)
                actual_x.append(actual_ball_pose[0])
                actual_y.append(actual_ball_pose[1])
            print("before cali x:", actual_x)
            print("before cali y:", actual_y)
            print("\n")

            #剛剛更新的球點位
            actual_x[0] = self.updated_target_cue[0]
            actual_y[0] = self.updated_target_cue[1]
            actual_x[-1] = self.updated_target_cue[-2]
            actual_y[-1] =  self.updated_target_cue[-1]
            print("after cali x:", actual_x)
            print("after cali y:", actual_y)
            ballcount = len(actual_x) - 1
            cuex, cuey = self.updated_target_cue[-2], self.updated_target_cue[-1]
            
            self.get_logger().info('CALCULATE PATH')
            # table.main return this [bestscore, bestvx, bestvy, countobs, final_self.hitpointx, final_self.hitpointy]
            self.strategy_info = table2.main(actual_x[:-1], actual_y[:-1], cuex, cuey)
            print("strategy info:", self.strategy_info)
            # for j in range(len(actual_x)-1):
            #     if j == 0:
            #         aimpoint = plt.Circle((actual_x[j], actual_y[j]),
            #                         16, color="green")
            #     else:
            #         aimpoint = plt.Circle((actual_x[j], actual_y[j]),
            #                         16, color="red")
            #     # plt.text(aimpointx[j],aimpointy[j],j,color='red',fontsize=15)
            #     plt.gca().add_patch(aimpoint)
            # plt.gca().add_patch(plt.Circle((cuex, cuey), 16, color='blue'))
            # plt.gca().add_patch(plt.Circle((self.strategy_info[4], self.strategy_info[5]), 3, color='black'))
            # # plt.quiver(cuex, cuey,-self.strategy_info[1], -self.strategy_info[2],color='black',units="xy",angles="xy",scale_units="xy",scale=1, width=2,alpha=0.5)
            # plt.quiver(self.strategy_info[4], self.strategy_info[5],-self.strategy_info[1], -self.strategy_info[2],
            #            color='black',units="xy",angles="xy",scale_units="xy",scale=1, width=2,alpha=0.5)
            # plt.title("sim pool table") 
            # plt.axis([0, tablewidth, 0, tableheight])
            # # plt.autoscale(enable=True, axis='both', tight=None) 
            # plt.axis("equal")
            # plt.show(block=False)
            # input("Enter to close plot...")
            # plt.cla()
            # plt.close()
            nest_state = States.HITPOINT_TOP
            
        elif state == States.HITPOINT_TOP:
            self.score = self.strategy_info[0]
            self.obstacle = self.strategy_info[3]
            self.get_logger().info('MOVING TO HITPOINT TOP...')
            self.hitpointx = self.strategy_info[4]
            self.hitpointy = self.strategy_info[5]
            vx = self.strategy_info[1]
            vy = self.strategy_info[2]
            # yaw, _ = yaw_angle(vx, vy)
            pose = Twist()
            [pose.linear.x, pose.linear.y, pose.linear.z] = [self.hitpointx, self.hitpointy, -70.0]
            if self.obstacle == 0:
                [pose.angular.x, pose.angular.y, pose.angular.z] = [-180., 0., 90.]
            else:
                [pose.angular.x, pose.angular.y, pose.angular.z] = [-180., 17., 90.]
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
                [pose.linear.x, pose.linear.y, pose.linear.z] = [self.hitpointx, self.hitpointy, -112.]
            else:
                [pose.linear.x, pose.linear.y, pose.linear.z] = [self.hitpointx, self.hitpointy, -106.642]
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
            if self.score <= 2000 or self.score == 0:
                hitpin = HITHEAVY_PIN
            elif self.score > 2000 and self.score <=4000:
                hitpin = HITMID_PIN
            else:
                hitpin = HITSOFT_PIN
            # input("Press Enter to Hitball")
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
            nest_state = States.MOVE_TO_PHOTO_POSE
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
            holding=True, #可以控制是否間斷程式
            cmd_mode=RobotCommand.Request.PTP,
            cmd_type=RobotCommand.Request.POSE_CMD,
            velocity=DEFAULT_VELOCITY,
            acceleration=DEFAULT_ACCELERATION,
            tool=1,
            base=0,
            digital_input_pin=0, #改成按按鈕
            digital_output_pin=0,
            digital_output_cmd=RobotCommand.Request.DIGITAL_OFF, #開燈
            pose=Twist(), #x,y,z,row,peach,r
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

#確定有跑手臂那包
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