import rclpy
from rclpy.node import Node
from detect_interface.msg import DetectionResults, BoundingBox
from std_msgs.msg import Float64MultiArray, MultiArrayLayout, MultiArrayDimension, String
import numpy as np 

class BoxPublisher(Node):
    def __init__(self):
        super().__init__('box_publisher')
        self.subscription = self.create_subscription(DetectionResults, '/detect/objs', self.detection_callback, 10)
        self.publisher_coords = self.create_publisher(Float64MultiArray, 'center_data_coords', 10)
        self.publisher_labels = self.create_publisher(String, 'center_data_labels', 10)
        self.label_order = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'white']  # 定義標籤排序
        self.get_logger().info('BoxPublisher has been started and is subscribing and publishing.')
        # self.max = 0
        # self.find_max_data = []

    def detection_callback(self, msg):
        self.get_logger().info('Received detection results')

        # 初始化 Float64MultiArray
        center_array = Float64MultiArray()
        center_array.layout.dim.append(MultiArrayDimension(label='centers', size=2, stride=2))
        center_array.layout.data_offset = 0

        # 使用字典收集每個標籤的中心點，以保持排序
        detected_objects = {label: [] for label in self.label_order}


        # 收集數據
        for label, bbox, confidance in zip(msg.labels, msg.bounding_boxes, msg.scores):
            if label in detected_objects:
                center_x = (bbox.xmin + bbox.xmax) / 2
                center_y = (bbox.ymin + bbox.ymax) / 2
                detected_objects[label].append([center_x, center_y, confidance])

        # self.find_max_data.append(detected_objects)
        # self.max += 1

        '''
        try solving yolo detect flashing problem
        '''

        # if self.max == 3:
            # print("find in this 5:", self.find_max_data)
        # detected_objects = max(self.find_max_data, key=len)

        # Relabel the lesser confidence '1' object as '9'
        if len(detected_objects['1']) == 2:
            detected_objects['9'] = detected_objects['1'].copy()  # Create a copy of the list
            del detected_objects['1'][0]

            remove_for_9 = detected_objects['9'][1]  # Get the second element from the copied list
            detected_objects['9'].remove(remove_for_9)  # Remove the element from the copied list

        # If there is only '1' or '9' object and it's labeled as '1', relabel it as '9'
        elif len(detected_objects['9']) == 0 and len(detected_objects['1']) == 1:
            detected_objects['9'] = detected_objects['1']
            detected_objects['1'] = []


        print("all ball:", detected_objects)

        # Publish labels as a string, need to use eval to convert back to list
        label_msg = String()
        label_msg.data = ' '.join(label for label in self.label_order if detected_objects[label])
        labels = label_msg.data.split()
        label_msg.data = str(labels)
        self.publisher_labels.publish(label_msg)
        self.get_logger().info(f'Published labels: {label_msg.data}')
        label_ting = eval(label_msg.data)
        # print("label ting:", label_ting[0])

        print("\n----------------\n")


        # 按標籤順序整理並發布中心點數據
        for label in self.label_order:
            for center in detected_objects.get(label):
                # print("label:", label)
                # print("center:", center)
                center_array.data.extend(center[:2])
                # label_msg = String()
                # label_msg.data = label
                # self.publisher_labels.publish(label_msg)
                self.get_logger().info(f'Label: {label}, Center: ({center[0]:.2f}, {center[1]:.2f}), Confidance: ({center[2]:.2f})')


    
        # 發布中心點數據
        self.publisher_coords.publish(center_array)
        print("Center array:", center_array)
        self.get_logger().info(f'Published center data: {center_array.data}')
        self.max = 0

def main(args=None):
    rclpy.init(args=args)
    node = BoxPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()