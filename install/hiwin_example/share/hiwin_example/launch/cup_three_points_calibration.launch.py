import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    hiwin_config = os.path.join(
        get_package_share_directory('hiwin_example'),
        'config',
        'cup_cali_pose.yaml'
        )
    
    cam_config = os.path.join(
        get_package_share_directory('hiwin_example'),
        'config',
        'cup_cam.yaml'
        )  
    print(cam_config)
    rviz_config = os.path.join(get_package_share_directory(
        'hiwin_example'), "launch", "cam.rviz")

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([get_package_share_directory('realsense2_camera'), 
                                           '/launch/rs_launch.py']),
            launch_arguments={'rgb_camera.profile': '1920x1080x30'}.items(),
        ),

        Node(
            package="rviz2",
            executable="rviz2",
            name="rviz2",
            arguments=["-d", rviz_config],
            output="screen",
        ),

        Node(
        package = 'ros2_aruco',
        name = 'three_points_cali_aruco',
        executable = 'hiwin_cali',
        parameters = [cam_config],
        output="screen",
    ),
    ])
    
#ros2 run hiwin_libmodbus hiwinlibmodbus_server
#ros2 run hiwin_example three_points_calibration_example --ros-args --params-file ~/workspace/src/Hiwin_libmodbus/hiwin_example/config/cup_cali_pose.yaml