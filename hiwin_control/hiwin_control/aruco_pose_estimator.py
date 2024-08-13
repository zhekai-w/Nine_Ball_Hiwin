import cv2
import numpy as np
import configparser
import os

import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import ParameterDescriptor
from geometry_msgs.msg import Point, Twist, Pose, PoseArray
from std_msgs.msg import Int16MultiArray
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge

def quaternion_from_matrix(matrix):
    """Return quaternion from rotation matrix.

    >>> R = rotation_matrix(0.123, (1, 2, 3))
    >>> q = quaternion_from_matrix(R)
    >>> numpy.allclose(q, [0.0164262, 0.0328524, 0.0492786, 0.9981095])
    True

    """
    q = np.empty((4, ), dtype=np.float64)
    M = np.array(matrix, dtype=np.float64, copy=False)[:4, :4]
    t = np.trace(M)
    if t > M[3, 3]:
        q[3] = t
        q[2] = M[1, 0] - M[0, 1]
        q[1] = M[0, 2] - M[2, 0]
        q[0] = M[2, 1] - M[1, 2]
    else:
        i, j, k = 0, 1, 2
        if M[1, 1] > M[0, 0]:
            i, j, k = 1, 2, 0
        if M[2, 2] > M[i, i]:
            i, j, k = 2, 0, 1
        t = M[i, i] - (M[j, j] + M[k, k]) + M[3, 3]
        q[i] = t
        q[j] = M[i, j] + M[j, i]
        q[k] = M[k, i] + M[i, k]
        q[3] = M[k, j] - M[j, k]
    q *= 0.5 / np.sqrt(t * M[3, 3])
    return q

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

class ArUcoMarkerEstimator(Node):
    def __init__(self):
        super().__init__("aruco_marker_estimator")
        # Subscribe to RealSense camera topic
        self.rs_sub = self.create_subscribption(Image, 'camera/camera/color/image_raw', self.rs_callback, 1)

        # Publish ArUco pose and ID
        self.aruco_pub = self.create_publisher(PoseArray, 'aruco/poses', 1)
        self.maker_pub = self.create_publisher(Int16MultiArray, 'aruco/marker_ids', 1)

        # Camera use var
        self.rgb_image = None
        self.cv_bridge = CvBridge

        # Define aruco dictionary and size
        self.aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)
        self.parameters = cv2.aruco.DetectorParameters_create()
        self.marker_size = 0.05 # in meter

        # Load camera matrix and distortion coefficient
        current_dir = os.getcwd()
        filepath = current_dir + '/camera_calibration.ini'
        self.camera_matrix, self.dist_coeffs = read_camera_config(filepath)

    def rs_callback(self, msg):
        self.pose = Pose()
        self.pose_array = PoseArray()
        self.marker_IDs = Int16MultiArray()

        self.rgb_image = self.cv_bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        # detect marker and estimate pose
        pose_estimator()
        self.aruco_pub.publish(self.pose_array)
        self.maker_pub.publish(self.marker_IDs)

    def pose_estimator(self):
        rvecs = None
        tvecs = None
        color_frame = self.rgb_image
        gray = cv2.cvtColor(color_frame, cv2.COLOR_BGR2GRAY)
        corners, ids, rejected = cv2.aruco.detectMarker(gray,
                                                        self.aruco_dict,
                                                        parameters=self.parameters)
        if ids is not None:
            cv2.aruco.drawDetectedMarkers(color_frame, corners, ids)
            rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(corners,
                                                                self.marker_size,
                                                                self.camera_matrix,
                                                                self.dist_coeffs)
            for i, marker_id in enumerate(ids)
                self.pose.position = tvecs[i][0]
                # pose.position.x = tvecs[i][0][0]
                # pose.position.y = tvecs[i][0][1]
                # pose.position.z = tvecs[i][0][2]

                rot_matrix, _ = cv2.Rodrigues(rvecs[i])
                quat = quaternion_from_matrix(rot_matrix)
                self.pose.orientation = quat
                # pose.orientation.x = quat[0]
                # pose.orientation.y = quat[1]
                # pose.orientation.z = quat[2]
                # pose.orientation.w = quat[3]

                self.pose_array.pose.append(self.pose)
                self.marker_IDs.append(marker_id)

                cv2.aruco.drawAxis(color_frame, self.camera_matrix, self.dist_coeffs, rvecs[i], tvecs[i], 0.1)

                print(f"Marker {ids[i][0]} position: X={tvecs[0][0][0]:.2f}, Y={tvecs[0][0][1]:.2f}, Z={tvecs[0][0][2]:.2f}")

        cv2.imshow('Detected ArUco markers', color_frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
