import cv2
import rclpy
import numpy as np
import pyrealsense2 as rs
from rclpy.node import Node
from detect_interface.msg import DetectionResults, BoundingBox
from std_msgs.msg import String  # 使用標準消息類型，或根據需要自定義

class BoxPublisher(Node):
    def __init__(self):
        super().__init__('box_publisher')
        self.subscription = self.create_subscription(DetectionResults,'/detect/objs',self.detection_callback,10)
        self.publisher = self.create_publisher(String, 'center_data', 10)  # 增加一個發布者
        self.get_logger().info('BoxPublisher has been started and is subscribing and publishing.')

    def detection_callback(self, msg):
        #記錄一條信息，表收到檢測結果。
        self.get_logger().info('Received detection results')
        #使用for循環:每個檢測到的物體。
        for label, score, bbox in zip(msg.labels, msg.scores, msg.bounding_boxes):
            # 計算 BoundingBox 的中心點
            center_x = (bbox.xmin + bbox.xmax) / 2
            center_y = (bbox.ymin + bbox.ymax) / 2
            #僅發布中心點
            center_data = f'Center of {label}: ({center_x:.2f}, {center_y:.2f})'
            self.publisher.publish(String(data=center_data))  # 發布處理後的數據
            self.get_logger().info(f'Published: {center_data}')

        if cv2.waitKey(1) & 0xFF == ord('q'):
             return
        
def main(args=None):
    rclpy.init(args=args)
    node = BoxPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    # # Stop streaming
    # pipeline.stop()

if __name__ == '__main__':
    main()
