import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import pyrealsense2 as rs
import cv2
import numpy as np
import os
import configparser

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

def undistort_image(image, camera_matrix, dist_coeffs):
    """
    Undistort an image using camera calibration parameters
    param image: Input image
    param camera_matrix: Camera matrix
    param dist_coeffs: Distortion ceofficients
    return: Undistorted image
    """
    h, w = image.shape[:2]

    new_camera_matrix,  roi = cv2.getOptimalNewCameraMatrix(camera_matrix, dist_coeffs, (w, h), 1, (w, h))
    undistorted = cv2.undistort(image, camera_matrix, dist_coeffs, None, new_camera_matrix)
    return undistorted

class ImagePublisher(Node):
    def __init__(self):
        super().__init__('image_publisher')  # Node name

        # Create the publisher
        self.publisher_ = self.create_publisher(Image, '/camera/camera/color/image_raw', 10)
        timer_period = 0.03  # Publish at 10Hz
        self.timer = self.create_timer(timer_period, self.timer_callback)

        # Initialize the RealSense pipeline
        self.pipeline = rs.pipeline()
        config = rs.config()
        config.enable_stream(rs.stream.color, 1920, 1080, rs.format.bgr8, 30)

        # Get the selected sensor and modify its exposure settings
        # sensor = config.resolve(self.pipeline).get_device().query_sensors()[1]
        # sensor.set_option(rs.option.exposure, 60)  # Set the exposure value (in microseconds)

        # Start streaming
        self.pipeline.start(config)

        # Set white balance after pipeline starts (as before)
        color_sensor = self.pipeline.get_active_profile().get_device().query_sensors()[1]
        color_sensor.set_option(rs.option.enable_auto_white_balance, False)
        color_sensor.set_option(rs.option.white_balance, 6100)

        # Initialize CvBridge
        self.bridge = CvBridge()

        # Read camera_calibration.ini
        current_dir = os.getcwd()
        print("Current dir", current_dir)
        filepath = current_dir + '/src/hiwin_control/hiwin_control/camera_calibration.ini'
        print("filepath", filepath)
        self.camera_matrix, self.dist_coeffs = read_camera_config(filepath)

    def timer_callback(self):
        # Get the frames
        frames = self.pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()

        # Check if a frame is available
        if not color_frame:
            return

        # Convert to numpy array and resize
        color_image = np.asanyarray(color_frame.get_data())

        # Undistort image
        undistort = undistort_image(color_image, self.camera_matrix, self.dist_coeffs)

        # Create and publish the image message
        msg = self.bridge.cv2_to_imgmsg(undistort, encoding="bgr8")
        msg.header.stamp = self.get_clock().now().to_msg()
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    image_publisher = ImagePublisher()
    rclpy.spin(image_publisher)
    image_publisher.destroy_node()  # Clean up before exiting
    rclpy.shutdown()

if __name__ == '__main__':
    main()
