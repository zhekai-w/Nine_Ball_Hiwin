import configparser
import numpy as np
import quaternion  # from numpy-quaternion

# 1. Read the INI
cfg = configparser.ConfigParser()
cfg.read('eye_in_hand_calibration.ini')
sect = cfg['hand_eye_calibration']

# 2. Parse translation
x = float(sect['x'])
y = float(sect['y'])
z = float(sect['z'])

# 3. Parse quaternion (w, x, y, z order for numpy-quaternion)
qx = float(sect['qx'])
qy = float(sect['qy'])
qz = float(sect['qz'])
qw = float(sect['qw'])
q = np.quaternion(qw, qx, qy, qz)

# 4. Build a 4×4 homogeneous transform
T = np.eye(4)
T[:3, 3] = [x, y, z]
T[:3, :3] = quaternion.as_rotation_matrix(q)

print("Pose T:\n", T)
# returns (roll, pitch, yaw) in radians
roll, pitch, yaw = quaternion.as_euler_angles(q)
# to convert to degrees:
rx, ry, rz = np.degrees([roll, pitch, yaw])
print(f"rx={rx:.2f}°, ry={ry:.2f}°, rz={rz:.2f}°")
