import time
import numpy as np
import configparser
import quaternion as qtn
import hiwin_control.transformations as transformations
from enum import Enum
from threading import Thread

import rclpy
from rclpy import Node
from rclpy.task import Future
from geometry_msgs.msg import Point, Twist, Pose, PoseArray
from std_msgs.msg import Int16MultiArray
from hiwin_interfaces.srv import RobotCommand

DEFAULT_VELOCITY = 20
DEFAULT_ACCELERATION = 20

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

def read_camera_config(filepath):
    camera_matrix = None
    dist_coeffs = None
    config = configparser.ConfigParser()
    config.read(filepath)
    try:
        # Read camera matrix
        cm = config['Intrinsic']
        camera_matrix = np.array([
            [float(cm['0_0']), float(cm['0_1']), float(cm['0_2'])],
            [float(cm['1_0']), float(cm['1_1']), float(cm['1_2'])],
            [0, 0, 1]
        ])

        # Read distortion coefficient
        dc = config['Distortion']
        dist_coeffs = np.array(
            [float(dc['k1']), float(dc['k2']), float(dc['t1']), float(dc['t2']), float(dc['k3'])]
        )
    except configparser.Error as e:
        print(e)
    return camera_matrix, dist_coeffs

class ArUcoArmController(Node):
    def __init__(self):
        super().__init__('aruco_arm_controller')
        self.hiwin_client = self.create_client(RobotCommand, 'hiwinmodbus_service')
        self.aruco_sub = self.create_subscriber(PoseArray, 'aruco/poses')
        self.marker_sub = self.create_subscriber(Int16MultiArray, 'aruco/marker_ids')
        self.aruco_poses = None
        self.marker_ids = None

    def aruco_callback(self, msg):
        self.aruco_poses = PoseArray()
        self.aruco_poses = msg

    def marker_sub(self, msg):
        self.marker_ids = Int16MultiArray()
        self.marker_ids = msg
        print("ArUco Marker IDs:", self.marker_ids)

    def state_machine(self, state:States) -> States:
        if state == States.INIT:
            self.get_logger().info('INIT')
            nest_state = States.MOVE_TO_PHOTO_POSE

        elif state == States.MOVE_TO_PHOTO_POSE:
            self.get_logger().info('MOVING TO PHOTO POSE')
            pose = Pose()


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

    def start_calibration_thread(self):
        self.main_loop_thread = Thread(target=self._main_loop)
        self.main_loop_thread.daemon = True
        self.main_loop_thread.start()



def main(args=None):
    rclpy.init(args=args)

    stratery = ArUcoArmController()
    stratery.start_calibration_thread()

    rclpy.spin(stratery)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
