import random
import math
import sys
import time 
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point, LineString
import yaml

#inital condition
CONFIG_FILE = 'arm.yaml'
#ball radius
radius = 16
width = 627
height = 304
# transform image coordinate system to robot coordinate system
# def transform(pos):
#     Mint_inv = np.linalg.inv(Mint)
#     Mext_inv = np.linalg.inv(Mext)
#     Mext_inv = Mext_inv[:-1,:]      # matrix 3x4
#     uv = np.array([*pos, 1])
#     camcoor = Mint_inv.dot(uv)
#     xc, yc, zc = camcoor
#     return  Mext_inv.dot(np.r_[camcoor, 1])

def transform(pos):
    Mint_inv = np.linalg.inv(Mint)
    Mext_inv = np.linalg.inv(Mext)
    Mext_inv = Mext_inv[:-1,:]      # matrix 3x4
    uv = np.array([*pos, 1])
    camcoor = Mint_inv.dot(uv)
    xc, yc, zc = camcoor
    return  Mext_inv.dot(np.r_[camcoor, 1])

def load_yaml():
    with open(CONFIG_FILE, 'r') as file:
        config = yaml.safe_load(file)
    return config

conf = load_yaml()
Mext = conf['Mext']
Mint = conf['Mint']

top_left = transform(conf['img_pot0'])
top_right = transform(conf['img_pot1'])
button_right = transform(conf['img_pot2'])
button_left = transform(conf['img_pot3'])


config_file = '/home/jimmy/Desktop/ws/src/Nine_Ball_Hiwin/hiwin_control/hiwin_control/arm.yaml'
with open(config_file, 'r') as file:
    data = yaml.safe_load(file)

hole_0 = np.array(data['pot0'][0:2])
hole_1 = np.array(data['pot3'][0:2])
hole_3 = np.array(data['pot2'][0:2])
hole_4 = np.array(data['pot1'][0:2])
vx = hole_4 - hole_0
vx_lengh = np.sqrt(vx[0]**2 + vx[1]**2)
unit_vx = vx/vx_lengh
vy = hole_0 - hole_1
vy_lengh = np.sqrt(vy[0]**2 + vy[1]**2)
unit_vy = vy/vy_lengh
hole_2 = hole_1 + unit_vx*(vx_lengh/2)
hole_5 = hole_0 +unit_vx*(vx_lengh/2)


aimpoint_0 = hole_0 + radius*(unit_vx-unit_vy)
aimpoint_1 = hole_1 + radius*(unit_vx+unit_vy)
aimpoint_2 = hole_2 + radius*(unit_vy)
aimpoint_3 = hole_3 + radius*(-unit_vx+unit_vy)
aimpoint_4 = hole_4 + radius*(-unit_vx-unit_vy)
aimpoint_5 = hole_5 + radius*(-unit_vy)
vir_hole_positions=[(aimpoint_0[0],aimpoint_0[1]),(aimpoint_1[0],aimpoint_1[1]),(aimpoint_2[0],aimpoint_2[1]),(aimpoint_3[0],aimpoint_3[1]),(aimpoint_4[0],aimpoint_4[1]),(aimpoint_5[0],aimpoint_5[1])]
x1,y1=hole_0[0],hole_0[1]
holex = [hole_0[0], hole_1[0], hole_2[0], hole_3[0], hole_4[0], hole_5[0]]
holey = [hole_0[1], hole_1[1], hole_2[1], hole_3[1], hole_4[1], hole_5[1]]
aimpointx = [aimpoint_0[0], aimpoint_1[0], aimpoint_2[0], aimpoint_3[0], aimpoint_4[0], aimpoint_5[0]]
aimpointy = [aimpoint_0[1], aimpoint_1[1], aimpoint_2[1], aimpoint_3[1], aimpoint_4[1], aimpoint_5[1]]


TOP_LEFT = hole_0
def distance_and_vector(point1,point2):
    n1x,n1y=point1
    n2x,n2y=point2
    dx = n1x - n2x
    dy = n1y - n2y
    dist = math.sqrt(dx ** 2 + dy ** 2)
    return round(dist, 2), (-dx, -dy)

def point_to_vector(n1x, n1y, vector_x, vector_y, dot_x, dot_y):
    dist_to_vector = math.sqrt(vector_x ** 2 + vector_y ** 2)
    ball_to_ball_x = dot_x - n1x
    ball_to_ball_y = dot_y - n1y
    dot_product = vector_x * ball_to_ball_x + vector_y * ball_to_ball_y
    if dot_product >= 0:
        shadow_length = dot_product / dist_to_vector
        ratio = shadow_length / dist_to_vector
        shadow_x = n1x + vector_x * ratio
        shadow_y = n1y + vector_y * ratio
        normal_length = distance_and_vector(dot_x, dot_y, shadow_x, shadow_y)[0]
        return normal_length
    else:
        return -1
    
# Generate random balls
def is_overlapping(x, y,cuex,cuey,existing_balls, radius):
    for bx, by in existing_balls:
        if math.sqrt((x - bx) ** 2 + (y - by) ** 2) < 2 * radius and math.sqrt((x-cuex)**2+(y-cuey)**2)<2*radius:
            return True
    return False

