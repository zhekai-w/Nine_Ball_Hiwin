import numpy as np
import yaml

config_file = 'arm.yaml'

with open(config_file, 'r') as file:
    data = yaml.safe_load(file)

hole_0 = np.array(data['pot0'][0:2])
hole_1 = np.array(data['pot3'][0:2])
hole_3 = np.array(data['pot2'][0:2])
hole_4 = np.array(data['pot1'][0:2])
vx = hole_4 - hole_0
unit_vx = vx/np.sqrt(vx[0]**2 + vx[1]**2)
print(vx)
print(unit_vx)
ul = np.sqrt(unit_vx[0]**2 + unit_vx[1]**2)
print(ul)
