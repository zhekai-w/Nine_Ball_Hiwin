# import numpy as np
# import configparser
# import os
# import cv2

# current_dir = os.getcwd()
# print(current_dir)

# config = configparser.ConfigParser()

# filepath = current_dir + '/camera_calibration.ini'

# def read_camera_config(filepath):
#     camera_matrix = None
#     dist_coeffs = None
#     config = configparser.ConfigParser()
#     config.read(filepath)
#     try:
#         # Read camera matrix
#         cm = config['Intrinsic']
#         camera_matrix = np.array([
#             [float(cm['0_0']), float(cm['0_1']), float(cm['0_2'])],
#             [float(cm['1_0']), float(cm['1_1']), float(cm['1_2'])],
#             [0, 0, 1]
#         ])

#         # Read distortion coefficient
#         dc = config['Distortion']
#         dist_coeffs = np.array(
#             [float(dc['k1']), float(dc['k2']), float(dc['t1']), float(dc['t2']), float(dc['k3'])]
#         )
#     except configparser.Error as e:
#         print(e)
#     return camera_matrix, dist_coeffs

# camera_matrix, dist_coeffs = read_camera_config(filepath)
# print(camera_matrix)
# print(dist_coeffs)

for i in range(0,8,2):
    print(i)