def generate_balls(ballcount, radius):
    cuex = random.randint(int(x1 + radius), int(x1 + width - radius))
    cuey = random.randint( int(y1 - height + radius),int(y1 - radius))
    ball_positions = []

    while len(ball_positions) <= ballcount:
        x = random.randint(int(x1 + radius), int(x1 + width - radius))
        y = random.randint(int(y1 - height + radius),int(y1 - radius), )
        # if not is_overlapping(x, y,cuex,cuey, ball_positions, radius):
        ball_positions.append((x, y))

    ballx_set = [pos[0] for pos in ball_positions]
    bally_set = [pos[1] for pos in ball_positions]

    return cuex, cuey, ballx_set, bally_set, ballcount
def calculate_aim_point(target_point,obj_point,distance):
    # 计算从球到目标的向量
    ball_diameter=distance
    ball_x,ball_y=target_point
    target_x,target_y=obj_point
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

def find_min_negative_integer_in_nested_list(lst):
    min_negative = None 
    min_position1 = None
    min_position2 = None

    for i, sublist in enumerate(lst):
        for j, value in enumerate(sublist):
            if isinstance(value, (int, float)) and value < 0:
                if min_negative is None or value > min_negative:
                    min_negative = value
                    min_position1, min_position2 = i, j

    return min_negative, min_position1, min_position2   

def check_obstacle_ball(obs_ball,obj_point, target_point,target_ball,obs_count,temp1,ballcount):
    maskwidth = 1.7*radius
    n1x, n1y = target_point
    n2x, n2y = obj_point
    vectorx = n1x - n2x
    vectory = n1y - n2y
    vectorlength = math.sqrt(abs(vectorx) ** 2 + abs(vectory) ** 2)
    unit_vector = np.array([vectorx / vectorlength, vectory / vectorlength])
    vector = np.array([vectorx + unit_vector[0] * radius, vectory + unit_vector[1] * radius])
    normal_unit_vector = np.array([unit_vector[1], -unit_vector[0]])
    ball = np.array([obj_point[0], obj_point[1]])
    first_poly = ball - normal_unit_vector * maskwidth
    second_poly = ball + normal_unit_vector * maskwidth
    third_poly = second_poly + vector
    fourth_poly = first_poly + vector
    ploy = [first_poly, second_poly, third_poly, fourth_poly]

    polygon = Polygon(ploy)
    obs_ball_position=[]
    for i in range(ballcount):
        if target_ball==obs_ball[i] or obj_point==obs_ball[i]:
            continue
        shapely_objectballs = Point(obs_ball[i])
        if polygon.contains(shapely_objectballs):
            obs_count =obs_count+1
            obs_ball_position.append(obs_ball[i])
    return obs_count, obs_ball_position

def vector_angle(point1,point2,point3):
    n1x, n1y = point1
    n2x, n2y = point2
    n3x, n3y = point3
    vx1, vy1 = n2x - n1x, n2y - n1y
    vx2, vy2 = n3x - n2x, n3y - n2y
    dotproduct = vx1 * vx2 + vy1 * vy2
    magnitude1 = math.sqrt(vx1 ** 2 + vy1 ** 2)
    magnitude2 = math.sqrt(vx2 ** 2 + vy2 ** 2)
    cos = dotproduct / (magnitude1 * magnitude2)
    cos = max(-1, min(1, cos))
    rad = math.acos(cos)
    deg = math.degrees(rad)
    if deg<=110:
        deg=-deg
    return deg

def cal_score(distance1,distance2, cue_obj_obs,obj_holeobs,pointedge,angle1,angle2,n):
    pointedge=False
    if n==1:
        score = ((angle1 * 22) + (distance1 * -10) + (obj_holeobs * -4000))
    elif n==2:
        score = (((angle1 * 22)/2) +((angle2*22)/2) +(distance1 * -10) + (obj_holeobs * -4000))
    elif n==3:
        score=(((angle1 * 22)/2) +((distance1+distance2) * -10) + (obj_holeobs * -4000))
        if distance2>=500:
            score=abs(score)
    if angle1>=0 or angle2>=0 or cue_obj_obs!=0 or pointedge== True :
        score=abs(score)
    return score


def mirror_point(slope, wall_side, point):
    x, y = point
    if slope == 'inf':  # Vertical wall
        return (2 * wall_side - x, y)
    elif slope == 0:  # Horizontal wall
        return (x, 2 * wall_side - y)
    # Add other slopes if necessary
    return (x, y)

def segment_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    # 計算每個線段的斜率和截距
    denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    # if denominator == 0:
    #     return None  # 兩線段平行或共線，無交點

    # 計算交點
    px = ((x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4)) / denominator
    py = ((x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4)) / denominator

    return (px,py)

# def kiss_nine_ball(cuex,cuey,objx,objy,ninex,niney,):
#the final data need to publish

    
def screen2(ballcount,routenumber,cue,obj,nine,ball_position):
        
    ballx_set=[]
    bally_set=[]
    for i in range(ballcount):
        ballx_set.append(ball_position[i][0])
        bally_set.append(ball_position[i][1])
    plt.title('Basic Plot in Matplotlib')
    plt.xlabel('X Axis Label')
    plt.ylabel('Y Axis Label')
   
    plt.plot([holex[0],holex[4]],[holey[0],holey[4]],[holex[4],holex[3]],[holey[4],holey[3]],[holex[3],holex[1]],[holey[3],holey[1]],[holex[1],holex[0]],[holey[1],holey[0]],color='black')
    plt.gca().add_patch(plt.Circle((obj[0], obj[1]), radius, color='yellow'))
    plt.gca().add_patch(plt.Circle((cue[0], cue[1]), radius, color='red'))
    plt.gca().add_patch(plt.Circle((nine[0], nine[1]), radius, color='pink'))
    # plt.gca().add_patch(plt.Circle((aimpointx[0], left_reflect_point_y[i]), 3, color='red'))
    
    for i in range(1,ballcount-1):
        plt.gca().add_patch(plt.Circle((ballx_set[i],bally_set[i]), radius, color='blue'))
        plt.text(ballx_set[i], bally_set[i], ((ballx_set[i],bally_set[i]),i+1),color='black', fontweight='bold')
    for i in range(6):
        plt.gca().add_patch(plt.Circle((holex[i],holey[i]), radius, color='black'))
        plt.gca().add_patch(plt.Circle((vir_hole_positions[i][0],vir_hole_positions[i][1]), radius, color='black'))
    
    plt.show()
    fig = plt.figure(figsize=(1900 / 200, 1080 / 200))
