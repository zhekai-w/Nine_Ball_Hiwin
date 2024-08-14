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
        # self.get_logger().info(f'Received coordinates: {msg.data}')
        temp_max = 0
        data_flag=0
        if self.max==5:
            max_data = []
            for data in self.all_10_data:
                if len(data) > temp_max:
                    temp_max = len(data)
                    max_data = data
            self.max = 0
            data_flag=1
            self.get_logger().info(f'max_data: {max_data}')

        else:
            self.max+=1
            self.all_10_data.append(msg.data)
        #[0,2,3,6,5,7]
        ballx_set=[]
        bally_set=[]
        if data_flag==1:
            for i in range(len(max_data)):
                if i%2==0:
                    ballx_set.append(max_data[i])
                else:
                    bally_set.append(max_data[i])
            ballcount=int((len(max_data)-2)/2)
            cuex=ballx_set[-1]
            cuey=bally_set[-1]

            temp_array=np.array(table.main(ballx_set, bally_set, ballcount, cuex, cuey))
            temp_array = np.clip(temp_array, -1e308, 1e308) 
            self.return_value.data=temp_array.astype(np.float64)
            # self.return_value.data=np.array(self.return_temp_value)
            self.get_logger().info(f'maxaaa: {self.return_value}')
            
            # 發布擊球點位相關數據
            self.publisher_hitpoint.publish(self.return_value)
            self.get_logger().info('hitpoint_success')

            data_flag=0
def main(args=None):
    rclpy.init(args=args)
    node = BoxSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()