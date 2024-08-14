import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray,String
import sys
import center.tableball as table
import center.just_pool_think0524 as table2
import numpy as np
import math
import quaternion as qtn
import center.transformations as transformations
import matplotlib.pyplot as plt


# from . import tableball as table  # Adjust this import based on your file structure
# import pygame as pg

CAM_TO_TABLE = 481
fix_abs_cam = [48.809, 310.996, 383.971, -179.499, -3.45, 89.95]

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

def convert_arm_pose(ball_pose, arm_pose):
    base2tool = np.array(arm_pose)
    base2tool[:3] /= 1000

    # tool to camera quaternion
    tool2cam_quaternion = [-0.0277325088427568, -0.026177641210702426, 0.7034336548574274, 0.7097370867214506]
    tool2cam_trans = [0.12230235996651653, -0.03599119674476696, 0.0681407254283748]

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

tablewidth = 627
tableheight = 304

def yaw_angle(vectorx, vectory):
    vectorlength = math.sqrt((vectorx**2)+(vectory**2))
    rad = math.acos((-1*vectory)/(vectorlength*1))
    theta = rad*180/math.pi
    if vectorx >= 0:
        return theta, rad
    elif vectorx < 0:
        return -theta, -rad

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
        actual_x = []
        actual_y = []

        if self.max == 5:
            max_data = max(self.all_10_data, key=len)
            for i in range(0, len(max_data), 2):
                i_rela_to_cam = pixel_mm_convert(CAM_TO_TABLE, max_data[i:i+2]) 
                actual_ball_pose = convert_arm_pose(i_rela_to_cam, fix_abs_cam)
                actual_x.append(actual_ball_pose[0])
                actual_y.append(actual_ball_pose[1])
            ballcount = len(actual_x) - 1
            cuex, cuey = actual_x[-1], actual_y[-1]
    
            
            # ballx_set = self.ball_pose_buffer[::2]
            # bally_set = self.ball_pose_buffer[1::2]
            # ballcount = len(actual_x) - 1
            # cuex, cuey = actual_x[-1], actual_y[-1]
            # try:

            self.max = 0
            self.all_10_data.clear()

            #table2.main return this [max_non_positive_score, bestvx, bestvy, routeobs, hitcuepointx, hitcuepointy]
            temp_array = np.array(table2.main(actual_x[:-1], actual_y[:-1], ballcount, cuex, cuey))
            print("Computed temp_array:", temp_array)
            # Implement more stringent clamping
            temp_array = temp_array.astype(np.float32)
            # calculate yaw angle
            yaw, _ = yaw_angle(temp_array[1], temp_array[2])

            for j in range(len(actual_x)-1):
                aimpoint = plt.Circle((actual_x[j], actual_y[j]),
                                    16, color="red")
                # plt.text(aimpointx[j],aimpointy[j],j,color='red',fontsize=15)
                plt.gca().add_patch(aimpoint)
            plt.gca().add_patch(plt.Circle((cuex, cuey), 16, color='blue'))
            plt.gca().add_patch(plt.Circle((temp_array[4], temp_array[5]), 3, color='black'))
            plt.quiver(temp_array[4], temp_array[5],-temp_array[1], temp_array[2],color='black',units="xy",angles="xy",scale_units="xy",scale=1, width=2,alpha=0.5)
            plt.title("sim pool table") 
            plt.axis([0, tablewidth, 0, tableheight])
            # plt.autoscale(enable=True, axis='both', tight=None) 
            plt.axis("equal")
            plt.show(block=False)
            # input("Enter to continue...")
            plt.pause(0.01)
            plt.cla()

            print("raw data", temp_array)
            self.return_value.data = [np.clip(x, -1e308, 1e308) for x in temp_array]
            print("Clamped and converted array:", self.return_value.data)

            self.publisher_hitpoint.publish(self.return_value)
            self.get_logger().info('Hitpoint data successfully published.')
            
            



def main(args=None):
    rclpy.init(args=args)
    node = BoxSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()