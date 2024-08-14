import time
import rclpy
from enum import Enum
from threading import Thread
from rclpy.node import Node
from rclpy.task import Future
from typing import NamedTuple
from geometry_msgs.msg import Twist

from hiwin_interfaces.srv import RobotCommand
from yolo_strategy_interfaces.srv import YoloStrategy

import cv2
import pyrealsense2 as rs
import numpy as np
import math

"""
擊球準備 (BF_HITBALL_POSE)
擊球 (HITBALL)
檢查位置 (CHECK_POSE)
收尾動作 (AF_HITBALL_POSE_2 和 MOVE_TO_PHOTO_POSE)
"""

#定義全局變量:定義了機器人臂的工具號和基座號。配置了速度和加速度的預設值。
#定義了一些 I/O 接腳用於機器人的操作。設定了工作平台的尺寸，以像素和毫米為單位。
MY_BASE = 12
CUE_TOOL = 12
CAM_TOOL = 11
DEFAULT_TOOL = 0 

DEFAULT_VELOCITY = 25
DEFAULT_ACCELERATION = 25

LIGHT_PIN = 6
HITSOFT_PIN = 4
HITMID_PIN = 5
HITHEAVY_PIN = 1
HEAVY_PIN = 2

tablewidth = 1920
tableheight = 932 #914
tablewidth_mm = 627
tableheight_mm = 304

#枚舉定義機器人的操作狀態，每個狀態代表機器人的一個動作階段。
class States(Enum):
    INIT = 0
    FINISH = 1
    MOVE_TO_PHOTO_POSE = 2
    TAKE_PHOTO = 33
    YOLO_DETECT = 4
    #計算出的擊球點調整位置。
    BF_HITBALL_POSE = 5
    BF_HITBALL_POSE_2 = 16
    HITBALL_POSE = 6
    HITBALL = 7
    AF_HITBALL_POSE = 8
    AF_HITBALL_POSE_2 = 17
    CHECK_POSE = 9
    CLOSE_ROBOT = 10
    WAITING = 11
    OPEN_SEC_IO =  12
    SECOND_PHOTO = 13
    RECALCULATE = 14
    CLOSE_SECOND_IO = 15

fix_abs_cam = [48.809, 310.996, 383.971, -179.499, -3.45, 89.95]
tool_to_cam = [-36.862, 128.23, -66.272]
CAM_TO_TABLE = 481

#使用 Intel RealSense 相機設備進行影像的捕獲。
#判斷是拍攝第一張還是第二張照片，並將影像保存。
def take_pics(first_or_second):
    # Create a context object. This object owns the handles to all connected realsense devices
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.color, 1920, 1080, rs.format.bgr8, 30)
    a = 0
    # Start streaming
    pipeline.start(config)  
    
    while True:

        # Wait for a coherent pair of frames: depth and color
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        # if not color_frame:
        #     continue

        # Convert images to numpy arrays
        color_image = np.asanyarray(color_frame.get_data())  

        # Show images
        cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('RealSense', color_image)
        
        if first_or_second == 1:
            # print('Press m to take pictures\n')
            # print('Press q to quit camera\n')  
            key = cv2.waitKey(1)
            if key&0xFF==ord('m'):
                print("Pciture Taken")
            cv2.imwrite('/home/zack/work/ROS2_ws/src/py_pubsub/py_pubsub/testpics/detect_ball.jpg',color_image)
            if key&0xFF==ord('q'):
                cv2.destroyAllWindows()
                break

        else:
            cv2.imwrite('/home/zack/work/ROS2_ws/src/py_pubsub/py_pubsub/testpics/detect_second_ball.jpg', color_image)
            cv2.destroyAllWindows()
            break
    # Stop streaming
    pipeline.stop() 

def mm_to_pixels(mmx, mmy):
    px = tablewidth*mmx/tablewidth_mm
    py = tableheight*mmy/tableheight_mm
    return px, py

