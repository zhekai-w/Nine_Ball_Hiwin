import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray,String
import sys
import center.tableball as table
import numpy as np


# from . import tableball as table  # Adjust this import based on your file structure
# import pygame as pg

class BoxSubscriber(Node):
    def __init__(self):
        super().__init__('pygame_node')
        self.subscription = self.create_subscription(Float64MultiArray, 'center_data_coords', self.strategy_callback, 10)
        self.publisher_hitpoint = self.create_publisher(Float64MultiArray, 'strategy_hitpoint', 10)
        self.get_logger().info('BoxSubscriber has been started and is subscribing to data.')
        self.max=0
        self.all_10_data = []
        self.return_value = Float64MultiArray()
    def strategy_callback(self, msg):
        self.all_10_data.append(msg.data)
        self.max += 1

        if self.max == 5:
            max_data = max(self.all_10_data, key=len)
            ballx_set = max_data[::2]
            bally_set = max_data[1::2]
            ballcount = len(ballx_set) - 1

            cuex, cuey = ballx_set[-1], bally_set[-1]
            try:
                temp_array = np.array(table.main(ballx_set[:-1], bally_set[:-1], ballcount, cuex, cuey))
                print("Computed temp_array:", temp_array)

                # Implement more stringent clamping
                # safe_range = 1e3  # Example range, adjust based on expected value range
                # temp_array = np.clip(temp_array, -safe_range, safe_range)
                temp_array = temp_array.astype(np.float64)
                for array in temp_array:
                    print(type(array))
                # print(type(temp_array[0]))
                self.return_value.data = temp_array
                print("Clamped and converted array:", self.return_value.data)

                self.publisher_hitpoint.publish(self.return_value)
                self.get_logger().info('Hitpoint data successfully published.')
            except Exception as e:
                self.get_logger().error(f'Error during processing or publishing: {e}')
            finally:
                self.max = 0
                self.all_10_data.clear()



def main(args=None):
    rclpy.init(args=args)
    node = BoxSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()