def find_min_negative_integer_in_nested_list(lst):
    min_negative = None 
    min_position1 = None
    min_position2 = None

    for i, sublist in enumerate(lst):
        for j, value in enumerate(sublist):
            if isinstance(value, (int, float)) and value < 0:
                if min_negative is None or value > min_negative:
                    min_negative = value
                    min_position1, min_position2 = i, j
    return min_negative, min_position1, min_position2  
def target_point_edge(point,judge):
    hitpointx,hitpointy=point
    if hitpointx - radius < x1 or hitpointx + radius > x1 + width or hitpointy + radius > y1 or hitpointy - radius <y1 - height:
        return True
    # for i in range(6):
    #     if point==hole_positions[i][0]-hole_radius or hole_positions[i][0]+hole_radius:
    #         return True
    return False
def final(routenumber,bestscore,best_vector,obstacle,best_cue_hitpoint,cue_obstacle):
    print("---------------------------------------------")
    print("routenumber",routenumber)
    print("Score:", bestscore)
    print("vx, vy:", best_vector)
    print("Obstacles on the route:", obstacle)
    print("x, y:", best_cue_hitpoint)
    print("there have obstacle around cue",cue_obstacle)

# def method1():
class method_choice():
    def __init__(self,ballx_set,bally_set,ballcount,cuex,cuey):
        self.cue=(cuex,cuey)
        self.nine=(ballx_set[-1],bally_set[-1])
        self.obj=(ballx_set[0],bally_set[0])
        self.ballcount=ballcount
        self.positions = [(ballx_set[i], bally_set[i]) for i in range(ballcount)]
        self.boundaries = [
        (x1,y1,x1+width,y1,cuex,cuey),  # top
        (x1,y1-height,x1+width,y1-height,cuex,cuey),  # bottom
        (x1,y1,x1,y1-height,cuex,cuey),  # left
        (x1+width,y1,x1+width,y1-height,cuex,cuey)  # right
        ]
        self.slope=[0,0,'inf','inf']
        self.wall_side = [ y1, y1-height,x1, x1 + width,]
    def edge_detect(self,best_cue_hitpoint):
        hitpointx,hitpointy=best_cue_hitpoint
        if hitpointx - 2.5*radius <= x1 or hitpointx + 2.5*radius >= x1 + width or hitpointy + 2.5*radius >= y1 or hitpointy - 2.5*radius <= y1 - height:
            return True
        obs_range=calculate_aim_point(best_cue_hitpoint,self.cue,radius)
        cue_obstacle=0
        cue_obstacle,_=check_obstacle_ball(self.positions,self.cue,obs_range,self.cue,cue_obstacle,1,self.ballcount)
        if cue_obstacle==0:
            return False
        return True
    def main(self):
        hitball_dis=radius*0.6
        self.obj_nine_hitpoints=[]
        self.nine_hitpoints=[]
        self.obj_hitpoints=[]
        self.obj_other_hitpoints=[]
        self.other_hitpoints=[]
        for i in range(6):
            temp1other_hitpoints=[]
            temp1obj_other_hitpoints=[]
            obj_hitpoint=calculate_aim_point(self.obj,vir_hole_positions[i],hitball_dis)
            nine_hitpoint=calculate_aim_point(self.nine,vir_hole_positions[i],hitball_dis)
            obj_nine_hitpoint=calculate_aim_point(self.obj,nine_hitpoint,hitball_dis)
            for j in range(1,self.ballcount):
                other_hitpoint=calculate_aim_point(self.positions[j],vir_hole_positions[i],hitball_dis)
                obj_other_hitpoint=calculate_aim_point(self.obj,other_hitpoint,hitball_dis)
                temp1other_hitpoints.append(other_hitpoint)
                temp1obj_other_hitpoints.append(obj_other_hitpoint)
            self.obj_other_hitpoints.append(temp1obj_other_hitpoints)
            self.other_hitpoints.append(temp1other_hitpoints)
            self.obj_nine_hitpoints.append(obj_nine_hitpoint)
            self.obj_hitpoints.append(obj_hitpoint)
            self.nine_hitpoints.append(nine_hitpoint)
        method1_1=False
        method1=False
        method2_1=False
        method2=False
        method1obs=[]
        method1_1obs=[]
        method1_1vector=[]
        for i in range(6):
            temp1obs=0
            temp1_1obs=0
            temp1obs,_=check_obstacle_ball(self.positions,self.cue,self.obj_hitpoints[i],self.obj,temp1obs,1,self.ballcount)
            temp1_1obs,_=check_obstacle_ball(self.positions,self.cue,self.obj_nine_hitpoints[i],self.obj,temp1_1obs,1,self.ballcount)
            temp1_1vector=vector_angle(self.cue,self.obj_nine_hitpoints[i],self.nine_hitpoints[i])
            method1_1vector.append(temp1_1vector)
            method1_1obs.append(temp1_1obs)
            method1obs.append(temp1obs)
            if temp1obs==0:
                method1=True
            if temp1_1obs==0 and temp1_1vector<=0:
                method1_1=True
        print(method1_1vector)
        self.method2reflection_point=[]
        self.method2_1reflection_point=[]
        method2obs=[]
        method2_1obs=[]
        method2_1vector=[]
        method2_2vector=[]
        
        #
        for i in range(4):
            temp2reflection=[]
            temp2_1reflection=[]
            temp2obs=[]
            temp2_1angle=[]
            temp2_2angle=[]
            temp2_1obs=[]
            for j in range(6):
                temp1obs=0
                temp1_1obs=0
                temp1mirror=mirror_point(self.slope[i],self.wall_side[i],self.obj_hitpoints[j])
                temp1_1mirror=mirror_point(self.slope[i],self.wall_side[i],self.obj_nine_hitpoints[j])
                temp1_1reflection=segment_intersection(*self.boundaries[i],temp1_1mirror[0],temp1_1mirror[1])
                temp1reflection=segment_intersection(*self.boundaries[i],temp1mirror[0],temp1mirror[1])
                temp2reflection.append(temp1reflection)
                temp2_1reflection.append(temp1_1reflection)
                temp1obs,_=check_obstacle_ball(self.positions,self.cue,temp1reflection,self.obj,temp1obs,1,self.ballcount)
                temp1obs,_=check_obstacle_ball(self.positions,temp1reflection,self.obj_hitpoints[j],self.obj,temp1obs,1,self.ballcount)
                temp1_1obs,_=check_obstacle_ball(self.positions,self.cue,temp1_1reflection,self.obj,temp1_1obs,1,self.ballcount)
                temp1_1obs,_=check_obstacle_ball(self.positions,temp1_1reflection,self.obj_nine_hitpoints[j],self.obj,temp1_1obs,1,self.ballcount)
                temp1_1vector=vector_angle(temp1_1reflection,self.obj_nine_hitpoints[i],self.nine_hitpoints[i])
                temp1_2vector=vector_angle(self.obj_nine_hitpoints[i],self.nine_hitpoints[i],vir_hole_positions[i])
                if temp1obs==0:
                    method2=True
                if temp1_1obs==0 and temp1_1vector<=0 and temp1_2vector<=0:
                    method2_1=True
                temp2_1angle.append(temp1_1vector)
                temp2_2angle.append(temp1_2vector)
                temp2obs.append(temp1obs)
                temp2_1obs.append(temp1_1obs)
            method2_1vector.append(temp2_1angle)
            method2_2vector.append(temp2_2angle)
            self.method2reflection_point.append(temp2reflection)
            self.method2_1reflection_point.append(temp2_1reflection)
            method2obs.append(temp2obs)
            method2_1obs.append(temp2_1obs)
        
        print("1.1",method1_1,method1_1obs)
        print("2.1",method2_1,method2_1obs)
        print("1",method1,method1obs)
        print("2",method2,method2obs)
        if method1_1==True:
            return method_choice.method1_1(self)
        elif method1==True:
            return method_choice.method1(self)
        elif method2==True:
            return method_choice.method2(self)
        else:
            return method_choice.method3(self)

    def method1_1(self):
        route=1.1
        print(route)
        method1_1obs=[]
        method1_1angle=[]
        method1_2angle=[]
        method1_1dis=[]
        method1_1cue_obs=[]
        method1point_edge=[]
        for i in range(6):
            temp1obs=0
            temp1_1obs=0
            temp1obs,_=check_obstacle_ball(self.positions,self.cue,self.obj_nine_hitpoints[i],self.obj,temp1obs,1.1,self.ballcount)
            temp1_1obs,_=check_obstacle_ball(self.positions,self.obj_nine_hitpoints[i],self.nine_hitpoints[i],self.nine,temp1_1obs,1.1,self.ballcount)
            temp1_1obs,_=check_obstacle_ball(self.positions,self.nine_hitpoints[i],vir_hole_positions[i],vir_hole_positions[i],temp1_1obs,1.1,self.ballcount)
            temp1angle=vector_angle(self.cue,self.obj_nine_hitpoints[i],self.nine_hitpoints[i])
            temp1_1angle=vector_angle(self.obj_nine_hitpoints[i],self.nine_hitpoints[i],vir_hole_positions[i])
            temp1dis,_=distance_and_vector(self.cue,self.obj_nine_hitpoints[i])
            temp1_1dis,_=distance_and_vector(self.obj_nine_hitpoints[i],self.nine_hitpoints[i])
            temp1_2dis,_=distance_and_vector(self.nine_hitpoints[i],vir_hole_positions[i])
            method1_1dis.append(temp1dis+temp1_1dis+temp1_2dis)
            method1_1angle.append(temp1angle)
            method1_2angle.append(temp1_1angle)
            method1_1cue_obs.append(temp1obs)
            method1_1obs.append(temp1_1obs)
            temp1point_edge=False
            temp1point_edge=target_point_edge(self.obj_nine_hitpoints[i],temp1point_edge)
            temp1point_edge=target_point_edge(self.nine_hitpoints[i],temp1point_edge)
            method1point_edge.append(temp1point_edge)
        method1_1score=[]
        method1_1judge=False
        negative_num=[]
        for i in range(6):
            temp1score=cal_score(method1_1dis[i],-1,method1_1cue_obs[i],method1_1obs[i],method1point_edge[i],method1_1angle[i],method1_2angle[i],2)
            method1_1score.append(temp1score)
            if temp1score<=0:
                method1_1judge=True
                negative_num.append(temp1score)
        print("method1_1angle",method1_1angle)
        print("method1angle",method1_2angle)
        print("method1",method1_1dis)
        print(method1_1score)
        if method1_1judge==False:
            return method_choice.method1(self)
        for i in range(6):
            plt.plot([self.cue[0],self.obj_nine_hitpoints[i][0]],[self.cue[1],self.obj_nine_hitpoints[i][1]],linestyle='-',color='blue')
        best_score=max(negative_num)
        best_index=method1_1score.index(best_score)
        print("index1_1",best_index)
        best_vir_hole=vir_hole_positions[best_index]
        first_hitpoint=self.obj_nine_hitpoints[best_index]
        second_hitpoint=self.nine_hitpoints[best_index]
        route_obs=method1_1obs[best_index]
        cue_hitpoint=calculate_aim_point(self.cue,first_hitpoint,radius*0.9)
        _,best_vector=distance_and_vector(self.cue,first_hitpoint)
        around_detect=method_choice.edge_detect(self,cue_hitpoint)
        final(route,best_score,best_vector,route_obs,cue_hitpoint,around_detect)
        plt.plot([self.cue[0],first_hitpoint[0]],[self.cue[1],first_hitpoint[1]],linestyle='-',color='blue')
        plt.plot([self.obj[0],second_hitpoint[0]],[self.obj[1],second_hitpoint[1]],linestyle='-',color='blue')
        plt.plot([self.nine[0],best_vir_hole[0]],[self.nine[1],best_vir_hole[1]],linestyle='-',color='blue')
        screen2(self.ballcount,route,self.cue,self.obj,self.nine,self.positions)
        return best_score,best_vector[0], best_vector[1], around_detect, cue_hitpoint[0], cue_hitpoint[1]
            
    def method2_1(self):
        route=2.1
        print(route)
        method2_1obs=[]
        method2_1angle=[]
        method2_2angle=[]
        method2_1dis=[]
        method2_1cue_obs=[]
        method2_1point_edge=[]
        for j in range(4):
            temp2obs=[]
            temp2dis=[]
            temp2angle=[]
            temp2_1angle=[]
            temp2cue_obs=[]
            temp2point_edge=[]
            temp2dis2=[]
            
            for i in range(6):
                temp1obs=0
                temp1cue_obs=0
                temp1cue_obs,_=check_obstacle_ball(self.positions,self.cue,self.method2_1reflection_point[j][i],self.obj,temp1cue_obs,2.1,self.ballcount)
                temp1obs,_=check_obstacle_ball(self.positions,self.method2_1reflection_point[j][i],self.obj_nine_hitpoints[i],self.obj,temp1obs,2.1,self.ballcount)
                temp1obs,_=check_obstacle_ball(self.positions,self.obj_nine_hitpoints[i],self.nine_hitpoints[i],self.nine,temp1obs,2.1,self.ballcount)
                temp1obs,_=check_obstacle_ball(self.positions,self.nine_hitpoints[i],vir_hole_positions[i],vir_hole_positions[i],temp1obs,2.1,self.ballcount)
                temp1angle=vector_angle(self.method2_1reflection_point[j][i],self.obj_nine_hitpoints[i],self.nine_hitpoints[i])
                temp1_1angle=vector_angle(self.obj_nine_hitpoints[i],self.nine_hitpoints[i],vir_hole_positions[i])
                temp1dis,_=distance_and_vector(self.cue,self.obj_nine_hitpoints[i])
                temp1_1dis,_=distance_and_vector(self.obj_nine_hitpoints[i],self.nine_hitpoints[i])
                temp1_2dis,_=distance_and_vector(self.nine_hitpoints[i],vir_hole_positions[i])
                temp2dis.append(temp1dis+temp1_1dis+temp1_2dis)
                temp2dis2.append()
                temp2angle.append(temp1angle)
                temp2_1angle.append(temp1_1angle)
                temp2obs.append(temp1obs)
                temp2cue_obs.append(temp1cue_obs)
                temp1point_edge=False
                temp1point_edge=target_point_edge(self.method2_1reflection_point[j][i],temp1point_edge)
                temp1point_edge=target_point_edge(self.obj_nine_hitpoints[i],temp1point_edge)
                temp1point_edge=target_point_edge(self.nine_hitpoints[i],temp1point_edge)
                temp2point_edge.append(temp1point_edge)
            
            method2_1point_edge.append(temp2point_edge)
            method2_1cue_obs.append(temp2cue_obs)
            method2_1dis.append(temp2dis)
            method2_1angle.append(temp2angle)
            method2_2angle.append(temp2_1angle)
            method2_1obs.append(temp2obs)
        print(method2_1point_edge)
        method2_1judge=False
        method2_1score=[]
        for j in range(4):
            temp2score=[]
            for i in range(6):
                temp1score=cal_score(method2_1dis[j][i],method2_1cue_obs[j][i],method2_1obs[j][i],method2_1point_edge[j][i],method2_1angle[j][i],method2_2angle[j][i],2)
                temp2score.append(temp1score)
                if temp1score<=0:
                    method2_1judge=True
            method2_1score.append(temp2score)
        print("method2_1score",method2_1score)
        if method2_1judge==False:
            return method_choice.method1(self)
        best_score,best_index1,best_index2=find_min_negative_integer_in_nested_list(method2_1score)
        best_vir_hole=vir_hole_positions[best_index2]
        reflection_point=self.method2_1reflection_point[best_index1][best_index2]
        first_hitpoint=self.obj_nine_hitpoints[best_index2]
        second_hitpoint=self.nine_hitpoints[best_index2]
        cue_hitpoint=calculate_aim_point(self.cue,reflection_point,radius*0.9)
        _,hitvector=distance_and_vector(self.cue,reflection_point)
        route_obs=method2_1obs[best_index1][best_index2]
        around_detect=method_choice.edge_detect(self,cue_hitpoint)
        plt.plot(cue_hitpoint[0],cue_hitpoint[1],marker='o',ms=3,color='red')
        plt.plot([self.cue[0],reflection_point[0]],[self.cue[1],reflection_point[1]],linestyle='-',color='red')
        plt.plot([reflection_point[0],first_hitpoint[0]],[reflection_point[1],first_hitpoint[1]],linestyle='-',color='red')
        plt.plot([self.obj[0],second_hitpoint[0]],[self.obj[1],second_hitpoint[1]],linestyle='-',color='red')
        plt.plot([self.nine[0],best_vir_hole[0]],[self.nine[1],best_vir_hole[1]])
        final(route,best_score,hitvector,route_obs,cue_hitpoint,around_detect)
        screen2(self.ballcount,route,self.cue,self.obj,self.nine,self.positions)
        return best_score,hitvector[0], hitvector[1], around_detect, cue_hitpoint[0], cue_hitpoint[1]
    def method1(self):
        route=1
        print(route)
        method1obs=[]
        method1angle=[]
        method1dis=[]
        method1cue_obs=[]
        method1point_edge=[]
        for i in range(6):
            temp1obs=0
            temp1cue_obs=0
            temp1point_edge=False
        
            temp1cue_obs,_=check_obstacle_ball(self.positions,self.cue,self.obj_hitpoints[i],self.obj,temp1cue_obs,1,self.ballcount)
            temp1obs,_=check_obstacle_ball(self.positions,self.obj_hitpoints[i],vir_hole_positions[i],vir_hole_positions[i],temp1obs,1,self.ballcount)
            temp1angle=vector_angle(self.cue,self.obj_hitpoints[i],vir_hole_positions[i])
            temp1point_edge=target_point_edge(self.obj_hitpoints[i],temp1point_edge)
            # temp1_1angle=vector_angle(self.obj_nine_hitpoints[i],self.nine_hitpoints[i],vir_hole_positions[i])
            temp1dis,_=distance_and_vector(self.cue,self.obj_hitpoints[i])
            temp1_1dis,_=distance_and_vector(self.obj_nine_hitpoints[i],vir_hole_positions[i])
            method1dis.append(temp1dis+temp1_1dis)
            method1angle.append(temp1angle)
            method1obs.append(temp1obs)
            method1cue_obs.append(temp1cue_obs)
            method1point_edge.append(temp1point_edge)
        method1score=[]
        method1judge=False
        negative_num=[]
        print("method1angle",method1angle)
        for i in range(6):
            temp1score=cal_score(method1dis[i],-1,method1cue_obs[i],method1obs[i],method1point_edge[i],method1angle[i],-1,1)
            method1score.append(temp1score)
            if temp1score<=0:
                method1judge=True 
                negative_num.append(temp1score)
        print(method1score)
        
        if method1judge==False:
            return method_choice.method2(self)
        for i in range(6):
            plt.plot([self.cue[0],self.obj_hitpoints[i][0]],[self.cue[1],self.obj_hitpoints[i][1]],linestyle='-',color='blue') 
            # return method_choice.method2_1(self)
        best_score=max(negative_num)
        best_index=method1score.index(best_score)
        print("index1",best_index)
        best_vir_hole=vir_hole_positions[best_index]
        first_hitpoint=self.obj_hitpoints[best_index]
        route_obs=method1obs[best_index]
        cue_hitpoint=calculate_aim_point(self.cue,first_hitpoint,radius*0.9)
        _,best_vector=distance_and_vector(self.cue,first_hitpoint)
        around_detect=method_choice.edge_detect(self,cue_hitpoint)
        final(route,best_score,best_vector,route_obs,cue_hitpoint,around_detect)
        plt.plot([self.cue[0],first_hitpoint[0]],[self.cue[1],first_hitpoint[1]],linestyle='-',color='red')
        plt.plot([self.obj[0],best_vir_hole[0]],[self.obj[1],best_vir_hole[1]],linestyle='-',color='blue')
        screen2(self.ballcount,route,self.cue,self.obj,self.nine,self.positions)  
        return best_score,best_vector[0], best_vector[1], around_detect, cue_hitpoint[0], cue_hitpoint[1]
    def method2(self):
        route=2
        print(route)
        method2obs=[]
        method2angle=[]
        method2_1angle=[]
        method2dis=[]
        method2point_edge=[]
        method2cue_obs=[]
        method2dis2=[]
        for j in range(4):
            temp2_1angle=[]
            temp2_1dis=[]
            temp2_1obs=[]
            temp2cue_obj=[]
            temp2point_edge=[]
            temp2dis2=[]
            for i in range(6):
                temp1obs=0
                temp1cue_obs=0
                temp1point_edge=False
                temp1point_edge=target_point_edge(self.method2reflection_point[j][i],temp1point_edge)
                temp1point_edge=target_point_edge(self.obj_hitpoints[i],temp1point_edge)
                temp2point_edge.append(temp1point_edge)
                temp1cue_obs,_=check_obstacle_ball(self.positions,self.cue,self.method2reflection_point[j][i],self.obj,temp1cue_obs,2,self.ballcount)
                temp1cue_obs,_=check_obstacle_ball(self.positions,self.method2reflection_point[j][i],self.obj_hitpoints[i],self.obj,temp1cue_obs,2,self.ballcount)
                temp1obs,_=check_obstacle_ball(self.positions,self.obj_hitpoints[i],vir_hole_positions[i],vir_hole_positions[i],temp1obs,2,self.ballcount)
                temp1angle=vector_angle(self.method2reflection_point[j][i],self.obj_hitpoints[i],vir_hole_positions[i])
                # temp1_1angle=vector_angle(self.obj_nine_hitpoints[i],self.nine_hitpoints[i],vir_hole_positions[i])
                temp1dis,_=distance_and_vector(self.cue,self.method2reflection_point[j][i])
                temp1_1dis,_=distance_and_vector(self.method2reflection_point[j][i],self.obj_hitpoints[i])
                temp1_2dis,_=distance_and_vector(self.obj_hitpoints[i],vir_hole_positions[i])
                temp2_1angle.append(temp1angle)
                temp2dis2.append(temp1dis+temp1_1dis)
                temp2_1dis.append(temp1_2dis)
                temp2_1obs.append(temp1obs)
                temp2cue_obj.append(temp1cue_obs)
            method2dis2.append(temp2dis2)
            method2cue_obs.append(temp2cue_obj)
            method2obs.append(temp2_1obs)
            method2dis.append(temp2_1dis)
            method2angle.append(temp2_1angle)
            method2point_edge.append(temp2point_edge)
        print("method2",method2dis2)
                # method2_2angle.append(temp1_1angle)
        method2judge=False
        method2score=[]
        for j in range(4):
            temp2score=[]
            for i in range(6):
                temp1score=cal_score(method2dis[j][i],method2dis2[j][i],method2cue_obs[j][i],method2obs[j][i],method2point_edge[j][i],method2angle[j][i],-1,3)
                temp2score.append(temp1score)
                if temp1score<=0:
                    method2judge=True
            method2score.append(temp2score)
        print(method2score)
        # for j in range(4):
        #     for i in range(6):
        #         plt.plot([self.cue[0],self.method2reflection_point[j][i][0]],[self.cue[1],self.method2reflection_point[j][i][1]],linestyle='-',color='blue') 
        #         plt.plot([self.method2reflection_point[j][i][0],self.obj_hitpoints[i][0]],[self.method2reflection_point[j][i][1],self.obj_hitpoints[i][1]],linestyle='-',color='green') 
        if method2judge==False:
            # screen2(self.ballcount,route,self.cue,self.obj,self.nine,self.positions)
            return method_choice.method3(self)
        best_score,best_index1,best_index2=find_min_negative_integer_in_nested_list(method2score)
        best_vir_hole=vir_hole_positions[best_index2]
        reflection_point=self.method2reflection_point[best_index1][best_index2]
        first_hitpoint=self.obj_hitpoints[best_index2]
        vir_hole=vir_hole_positions[best_index2]
        cue_hitpoint=calculate_aim_point(self.cue,reflection_point,radius*0.9)
        _,hitvector=distance_and_vector(self.cue,reflection_point)
        route_obs=method2obs[best_index1][best_index2]
        around_detect=method_choice.edge_detect(self,cue_hitpoint)
        plt.plot(cue_hitpoint[0],cue_hitpoint[1],marker='o',ms=3,color='red')
        plt.plot([self.cue[0],reflection_point[0]],[self.cue[1],reflection_point[1]],linestyle='-',color='red')
        plt.plot([reflection_point[0],first_hitpoint[0]],[reflection_point[1],first_hitpoint[1]],linestyle='-',color='red')
        plt.plot([self.obj[0],vir_hole[0]],[self.obj[1],vir_hole[1]],linestyle='-',color='red')
        final(route,best_score,hitvector,route_obs,cue_hitpoint,around_detect)
        screen2(self.ballcount,route,self.cue,self.obj,self.nine,self.positions)
        return best_score,hitvector[0], hitvector[1], around_detect, cue_hitpoint[0], cue_hitpoint[1]

    def method3(self):        
        route=3
        print(route)
        method2obs=[]
        method2angle=[]
        method2_1angle=[]
        method2dis=[]
        method2_2angle=[]
        method2cue_obs=[]
        method2point_edge=[]
        print("obj_other_point",self.obj_other_hitpoints)
        print("other_point",self.other_hitpoints)
        for i in range(6):
            temp2_1angle=[]
            temp2_1dis=[]
            temp2_1obs=[]
            temp2_2angle=[]
            temp2cue_obs=[]
            temp2point_edge=[]
            for j in range(self.ballcount-1):
                temp1obs=0
                temp1cue_obj=0
                temp1point_edge=False
                
                temp1point_edge=target_point_edge(self.obj_other_hitpoints[i][j],temp1point_edge)
                temp1point_edge=target_point_edge(self.other_hitpoints[i][j],temp1point_edge)
                temp2point_edge.append(temp1point_edge)
                temp1cue_obj,_=check_obstacle_ball(self.positions,self.cue,self.obj_other_hitpoints[i][j],self.obj,temp1cue_obj,3,self.ballcount)
                temp1obs,_=check_obstacle_ball(self.positions,self.obj,self.other_hitpoints[i][j],self.positions[j],temp1obs,3,self.ballcount)
                temp1obs,_=check_obstacle_ball(self.positions,self.positions[j],vir_hole_positions[i],vir_hole_positions[i],temp1obs,3,self.ballcount)
                temp1angle=vector_angle(self.cue,self.obj_other_hitpoints[i][j],self.other_hitpoints[i][j])
                temp1_1angle=vector_angle(self.obj_other_hitpoints[i][j],self.other_hitpoints[i][j],vir_hole_positions[i])
                temp1dis,_=distance_and_vector(self.cue,self.obj_other_hitpoints[i][j])
                temp1_1dis,_=distance_and_vector(self.obj,self.other_hitpoints[i][j])
                temp1_2dis,_=distance_and_vector(self.positions[j],vir_hole_positions[i])
                temp2_1angle.append(temp1angle)
                temp2_2angle.append(temp1_1angle)
                temp2_1dis.append(temp1dis+temp1_1dis+temp1_2dis)
                temp2_1obs.append(temp1obs)
                temp2cue_obs.append(temp1cue_obj)
            method2point_edge.append(temp2point_edge)
            method2cue_obs.append(temp2cue_obs)
            method2_2angle.append(temp2_2angle)
            method2obs.append(temp2_1obs)
            method2dis.append(temp2_1dis)
            method2angle.append(temp2_1angle)
        print("emthod2angle",method2angle)
        print("method2_2angle",method2_2angle)
                # method2_2angle.append(temp1_1angle)
        method3judge=False
        method3score=[]
        for j in range(6):
            temp2score=[]
            for i in range(self.ballcount-1):
                temp1score=cal_score(method2dis[j][i],1,method2cue_obs[j][i],method2obs[j][i],method2point_edge[j][i],method2angle[j][i],method2_2angle[j][i],2)
                temp2score.append(temp1score)
                if temp1score<=0:
                    method3judge=True
            method3score.append(temp2score)
        print("method3angle1",method2angle)
        print("method3angle2",method2_2angle)
        print("method3,",method3score)
        print("method3obs",method2cue_obs)
        # for j in range(4):
        #     for i in range(6):
        #         plt.plot([self.cue[0],self.obj_other_hitpoints[j][i][0]],[self.cue[1],self.obj_other_hitpoints[j][i][1]],linestyle='-',color='blue') 
        #         plt.plot([self.obj_other_hitpoints[j][i][0],self.other_hitpoints[j][i][0]],[self.obj_other_hitpoints[j][i][1],self.other_hitpoints[j][i][1]],linestyle='-',color='green') 
        if method3judge==False:
            return method_choice.method4(self)
        best_score,best_index1,best_index2=find_min_negative_integer_in_nested_list(method3score)
        print("index",best_index1,best_index2)
        best_vir_hole=vir_hole_positions[best_index1]
        second_hitpoint=self.other_hitpoints[best_index1][best_index2]
        first_hitpoint=self.obj_other_hitpoints[best_index1][best_index2]
        cue_hitpoint=calculate_aim_point(self.cue,first_hitpoint,radius*0.9)
        _,hitvector=distance_and_vector(self.cue,first_hitpoint)
        target_ball=self.positions[best_index2+1]
        route_obs=method2obs[best_index1][best_index2]
        around_detect=method_choice.edge_detect(self,cue_hitpoint)
        plt.plot(cue_hitpoint[0],cue_hitpoint[1],marker='o',ms=3,color='red')
        plt.plot([self.cue[0],first_hitpoint[0]],[self.cue[1],first_hitpoint[1]],linestyle='-',color='red')
        plt.plot([self.obj[0],second_hitpoint[0]],[self.obj[1],second_hitpoint[1]],linestyle='-',color='red')
        plt.plot([target_ball[0],best_vir_hole[0]],[target_ball[1],best_vir_hole[1]],linestyle='-',color='red')
        final(route,best_score,hitvector,route_obs,cue_hitpoint,around_detect)
        screen2(self.ballcount,route,self.cue,self.obj,self.nine,self.positions)
        return best_score,hitvector[0], hitvector[1], around_detect, cue_hitpoint[0], cue_hitpoint[1]
        
    def method4(self):
        route=4
        print(route)
        _,hitvector=distance_and_vector(self.cue,self.obj)
        best_score=-10000
        cue_hitpoint=calculate_aim_point(self.cue,self.obj,radius*0.9)
        around_detect=method_choice.edge_detect(self,cue_hitpoint)
        final(route,best_score,hitvector,0,cue_hitpoint,around_detect)
        plt.plot([self.cue[0],self.obj[0]],[self.cue[1],self.obj[1]],linestyle='-',color='red')
        screen2(self.ballcount,route,self.cue,self.obj,self.nine,self.positions)
        return best_score,hitvector[0], hitvector[1], around_detect, cue_hitpoint[0], cue_hitpoint[1]
if __name__== '__main__':
    while True:
        balls=[]
        ballcount=8
        #def generate the ball
        cuex, cuey, ballx_set, bally_set, ball_count=generate_balls(ballcount,radius)
        print(ballx_set)
        print(bally_set)
        ballcount+=1
        print("self.ballcount",ballcount)
        main=method_choice(ballx_set,bally_set,ballcount,cuex,cuey)
        main.main()
