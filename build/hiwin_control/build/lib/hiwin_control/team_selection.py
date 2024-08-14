import random
import math
import sys
import time 
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point, LineString
#inital condition
actual_width = 62.7
actual_height = 30.4
#virtual height width
# width = 627
width  =627
height = 304
radius = int(1.6 / actual_height * height)
hole_radius = int(width / actual_width * 2)
# Table coordinates
x1 = -311.196
y1 =  612.0
hole_positions = [(x1, y1), (x1 + width // 2, y1), (x1 + width, y1),
                  (x1, y1 + height), (x1 + width // 2, y1 + height), (x1 + width, y1 + height)]

vir_hole_positions = [(x1 + radius, y1 + radius), (x1 + width /2, y1 + radius), (x1 + width - radius, y1 + radius),
                      (x1 + radius, y1 + height - radius), (x1 + width / 2, y1 + height - radius), (x1 + width - radius, y1 + height - radius)]
actualwidth =62.7
actualheight=30.4
width=627
height=304
radius=int(1.6/actualheight*height)
holeradius=int(width/actualwidth*2)
holex=[x1,x1+width/2,x1+width,x1,x1+width/2,x1+width]
holey=[y1,y1,y1,y1+height,y1+height,y1+height]
virholex=[x1+radius,x1+width/2,x1+width-radius,x1+radius,x1+width/2,x1+width-radius]
virholey=[y1+radius,y1+radius,y1+radius,y1+height-radius,y1+height-radius,y1+height-radius]

tablewidth = 627
tableheight = 304

TOP_LEFT = [-311.196, 612.0]

holex =     [TOP_LEFT[0],            TOP_LEFT[0],            TOP_LEFT[0]+tablewidth/2,
             TOP_LEFT[0]+tablewidth, TOP_LEFT[0]+tablewidth, TOP_LEFT[0]+tablewidth/2]
holey =     [TOP_LEFT[1],             TOP_LEFT[1]-tableheight, TOP_LEFT[1]-tableheight,
             TOP_LEFT[1]-tableheight, TOP_LEFT[1],             TOP_LEFT[1]]


def distance_and_vector(point1,point2):
    n1x,n1y=point1
    n2x,n2y=point2
    dx = n1x - n2x
    dy = n1y - n2y
    dist = math.sqrt(dx ** 2 + dy ** 2)
    return round(dist, 2), (dx, dy)

def calculate_aim_point(obj_point,target_point, ball_diameter):
    # 计算从球到目标的向量
    ball_x,ball_y=obj_point
    target_x,target_y=target_point
    vector_x = target_x - ball_x
    vector_y = target_y - ball_y
    
    # 计算向量的长度
    length = math.sqrt(vector_x ** 2 + vector_y ** 2)
    
    # 计算单位向量（方向向量）
    unit_vector_x = vector_x / length
    unit_vector_y = vector_y / length
    
    # 计算一个球直径的距离
    aim_distance = 2*ball_diameter
    
    # 计算在球的后方一个直径的点
    aim_point_x = ball_x - unit_vector_x * aim_distance
    aim_point_y = ball_y - unit_vector_y * aim_distance
    
    return (aim_point_x, aim_point_y)
        
# def screen(hit_point,target_point):
#     plt.title('Basic Plot in Matplotlib')
#     plt.xlabel('X Axis Label')
#     plt.ylabel('Y Axis Label')
#     plt.grid()
#     plt.plot([holex[0],holex[2]],[holey[0],holey[2]],[holex[2],holex[5]],[holey[2],holey[5]],
#             [holex[5],holex[3]],[holey[5],holey[3]],[holex[3],holex[0]],[holey[3],holey[0]],color='black')
#     # for i in range(linecount):
#     #    plt.plot((lines[i],lines[i+2]),(lines[i+1],lines[i+3]), linestyle = '-') 
#     plt.plot(cue[0], cue[1],marker='o',ms=radius,color='red')
#     plt.plot(hit_point[0],hit_point[1],marker='o',ms=radius,color='red')
#     for i in range(6):
#         plt.plot(hole_positions[i][0],hole_positions[i][1],marker = 'o',ms=holeradius,color='black')
#         plt.plot(vir_hole_positions[i][0],vir_hole_positions[i][1],marker = 'o',ms=holeradius,color='black')
#         # plt.plot(obj_hitpoints[i],marker = 'o',ms=3,color='green')
#         # plt.plot(nine_hitpoints[i],marker = 'o',ms=3,color='green')
#     plt.show()
        
        
def main(cuex,cuey):
    cue=(cuex,cuey)
    target_point=[(holex[3]+holex[4])/2, (holey[3]+holey[4])/2]
    print(target_point)
    hit_point=calculate_aim_point(cue,target_point,radius)
    cue_target_dis,cue_target_vector=distance_and_vector(cue,target_point)
    score=4500
    # screen(hit_point,target_point)
    return score,cue_target_vector[0], cue_target_vector[1], 0, hit_point[0], hit_point[1]

result = main(231, 312)
print(result)


    