#節點定義與機器人操作
#這個類繼承自 ROS 2 的 Node，負責管理整個機器人的操作流程。
#利用狀態機模型來控制機器人的不同階段，如初始化、移動、拍照、物體檢測等。
class ArmsDealer_2(Node):
    def __init__(self):
        super().__init__('arms_dealer')
        self.strategy_client = self.create_client(YoloStrategy, 'yolo_strategy')
        # while not self.strategy_client.wait_for_service(timeout_sec=2.0):
        self.yolo_req = YoloStrategy.Request()

        # Hiwin client
        self.hiwin_client = self.create_client(RobotCommand, 'hiwinmodbus_service')
        self.cue_hitpoint = []
        self.ball_in_route = []
        self.Nballinroute = 0
        self.yolo_state = 0
        self.obs_flag = 0
        self.current_pose = []
        self.fix_z = 80.0
        self.real_ball_position = []
    # 根據當前的狀態執行不同的動作
    def strategy_state(self, state:States) -> States:
        if state == States.INIT:
            # 初始化相機位置
            self.get_logger().info('Moving to camera point')
            pose = Twist()
            # 設定機器人的位置和姿態
            [pose.linear.x, pose.linear.y, pose.linear.z] = fix_abs_cam[0:3]
            [pose.angular.x, pose.angular.y, pose.angular.z] = fix_abs_cam[3:6]
             # 創建並發送機器人命令
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.PTP,
                pose = pose
                )
            res = self.call_hiwin(req)
            # 判斷機器人是否完成操作
            if res.arm_state == RobotCommand.Response.IDLE:
                nest_state = States.TAKE_PHOTO
            else:
                nest_state = None

        elif state == States.TAKE_PHOTO:
            self.get_logger().info('Taking photo\n')
            take_pics(1)
            time.sleep(1)
            self.get_logger().info('Photo Taken\n')
            self.yolo_state = 1
            nest_state = States.YOLO_DETECT

        elif state == States.YOLO_DETECT:
            if self.yolo_state == 1:
                self.ball_in_route = []
                self.obs_flag = 0
                self.get_logger().info('Detecting all hitpoint location\n')
                # flat array. First two indexis are for cueballx and y幫大部分進行註解，每一行也註解

                '''
                request type for call_yolo()
                request 1 for hitpoint position, yaw angle and route score (in pixels)
                request 2 for all ball position in 1D array, first half of the array
                  is for x-axis the other half is for y-axis 
                  last index of every axis is for cueball position (in pixel)
                request 3 for all ball position that are in best route (in mm)
                request 4 to update ball position and recalculate hitpoint and yaw angle (in mm)
                '''

                self.yolo_req.send_position = 3 
                yolo_res_ballinroute = self.call_yolo(self.yolo_req) # request 3 for ball in route
                self.ball_in_route = yolo_res_ballinroute.current_position
                self.obs_flag = yolo_res_ballinroute.obstacle_flag
                self.Nballinroute = len(self.ball_in_route)
                # nest_state = States.BF_HITBALL_POSE
                nest_state = States.SECOND_PHOTO
            elif self.yolo_state == 2:
                # self.cue_hitpoint = []
                # self.get_logger().info('Detecting specific hitpoint location\n')
                # self.yolo_req.send_position = 1
                # yolo_res = self.call_yolo(self.yolo_req) # request 1 for cueball hitpoint and vector
                # self.cue_hitpoint = yolo_res.current_position
                # print('cue_hitpoint:',self.cue_hitpoint)
                nest_state = States.BF_HITBALL_POSE
            else:
                nest_state = None
            
        elif state == States.SECOND_PHOTO:
            self.real_ball_position = []
            for i in range(0, self.Nballinroute, 2):
                self.get_logger().info('Moving to second photo pose %d\n'%i)
                pose = Twist()
                print('first ball position x:',self.ball_in_route[i])
                print('first ball position y:',self.ball_in_route[i+1])
                [pose.linear.x, pose.linear.y, pose.linear.z] = [self.ball_in_route[i] - tool_to_cam[0] , 
                                                                 self.ball_in_route[i+1] - tool_to_cam[1] , 
                                                                 self.fix_z]
                [pose.angular.x, pose.angular.y, pose.angular.z] = fix_abs_cam[3:6]
                req = self.generate_robot_request(
                    cmd_mode = RobotCommand.Request.PTP,
                    pose = pose
                )
                self.call_hiwin(req)

                take_pics(2)
                time.sleep(1.0)
                self.get_logger().info('Photo taken\n')
              
                # call yolo 2 to adjust for error
                self.yolo_req.send_position = 2
                yolo_second_res = self.call_yolo(self.yolo_req)
                # return midball position reletive to camera
                ball_relative_cam = yolo_second_res.current_position

                self.get_logger().info('Reading current arm pose\n')
                req = self.generate_robot_request(
                    cmd_mode=RobotCommand.Request.CHECK_POSE)
                res = self.call_hiwin(req)
                current_pose = res.current_position
                # flat array. First two indexis are for cueballx/y
                self.real_ball_position.append(current_pose[0]+tool_to_cam[0]+ball_relative_cam[0]+5.0)
                self.real_ball_position.append(current_pose[1]+tool_to_cam[1]-ball_relative_cam[1])
                print('actual ball position x:\n', current_pose[0]+tool_to_cam[0]+ball_relative_cam[0]+5.0)
                print('actual ball position y:\n', current_pose[1]+tool_to_cam[1]-ball_relative_cam[1])
            
            if res.arm_state == RobotCommand.Response.IDLE:
                nest_state = States.RECALCULATE
            else:
                nest_state = None

        elif state == States.RECALCULATE:
            self.cue_hitpoint = []
            print('updated position:\n',self.real_ball_position)
            self.yolo_req.update_position = self.real_ball_position
            self.yolo_req.send_position = 4 # request 4 to update cueball hitpoint and vector
            re_yolo_res = self.call_yolo(self.yolo_req)
            self.get_logger().info('Reculculating hit ball location\n')
            self.cue_hitpoint = re_yolo_res.current_position
            print('cue_hitpoint:',self.cue_hitpoint)
            nest_state = States.BF_HITBALL_POSE

        elif state == States.BF_HITBALL_POSE:
            self.get_logger().info('Before hitting cueball\n')
            pose = Twist()
            ####################convert from arm base to mother board
            [pose.linear.x, pose.linear.y, pose.linear.z] = [self.cue_hitpoint[0], self.cue_hitpoint[1], -70.0]
            if self.obs_flag == 0:
                [pose.angular.x, pose.angular.y, pose.angular.z] = [-180., 0., 90.]
            else:
                [pose.angular.x, pose.angular.y, pose.angular.z] = [-180., 20.0, 90.]
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.PTP,
                # holding=False,
                tool = CUE_TOOL,
                pose = pose
            )
            res = self.call_hiwin(req)
            if res.arm_state == RobotCommand.Response.IDLE:
                nest_state = States.OPEN_SEC_IO
            else:
                nest_state = None

        

        elif state == States.OPEN_SEC_IO:
            self.get_logger().info('Opening second IO\n')
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.DIGITAL_OUTPUT,
                digital_output_cmd = RobotCommand.Request.DIGITAL_ON,
                digital_output_pin = HEAVY_PIN
            )
            res = self.call_hiwin(req)
            if res.arm_state == RobotCommand.Response.IDLE:
                nest_state = States.BF_HITBALL_POSE_2
            else:
                nest_state = None

        elif state == States.BF_HITBALL_POSE_2:
                    self.get_logger().info('Turning yaw angle\n')
                    pose = Twist()
                    ####################convert from arm base to mother board
                    [pose.linear.x, pose.linear.y, pose.linear.z] = [self.cue_hitpoint[0], self.cue_hitpoint[1], -70.0]
                    if self.obs_flag == 0:
                        [pose.angular.x, pose.angular.y, pose.angular.z] = [-180., 0., self.cue_hitpoint[2]-90.]
                    else:
                        [pose.angular.x, pose.angular.y, pose.angular.z] = [-180., 20.0, self.cue_hitpoint[2]-90.]
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
        #檢查位置
        elif state == States.CHECK_POSE:
            self.get_logger().info('CHECK_POSE')
            req = self.generate_robot_request(
                cmd_mode=RobotCommand.Request.CHECK_POSE
                )
            res = self.call_hiwin(req)
            # print(res.current_position)
            self.current_pose = res.current_position
            if res.arm_state == RobotCommand.Response.IDLE:
                nest_state = States.HITBALL_POSE
            else:
                nest_state = None

        elif state == States.HITBALL_POSE:
            self.get_logger().info('Going to hit cueball\n')
            pose = Twist()
            if self.obs_flag == 0:
                [pose.linear.x, pose.linear.y, pose.linear.z] = [self.cue_hitpoint[0], self.cue_hitpoint[1], -132.0]
            else:
                [pose.linear.x, pose.linear.y, pose.linear.z] = [self.cue_hitpoint[0], self.cue_hitpoint[1], -119.0]
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
        #擊球
        elif state == States.HITBALL:
            self.get_logger().info('Hitting cueball\n')
            req = self.generate_robot_request(
                cmd_mode=RobotCommand.Request.WAITING
            )
            res = self.call_hiwin(req)
            # how hard it hits. Decided by the score of the route
            # if self.cue_hitpoint[-1] >= 5000:
            #     hit_pin = HITSOFT_PIN
            if self.cue_hitpoint[-1] >= 3000:
                hit_pin = HITMID_PIN
            else:
                hit_pin = HITHEAVY_PIN

            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.DIGITAL_OUTPUT,
                digital_output_cmd = RobotCommand.Request.DIGITAL_ON,
                digital_output_pin = hit_pin
            )
            self.call_hiwin(req)
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.DIGITAL_OUTPUT,
                digital_output_cmd = RobotCommand.Request.DIGITAL_OFF,
                digital_output_pin = hit_pin
            )
            res = self.call_hiwin(req)
            req = self.generate_robot_request(
                cmd_mode=RobotCommand.Request.WAITING
            )
            res = self.call_hiwin(req)撞球末段點(製具句換長度)D_IO:
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.DIGITAL_OUTPUT,
                digital_output_cmd = RobotCommand.Request.DIGITAL_OFF,
                digital_output_pin = HEAVY_PIN
            )
            res = self.call_hiwin(req)
            if res.arm_state == RobotCommand.Response.IDLE:
                nest_state = States.AF_HITBALL_POSE_2
            else:
                nest_state = None
        #擊球後，機械臂需移回初始或安全位置，準備下一次操作。
        elif state == States.AF_HITBALL_POSE_2:
            pose = Twist()
            ####################convert from arm base to mother board
            [pose.linear.x, pose.linear.y, pose.linear.z] = [self.cue_hitpoint[0], self.cue_hitpoint[1], -70.0]
            if self.obs_flag == 0:
                [pose.angular.x, pose.angular.y, pose.angular.z] = [-180., 0., self.cue_hitpoint[2]-90.]
            else:
                [pose.angular.x, pose.angular.y, pose.angular.z] = [-180., 20.0, self.cue_hitpoint[2]-90.]
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.PTP,
                # holding=False,
                tool = CUE_TOOL,
                pose = pose
            )
            res = self.call_hiwin(req)
            if res.arm_state == RobotCommand.Response.IDLE:
                nest_state = States.AF_HITBALL_POSE
            else:
                nest_state = None
        
        elif state == States.AF_HITBALL_POSE:
            self.get_logger().info('Moving back to photo pose\n')
            pose = Twist()
            [pose.linear.x, pose.linear.y, pose.linear.z] = [self.cue_hitpoint[0], self.cue_hitpoint[1], -70.0]
            [pose.angular.x, pose.angular.y, pose.angular.z] = fix_abs_cam[3:6]
            req = self.generate_robot_request(
                cmd_mode = RobotComman撞球末段點(製具句換長度)VE_TO_PHOTO_POSE
            else:
                nest_state = None

        elif state == States.MOVE_TO_PHOTO_POSE:
            self.cue_hitpoint = [] # clear array for next use
            self.get_logger().info('Moving to photo pose\n')
            pose = Twist()
            [pose.linear.x, pose.linear.y, pose.linear.z] = fix_abs_cam[0:3]
            [pose.angular.x, pose.angular.y, pose.angular.z] = fix_abs_cam[3:6]
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.PTP,
                pose = pose
            )
            res = self.call_hiwin(req)
            if res.arm_state == RobotCommand.Response.IDLE:
                nest_state = States.TAKE_PHOTO
            else:
                nest_state = None

        else:
            nest_state = None
            self.get_logger().info('input state not supported!\n')

        return nest_state
    
    def _main_loop(self):
        state = States.INIT
        while state != States.FINISH:
            state = self.strategy_state(state)
            if state == None:
                break
        self.destroy_node()
    #函數用於創建機器人操作請求
    def generate_robot_request(
            self, 
            holding=True,
            cmd_mode=RobotCommand.Request.PTP,
            cmd_type=RobotCommand.Request.POSE_CMD,
            velocity=DEFAULT_VELOCITY,
            acceleration=DEFAULT_ACCELERATION,
            tool=0,
            base=0,
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
    #用於非同步調用機器人服務並等待結果。
    def call_hiwin(self, req):
        while not self.hiwin_client.wait_for_service(timeout_sec=2.0):
            self.get_logger().info('service not available, waiting again...')
        future = self.hiwin_client.call_async(req)
        if self._wait_for_future_done(future):
            res = future.result()
        else:
            res = None
        return res

    def call_yolo(self, req):
        while not self.strategy_client.wait_for_service(timeout_sec=2.0):
            self.get_logger().info('YOLO service not available, waiting again...')
        future = self.strategy_client.call_async(req)
        if self._wait_for_future_done(future):
            res = future.result()
        else:
            res = None
        return res
    
    def _wait_for_future_done(self, future: Future, timeout=-1):
        time_start = time.time()
        while not future.done():
            time.sleep(0.01)
            if timeout > 0 and time.time() - time_start > timeout:
                self.get_logger().error('Wait for service timeout!')
                return False
        return True
    #啟動主循環(start_main_loop_thread)的方法和一個測試函數(test_request)，這允許用戶手動測試機器人的行為。
    def start_main_loop_thread(self):
        self.main_loop_thread = Thread(target=self._main_loop)
        self.main_loop_thread.daemon = True
        self.main_loop_thread.start()

    def test_request(self):
        key = input('Enter 1 or 0 to send ball location:\n')
        if key == '1':
            oi = 3
        else:
            oi = 0
        self.yolo_req.send_position = oi
        future = self.strategy_client.call_async(self.yolo_req)
        rclpy.spin_until_future_complete(self, future)
        # if self._wait_for_future_done(future):
        #     res = future.result()
        # else:
        #     res = None
       
        return future.result()
    
class ArmsDealer(Node):
    def __init__(self):
        super().__init__('arms_dealer_2')
        self.strategy_client = self.create_client(YoloStrategy, 'yolo_strategy')
        # while not self.strategy_client.wait_for_service(timeout_sec=2.0):
        self.yolo_req = YoloStrategy.Request()

        # Hiwin client
        self.hiwin_client = self.create_client(RobotCommand, 'hiwinmodbus_service')
        self.cue_hitpoint = []
        self.ball_in_route = []
        self.Nballinroute = 0
        self.yolo_state = 0
        self.obs_flag = 0
        self.ball_position_pixels = []
        self.current_pose = []

    def strategy_state(self, state:States) -> States:
        if state == States.INIT:
            self.get_logger().info('Moving to calculated camera point')
            pose = Twist()
            [pose.linear.x, pose.linear.y, pose.linear.z] = fix_abs_cam[0:3]
            [pose.angular.x, pose.angular.y, pose.angular.z] = fix_abs_cam[3:6]
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.PTP,
                tool = CAM_TOOL,
                pose = pose
                )
            res = self.call_hiwin(req)
            if res.arm_state == RobotCommand.Response.IDLE:
                nest_state = States.SEC_IO
            else:
                nest_state = None

        elif state == States.SEC_IO:
            self.get_logger().info('Turning second IO on for heavy hit\n')
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.DIGITAL_OUTPUT,
                digital_output_cmd = RobotCommand.Request.DIGITAL_ON,
                digital_output_pin = HEAVY_PIN
            )
            self.call_hiwin(req)
            nest_state = States.TAKE_PHOTO

        elif state == States.TAKE_PHOTO:
            self.get_logger().info('Taking photo\n')
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.DIGITAL_OUTPUT,
                digital_output_cmd = RobotCommand.Request.DIGITAL_ON,
                digital_output_pin = LIGHT_PIN
            )
            # time.sleep(1.0)
            self.call_hiwin(req)
            take_pics(1)
            
            self.get_logger().info('Taking photo\n')
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.DIGITAL_OUTPUT,
                digital_output_cmd = RobotCommand.Request.DIGITAL_OFF,
                digital_output_pin = LIGHT_PIN
            )
            res = self.call_hiwin(req)
            self.yolo_state = 1
            nest_state = States.WAITING

        elif state == States.WAITING:
            req = self.generate_robot_request(
                cmd_mode=RobotCommand.Request.WAITING
            )
            res = self.call_hiwin(req)
            if res.arm_state == RobotCommand.Response.IDLE:
                nest_state = States.YOLO_DETECT
            else:
                nest_state = None

        elif state == States.YOLO_DETECT:
            if self.yolo_state == 1:
                self.ball_in_route = []
                self.obs_flag = 0
                self.get_logger().info('Detecting all hitpoint location\n')
                # flat array. First two indexis are for cueballx and y

                '''
                request type for call_yolo()
                request 1 for hitpoint position, yaw angle and route score (in pixel)
                request 2 for all ball position in 1D array, first half of the array
                  is for x-axis the other half is for y-axis 
                  last index of every axis is for cueball position (in pixel)
                request 3 for all ball position that are in best route (in mm)
                request 4 to update ball position and recalculate hitpoint and yaw angle
                '''

                self.yolo_req.send_position = 3 
                yolo_res_ballinroute = self.call_yolo(self.yolo_req) # request 3 for ball in route
                self.ball_in_route = yolo_res_ballinroute.current_position
                self.obs_flag = yolo_res_ballinroute.obstacle_flag
                self.Nballinroute = len(self.ball_in_route)
                # nest_state = States.BF_HITBALL_POSE
                nest_state = States.SECOND_PHOTO
            elif self.yolo_state == 2:
                # self.cue_hitpoint = []
                # self.get_logger().info('Detecting specific hitpoint location\n')
                # self.yolo_req.send_position = 1
                # yolo_res = self.call_yolo(self.yolo_req) # request 1 for cueball hitpoint and vector
                # self.cue_hitpoint = yolo_res.current_position
                # print('cue_hitpoint:',self.cue_hitpoint)
                nest_state = States.BF_HITBALL_POSE
            else:
                nest_state = None
            
        elif state == States.SECOND_PHOTO:
            real_ball_position = []
            for i in range(0, self.Nballinroute, 2):
                self.get_logger().info('Moving to second photo pose %d\n'%i)
                pose = Twist()
                print(self.ball_in_route[i])
                print(self.ball_in_route[i+1])
                [pose.linear.x, pose.linear.y, pose.linear.z] = [self.ball_in_route[i], self.ball_in_route[i+1], -200.0]
                [pose.angular.x, pose.angular.y, pose.angular.z] = fix_abs_cam[3:6]
                req = self.generate_robot_request(
                    cmd_mode = RobotCommand.Request.PTP,
                    holding = True,
                    tool = CAM_TOOL,
                    pose = pose
                )
                self.call_hiwin(req)

                req = self.generate_robot_request(
                cmd_mode=RobotCommand.Request.WAITING
                )
                res = self.call_hiwin(req)

                self.get_logger().info('Taking second photo to correct ball position\n')
                req = self.generate_robot_request(
                    cmd_mode = RobotCommand.Request.DIGITAL_OUTPUT,
                    digital_output_cmd = RobotCommand.Request.DIGITAL_ON,
                    digital_output_pin = LIGHT_PIN
                )
                self.call_hiwin(req)
                take_pics(2)
                time.sleep(1.0)
                self.get_logger().info('Photo taken\n')
                req = self.generate_robot_request(
                    cmd_mode = RobotCommand.Request.DIGITAL_OUTPUT,
                    digital_output_cmd = RobotCommand.Request.DIGITAL_OFF,
                    digital_output_pin = LIGHT_PIN
                )
                res = self.call_hiwin(req)
                # call yolo to see ball position
                self.yolo_req.send_position = 2
                yolo_second_res = self.call_yolo(self.yolo_req)
                # return whole list, first half of list for x-axis and second half for y-axis
                obj = yolo_second_res.current_position
                l = len(obj)/2
                l = int(l)
                objx = obj[0:l]
                objy = obj[l:l*2]
                print('close objx:\n', objx)
                print('close objy:\n',objy)
                # calculate closest ball relative to pixel mid point (1920/2, 1080/2)
                # we only need the middle ball position here
                dis = []
                missx = []
                missy = []
                for j in range(0,l):
                    disx = objx[j]- tablewidth/2  # not actual tablewidth and height, but in pixels 1920*1080 
                    disy = objy[j] - 1080/2
                    temp_dis = math.sqrt((disx)**2+(disy)**2)
                    dis.append(temp_dis)
                    missx.append(disx)
                    missy.append(disy)
                midball_index = dis.index(min(dis))
                devx = missx[midball_index]
                devy = missy[midball_index]
                
                devmmx = devx*(tablewidth_mm*200)/(tablewidth*(-fix_abs_cam[2]))
                devmmy = devy*(tableheight_mm*200)/(tableheight*(-fix_abs_cam[2]))
                # print('pixel deviation x:\n', devx)
                # print('pixel deviation y:\n', devy)
                # print('actual deviation x:\n', devmmx)
                # print('actual deviation y:\n', devmmy)

                self.get_logger().info('Reading current arm pose\n')
                req = self.generate_robot_request(
                    cmd_mode=RobotCommand.Request.CHECK_POSE,
                    tool = CAM_TOOL
                    )
                res = self.call_hiwin(req)
                current_pose = res.current_position
                # flat array. First two indexis are for cueballx and y
                real_ball_position.append(current_pose[0]+devmmx)
                real_ball_position.append(current_pose[1]+devmmy)
                print('cam tool x:\n', current_pose[0])
                print('cam tool y:\n', current_pose[1])
                print('###################')
                print('actual ball position x:\n', current_pose[0]+devmmx)
                print('actual ball position y:\n', current_pose[1]+devmmy)

            # convert real_ball_position from mm to pixels for strategy
            self.ball_position_pixels = []
            for j in range(0, len(real_ball_position), 2):
                tempx, tempy = mm_to_pixels(real_ball_position[j], real_ball_position[j+1])
                self.ball_position_pixels.append(tempx)
                self.ball_position_pixels.append(tempy)
            
            if res.arm_state == RobotCommand.Response.IDLE:
                nest_state = States.RECALCULATE
            else:
                nest_state = None

        elif state == States.RECALCULATE:
            self.cue_hitpoint = []
            print('updated position:\n',self.ball_position_pixels)
            self.yolo_req.update_position = self.ball_position_pixels
            self.yolo_req.send_position = 4 # request 4 to update cueball hitpoint and vector
            re_yolo_res = self.call_yolo(self.yolo_req)
            self.get_logger().info('Reculculating hit ball location\n')
            self.cue_hitpoint = re_yolo_res.current_position
            print('cue_hitpoint:',self.cue_hitpoint)
            nest_state = States.BF_HITBALL_POSE

        elif state == States.BF_HITBALL_POSE:
            self.get_logger().info('Before hitting cueball\n')
            pose = Twist()
            ####################convert from arm base to mother board
            [pose.linear.x, pose.linear.y, pose.linear.z] = [self.cue_hitpoint[0], self.cue_hitpoint[1], -70.0]
            if self.obs_flag == 0:
                [pose.angular.x, pose.angular.y] = fix_abs_cam[3:5]
            else:
                [pose.angular.x, pose.angular.y] = [fix_abs_cam[3], -20.0]
            pose.angular.z = fix_abs_cam[5] - 90
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.PTP,
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
                cmd_mode=RobotCommand.Request.CHECK_POSE )
            res = self.call_hiwin(req)
            # print(res.current_position)
            self.current_pose = res.current_position
            if res.arm_state == RobotCommand.Response.IDLE:
                nest_state = States.HITBALL_POSE
            else:
                nest_state = None

        elif state == States.HITBALL_POSE:
            self.get_logger().info('Going to hit cueball\n')
            pose = Twist()
            if self.obs_flag == 0:
                [pose.linear.x, pose.linear.y, pose.linear.z] = [self.cue_hitpoint[0], self.cue_hitpoint[1], -20.0]
            else:
                [pose.linear.x, pose.linear.y, pose.linear.z] = [self.cue_hitpoint[0], self.cue_hitpoint[1], -30.0]
            [pose.angular.x, pose.angular.y] = self.current_pose[3:5]
            pose.angular.z = self.cue_hitpoint[2]-90
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.LINE,
                pose = pose
            )
            res = self.call_hiwin(req)
            if res.arm_state == RobotCommand.Response.IDLE:
                nest_state = States.HITBALL
            else:
                nest_state = None
        
        elif state == States.HITBALL:
            self.get_logger().info('Hitting cueball\n')
            req = self.generate_robot_request(
                cmd_mode=RobotCommand.Request.WAITING
            )
            res = self.call_hiwin(req)
            # how hard it hits. Decided by the score of the route
            # if self.cue_hitpoint[-1] >= 5000:
            #     hit_pin = HITSOFT_PIN
            if self.cue_hitpoint[-1] >= 3000:
                hit_pin = HITMID_PIN
            else:
                hit_pin = HITHEAVY_PIN

            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.DIGITAL_OUTPUT,
                digital_output_cmd = RobotCommand.Request.DIGITAL_ON,
                digital_output_pin = hit_pin
            )
            self.call_hiwin(req)
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.DIGITAL_OUTPUT,
                digital_output_cmd = RobotCommand.Request.DIGITAL_OFF,
                digital_output_pin = hit_pin
            )
            res = self.call_hiwin(req)
            req = self.generate_robot_request(
                cmd_mode=RobotCommand.Request.WAITING
            )
            res = self.call_hiwin(req)
            if res.arm_state == RobotCommand.Response.IDLE:
                nest_state = States.AF_HITBALL_POSE
            else:
                nest_state = None
        
        elif state == States.AF_HITBALL_POSE:
            self.get_logger().info('Moving back to photo pose\n')
            pose = Twist()
            [pose.linear.x, pose.linear.y, pose.linear.z] = [self.cue_hitpoint[0], self.cue_hitpoint[1], -70.0]
            [pose.angular.x, pose.angular.y] = fix_abs_cam[3:5]
            pose.angular.z = fix_abs_cam[5] - 90
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.LINE,
                pose = pose,
            )
            res = self.call_hiwin(req)
            if res.arm_state == RobotCommand.Response.IDLE:
                nest_state = States.MOVE_TO_PHOTO_POSE
            else:
                nest_state = None

        elif state == States.MOVE_TO_PHOTO_POSE:
            self.cue_hitpoint = [] # clear array for next use
            self.get_logger().info('Moving to photo pose\n')
            pose = Twist()
            [pose.linear.x, pose.linear.y, pose.linear.z] = fix_abs_cam[0:3]
            [pose.angular.x, pose.angular.y, pose.angular.z] = fix_abs_cam[3:6]
            req = self.generate_robot_request(
                cmd_mode = RobotCommand.Request.PTP,
                tool = CAM_TOOL,
                pose = pose
            )
            res = self.call_hiwin(req)
            if res.arm_state == RobotCommand.Response.IDLE:
                nest_state = States.TAKE_PHOTO
            else:
                nest_state = None

        else:
            nest_state = None
            self.get_logger().info('input state not supported!\n')

        return nest_state

    def _main_loop(self):
        state = States.INIT
        while state != States.FINISH:
            state = self.strategy_state(state)
            if state == None:
                break
        self.destroy_node()

    def generate_robot_request(
            self, 
            holding=True,
            cmd_mode=RobotCommand.Request.PTP,
            cmd_type=RobotCommand.Request.POSE_CMD,
            velocity=DEFAULT_VELOCITY,
            acceleration=DEFAULT_ACCELERATION,
            tool=CUE_TOOL,
            base=MY_BASE,
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

    def call_yolo(self, req):
        while not self.strategy_client.wait_for_service(timeout_sec=2.0):
            self.get_logger().info('YOLO service not available, waiting again...')
        future = self.strategy_client.call_async(req)
        if self._wait_for_future_done(future):
            res = future.result()
        else:
            res = None
        return res
    
    def _wait_for_future_done(self, future: Future, timeout=-1):
        time_start = time.time()
        while not future.done():
            time.sleep(0.01)
            if timeout > 0 and time.time() - time_start > timeout:
                self.get_logger().error('Wait for service timeout!')
                return False
        return True
    
    def start_main_loop_thread(self):
        self.main_loop_thread = Thread(target=self._main_loop)
        self.main_loop_thread.daemon = True
        self.main_loop_thread.start()

    def test_request(self):
        key = input('Enter 1 or 0 to send ball location:\n')
        if key == '1':
            oi = 1
        else:
            oi = 0
        self.yolo_req.send_position = oi
        future = self.strategy_client.call_async(self.yolo_req)
        rclpy.spin_until_future_complete(self, future)
        # if self._wait_for_future_done(future):
        #     res = future.result()
        # else:
        #     res = None
       
        return future.result()
    

def main(args=None):
    rclpy.init(args=args)

    strategy = ArmsDealer_2()
    # # test yolo_service
    # response = strategy.test_request()
    # strategy.get_logger().info('ball location:{}\n'.format(response.current_position))

    #actual strategy client
    strategy.start_main_loop_thread()
    rclpy.spin(strategy)
    # strategy.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()