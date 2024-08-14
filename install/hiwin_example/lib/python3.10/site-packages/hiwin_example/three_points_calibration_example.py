#!/usr/bin/env python3
import time
import rclpy
from enum import Enum
from threading import Thread
from rclpy.node import Node
from rclpy.task import Future
from typing import NamedTuple
from geometry_msgs.msg import Twist

from hiwin_interfaces.srv import RobotCommand
from ros2_aruco_interfaces.srv import ArucoMarkerInfo
# from YoloDetector import YoloDetectorActionClient

from math import *
from scipy.spatial.transform import Rotation as R
import numpy as np
import quaternion as qtn
from hiwin_example import transformations


DEFAULT_VELOCITY = 20
DEFAULT_ACCELERATION = 20
MOVING_VELOCITY = 100

ORIGIN_ID = 15

class States(Enum):
    INIT = 0
    FINISH = 1
    MOVE_TO_PHOTO_POSE = 2
    GET_CALI_POINT = 3
    MOVE_TO_CALI_POINT = 4
    CALCULATE_COORDINATE = 5
    SET_NEW_BASE = 6
    CHECK_POSE = 7
    CLOSE_ROBOT = 8
    MOVE_TO_MARKER_UP = 9

class ThreePointsCalibration(Node):

    def __init__(self):
        super().__init__('three_points_calibration')
        self.calibration_client = self.create_client(ArucoMarkerInfo, 
                                                    'calibration_points')
        self.hiwin_client = self.create_client(RobotCommand, 'hiwinmodbus_service')
        self.object_pose = None
        self.object_cnt = 0
        self.cali_cnt = 0
        self.marker_ids = []
        self.cali_pose = []
        self.marker_pose = []
        self.final_cali_pose = []
        self.new_base = []

        self.declare_parameter("PHOTO_POSE", rclpy.Parameter.Type.DOUBLE_ARRAY)
        self.declare_parameter("camera_intrinsics", rclpy.Parameter.Type.DOUBLE_ARRAY)
        self.declare_parameter("camera_distortion", rclpy.Parameter.Type.DOUBLE_ARRAY)
        self.declare_parameter("tool2cam_quaternion", rclpy.Parameter.Type.DOUBLE_ARRAY)
        self.declare_parameter("tool2cam_trans", rclpy.Parameter.Type.DOUBLE_ARRAY)
        self.declare_parameter("base2tool_quaternion", rclpy.Parameter.Type.DOUBLE_ARRAY)
        self.declare_parameter("base2tool_trans", rclpy.Parameter.Type.DOUBLE_ARRAY)
        self.declare_parameter("input_pin", 1)
        self.photo_pose = self.get_parameter("PHOTO_POSE").get_parameter_value().double_array_value
        self.tool2cam_quaternion = self.get_parameter("tool2cam_quaternion").get_parameter_value().double_array_value
        self.tool2cam_trans = self.get_parameter("tool2cam_trans").get_parameter_value().double_array_value
        self.base2tool_quaternion = self.get_parameter("base2tool_quaternion").get_parameter_value().double_array_value
        self.base2tool_trans = self.get_parameter("base2tool_trans").get_parameter_value().double_array_value
        self.input_pin = self.get_parameter("input_pin").get_parameter_value().integer_value


    def _state_machine(self, state: States) -> States:
        if state == States.INIT:
            self.get_logger().info('INIT')
            nest_state = States.MOVE_TO_PHOTO_POSE

        elif state == States.MOVE_TO_PHOTO_POSE:
            self.get_logger().info('MOVE_TO_PHOTO_POSE')
            pose = Twist()
            req = self.generate_robot_request(
                cmd_type=RobotCommand.Request.JOINTS_CMD,
                joints=self.photo_pose, velocity=MOVING_VELOCITY
                )
            res = self.call_hiwin(req)
            if res.arm_state == RobotCommand.Response.IDLE:
                nest_state = States.GET_CALI_POINT
            else:
                nest_state = None

        elif state == States.GET_CALI_POINT:
            self.get_logger().info('GET_CALI_POINT')
            req = self.generate_robot_request(
                cmd_mode=RobotCommand.Request.CHECK_POSE)
            res = self.call_hiwin(req)
            current_position = res.current_position

            time.sleep(0.2)
            aruco_req = ArucoMarkerInfo.Request()
            aruco_req.process = True
            res = self.call_for_aruco(aruco_req)
            if len(res.marker_ids) == 2 and \
                    (res.marker_ids[0] == ORIGIN_ID or res.marker_ids[1] == ORIGIN_ID):
                if res.marker_ids[0] != ORIGIN_ID:
                    res.marker_ids[0], res.marker_ids[1] = res.marker_ids[1], res.marker_ids[0]
                    res.poses[0], res.poses[1] = res.poses[1], res.poses[0]

                self.marker_ids = res.marker_ids

                self.cali_pose = [self.convert_arm_pose(pose, current_position) for pose in res.poses]

                nest_state = States.MOVE_TO_MARKER_UP
            else:
                if self.cali_cnt > 50:
                    self.get_logger().info('get aruco marker failed')
                    self.cali_cnt = 0
                    nest_state = States.CLOSE_ROBOT
                else:
                    self.cali_cnt += 1
                    pose = Twist()
                    [pose.linear.x, pose.linear.y, pose.linear.z] = current_position[0:3]
                    [pose.angular.x, pose.angular.y, pose.angular.z] = current_position[3:6]
                    pose.angular.x += 0.5
                    req = self.generate_robot_request(
                        cmd_mode=RobotCommand.Request.PTP,
                        pose=pose, velocity=MOVING_VELOCITY)
                    res = self.call_hiwin(req)
                    nest_state = States.GET_CALI_POINT

        elif state == States.MOVE_TO_MARKER_UP:
            self.get_logger().info('MOVE_TO_MARKER_UP')
            req = self.generate_robot_request(
                cmd_mode=RobotCommand.Request.CHECK_POSE)
            res = self.call_hiwin(req)
            pose = Twist()
            [pose.angular.x, pose.angular.y, pose.angular.z] = res.current_position[3:6]
            for p in self.cali_pose:
                pose.linear.x, pose.linear.y, pose.linear.z = p[0:3]
                pose.linear.x += 30
                pose.linear.y += 30
                pose.linear.z += 200
                req = self.generate_robot_request(
                    cmd_mode=RobotCommand.Request.PTP,
                    pose=pose, velocity=MOVING_VELOCITY)
                res = self.call_hiwin(req)

                time.sleep(0.2)
                aruco_req = ArucoMarkerInfo.Request()
                aruco_req.process = True
                marker_pose = None
                marker_poses = []
                for _ in range(10):
                    res = self.call_for_aruco(aruco_req)
                    if len(res.poses) == 0:
                        self.get_logger().warn('FUCK NO MARKER')
                        continue
                    marker_pose = res.poses[0]
                    marker_poses.append([marker_pose.position.x, 
                                         marker_pose.position.y, 
                                         marker_pose.position.z])
                    time.sleep(0.05)

                marker_pose.position.x, marker_pose.position.y,\
                marker_pose.position.z = np.mean(marker_poses, axis=0)
                req = self.generate_robot_request(
                    cmd_mode=RobotCommand.Request.CHECK_POSE)
                res = self.call_hiwin(req)
                p[:] = self.convert_arm_pose(marker_pose, res.current_position)[:]


            print(self.cali_pose)
            extend = [400.0, 150.0, 0.0, 0.0, 0.0, 0.0]
            extend_cali_pose = [self.cali_pose[0][x] + extend[x] for x in range(len(self.cali_pose[0]))]
            print(extend_cali_pose)
            self.cali_pose.insert(1, extend_cali_pose)
            nest_state = States.MOVE_TO_CALI_POINT

        elif state == States.MOVE_TO_CALI_POINT:
            self.get_logger().info('MOVE_TO_CALI_POINT')
            req = self.generate_robot_request(
                cmd_mode=RobotCommand.Request.CHECK_POSE)
            res = self.call_hiwin(req)
            pose = Twist()
            print(self.cali_pose)
            # input()
            pose.angular.x, pose.angular.y, pose.angular.z = res.current_position[3:6]
            for p in self.cali_pose:
                pose.linear.x, pose.linear.y, pose.linear.z = p[0:3]
                pose.linear.z += 90
                req = self.generate_robot_request(
                    cmd_mode=RobotCommand.Request.PTP,
                    pose=pose, velocity=MOVING_VELOCITY)
                res = self.call_hiwin(req)
                if res.arm_state == RobotCommand.Response.IDLE:
                    # input()
                    pose.linear.z = p[2] + 50
                    req = self.generate_robot_request(
                        cmd_mode=RobotCommand.Request.LINE,
                        pose=pose,
                        holding=False)
                    res = self.call_hiwin(req)
                    while 1:
                        req = self.generate_robot_request(
                            cmd_mode=RobotCommand.Request.READ_DI,
                            digital_input_pin=self.input_pin,
                            holding=False)
                        res = self.call_hiwin(req)
                        print(res.digital_state)
                        if res.digital_state:
                            req = self.generate_robot_request(
                                cmd_mode=RobotCommand.Request.CHECK_POSE, holding=False)
                            res = self.call_hiwin(req)
                            self.final_cali_pose.append(res.current_position)
                            req = self.generate_robot_request(
                                cmd_mode=RobotCommand.Request.MOTION_STOP,
                                holding=False)
                            res = self.call_hiwin(req)
                            break

                    up_pose = pose
                    up_pose.linear.z = 80.00
                    req = self.generate_robot_request(
                        cmd_mode=RobotCommand.Request.PTP,
                        pose=up_pose,)
                    res = self.call_hiwin(req)
                    req = self.generate_robot_request(
                        cmd_type=RobotCommand.Request.JOINTS_CMD,
                        joints=self.photo_pose
                        , velocity=MOVING_VELOCITY)
                    res = self.call_hiwin(req)
            nest_state = States.CALCULATE_COORDINATE

        elif state == States.CALCULATE_COORDINATE:
            self.get_logger().info('CALCULATE_COORDINATE')
            self.new_base = self.get_vector()
            nest_state = States.SET_NEW_BASE

        elif state == States.SET_NEW_BASE:
            self.get_logger().info('SET_NEW_BASE')
            pose = Twist()
            [pose.linear.x, pose.linear.y, pose.linear.z] = self.new_base[0:3]
            [pose.angular.x, pose.angular.y, pose.angular.z] = self.new_base[3:6]
            req = self.generate_robot_request(
                cmd_mode=RobotCommand.Request.SET_BASE,
                holding=False,
                pose=pose
            )
            res = self.call_hiwin(req)
            nest_state = States.FINISH


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
        rclpy.shutdown()

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
            base_num = 30,
            tool_num = 30,
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
        request.tool_num = tool_num
        request.base_num = base_num
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

    def call_for_aruco(self, req):
        while not self.calibration_client.wait_for_service(timeout_sec=2.0):
            self.get_logger().info('service not available, waiting again...')
        future = self.calibration_client.call_async(req)
        if self._wait_for_future_done(future):
            res = future.result()
        else:
            res = None
        return res

    def convert_arm_pose(self, aruco_pose, arm_pose):
        base2tool = np.array(arm_pose)
        base2tool[:3] /= 1000

        tool2cam_rot = qtn.as_rotation_matrix(np.quaternion(self.tool2cam_quaternion[3],
                                                            self.tool2cam_quaternion[0], 
                                                            self.tool2cam_quaternion[1], 
                                                            self.tool2cam_quaternion[2]))

        tool2cam_trans = np.array([self.tool2cam_trans])
        
        print("tool2cam_trans = {}".format(tool2cam_trans))
        
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



        cam2aruco_rot = qtn.as_rotation_matrix(np.quaternion(aruco_pose.orientation.w, 
                                                             aruco_pose.orientation.x, 
                                                             aruco_pose.orientation.y, 
                                                             aruco_pose.orientation.z))
        cam2aruco_trans = np.array([[aruco_pose.position.x,
                                     aruco_pose.position.y,
                                     aruco_pose.position.z]])
        
        cam2aruco_mat = np.append(cam2aruco_rot, cam2aruco_trans.T, axis=1)
        cam2aruco_mat = np.append(cam2aruco_mat, np.array([[0., 0., 0., 1.]]), axis=0)

        base2cam_mat = np.matmul(base2tool_mat, tool2cam_mat)
        base2aruco_mat = np.matmul(base2cam_mat, cam2aruco_mat)


        ax, ay, az = transformations.euler_from_matrix(base2aruco_mat)
        base2aruco_translation = transformations.translation_from_matrix(base2aruco_mat)*1000.0

        calibrate_pose = [base2aruco_translation[0], 
                          base2aruco_translation[1], 
                          base2aruco_translation[2],
                          ax*180/3.14, 
                          ay*180/3.14, 
                          az*180/3.14]

        return calibrate_pose

    def get_vector(self, axis = "yx"):
        if axis == "xy":
            new_base_point = self.final_cali_pose[0][0:3]
            x_extend_point = self.final_cali_pose[1][0:3]
            third_point = self.final_cali_pose[2][0:3]
            new_base_point = np.array(new_base_point)
            x_extend_point = np.array(x_extend_point)
            third_point = np.array(third_point)

            Vector_X = x_extend_point - new_base_point     # X軸向量
            Vector_other = third_point - new_base_point    # base and other 兩點向量
            Vector_Z = np.cross(Vector_X, Vector_other) # 外積出Z軸向量
            Vector_Y = np.cross(Vector_Z, Vector_X)  # 外積出Y軸向量

        elif axis == "yx":

            new_base_point = self.final_cali_pose[0][0:3]
            y_point = self.final_cali_pose[2][0:3]
            third_point = self.final_cali_pose[1][0:3]
            new_base_point = np.array(new_base_point)
            y_point = np.array(y_point)
            third_point = np.array(third_point)

            Vector_Y =  y_point - new_base_point      # Y軸向量
            Vector_other = third_point - new_base_point   # base and other 兩點向量
            Vector_Z = np.cross(Vector_other, Vector_Y) # 外積出Z軸向量
            Vector_X = np.cross(Vector_Y, Vector_Z)  # 外積出X軸向量

        vx = Vector_X / np.linalg.norm(Vector_X)    # 轉成單位向量
        vy = Vector_Y / np.linalg.norm(Vector_Y)
        vz = Vector_Z / np.linalg.norm(Vector_Z)


        Transpose = np.array([vx, vy, vz]).T
        r = R.from_matrix(Transpose)
        euler_angle = r.as_euler('xyz', degrees=True)
        print(euler_angle)

        new_base = [new_base_point[0], 
                  new_base_point[1], 
                  new_base_point[2], 
                  euler_angle[0], 
                  euler_angle[1], 
                  euler_angle[2]]
        print(new_base)

        return new_base

    def start_calibration_thread(self):
        self.main_loop_thread = Thread(target=self._main_loop)
        self.main_loop_thread.daemon = True
        self.main_loop_thread.start()



def main(args=None):
    rclpy.init(args=args)

    stratery = ThreePointsCalibration()
    stratery.start_calibration_thread()

    rclpy.spin(stratery)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
