# Modbus Library for Hiwin Robot
This Modbus Library include libmodbus and ROS2 package, which let controlling Hiwin Robot more easier for beginner, also can exten function with ROS2.
Also include Hiwin pool ball competition packages

## Acknowledgment
The submodule package is from [libmodus](https://github.com/stephane/libmodbus.git) and [hiwin_libmodbus](https://github.com/tku-iarc/Hiwin_libmodbus.git).

## Requirements 
This package requires a system setup with ROS2. It is recommended to use **Ubuntu 22.04 with ROS2 Humble**.

<!-- camera SDK and ROS package is needed. Here we use [Linux Distribution](https://github.com/IntelRealSense/librealsense/blob/master/doc/distribution_linux.md#installing-the-packages) and [Realsense-ros](https://github.com/IntelRealSense/realsense-ros/tree/ros1-legacy) -->

To make sure that program isn't affected by python version, it is highly recommended to use a docker, 
we have build a environment that all Requirement for this package is build, 
See the [ubuntu-docker](https://github.com/errrr0501/ubuntu22.04_ros2.git) on information how to set this up.

# Getting start
## Building

```bash

# go to your workspace/src
cd ~<your_workspace>/src
# clone this repository with libmodus
git clone --recurse-submodules https://github.com/zhekai-w/Nine_Ball_Hiwin.git

sudo apt update -qq
rosdep update
rosdep install --from-paths src --ignore-src -y

# build the workspace
cd ~<your_workspace>
colcon build --cmake-args -DCMAKE_BUILD_TYPE=Release

# activate the workspace (ie: source it)
source install/setup.bash
```

## Run Test Script
Note:In order to connect to real Hiwin Robot, please change your **Network** setting after plugin LAN.
Select **Wired->setting->IPv4**, choose **Manual** change **Netmasks** to `255.255.255.0`, 
change **Address** to `192.168.0.x`, except `192.168.0.1`, which is default robot ip address.

```bash

# connect to Hiwin Robot
ros2 run hiwin_libmodbus hiwinlibmodbus_server

# run yolov4 service server
ros2 run py_pubsub yolo_service

# run pool strategy service client
ros2 run py_pubsub strategy_client

# or run example strategy
python3 src/Hiwin_libmodbus/hiwin_example/hiwin_example/strategy_example.py
```

## Run Nine Ball Script

```bash

# Stream video for YOLO detection
ros2 run hiwin_control stream_rs
# Or
ros2 launch realsense2_camera rs_launch.py rgb_camera.color_profile:=1920x1080x30

# Launch YOLOv7 object detection
ros2 launch yolov7_obj_detect object_detection_launch.py 

# Publish YOLOv7 detected bounding boxes
ros2 run center publisher_dection_boxes

# Connect to Hiwin Robot
ros2 run hiwin_libmodbus hiwinlibmodbus_server

# Run Nine ball strategy/controller
ros2 run hiwin_control arm_controller
```

