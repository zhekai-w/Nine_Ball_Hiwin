import numpy as np
import yaml
import configparser

# '''
# Base on robot arm coordinate
# '''
# r = 16

# config_file = 'arm.yaml'
# with open(config_file, 'r') as file:
#     data = yaml.safe_load(file)

# print(data['armpos'])
# print(data['zoff'])

TOOL_TO_CAM = [0.,0.,0.]

# Read tool to camera vector
config = configparser.ConfigParser()
config.read('eye_in_hand_calibration.ini')
tm = config['hand_eye_calibration']
TOOL_TO_CAM[0] = float(tm['y'])*1000
TOOL_TO_CAM[1] = float(tm['x'])*1000
TOOL_TO_CAM[2] = -float(tm['z'])*1000
print(TOOL_TO_CAM)
