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
width=627
height=304
radius = 16
hole_radius = 20
# Table coordinates
x1 = -311.196
y1 = 612
# x1=-100
# y1=100
hole_positions = [(x1, y1),(x1, y1-height), (x1 + width / 2, y1- height), (x1 + width, y1-height),(x1+width, y1), (x1 + width / 2, y1)]
vir_hole_positions = [(x1+radius, y1-radius),(x1+radius, y1-height+radius), (x1 + width / 2, y1- height+radius), (x1 + width-radius, y1-height+radius),(x1+width-radius, y1-radius), (x1 + width / 2, y1-radius)]
holex=[x1,x1,x1+width,x1+width,x1+width,x1+width]
holey=[y1,y1-height,y1-height,y1-height,y1,y1]
actualwidth =62.7
actualheight=30.4
# holex=[x1,x1+width/2,x1+width,x1,x1+width/2,x1+width]
# holey=[y1,y1,y1,y1+height,y1+height,y1+height]


def distance_and_vector(point1,point2):
    n1x,n1y=point1
    n2x,n2y=point2
    dx = n1x - n2x
    dy = n1y - n2y
    dist = math.sqrt(dx ** 2 + dy ** 2)
    return round(dist, 2), (dx, dy)

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
        if not is_overlapping(x, y,cuex,cuey, ball_positions, radius):
            ball_positions.append((x, y))

    ballx_set = [pos[0] for pos in ball_positions]
    bally_set = [pos[1] for pos in ball_positions]

    return cuex, cuey, ballx_set, bally_set, ballcount
def calculate_aim_point(target_point,obj_point,empty1):
    # 计算从球到目标的向量
    ball_diameter=0.8*radius
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



def check_obstacle_ball(obs_ball, obj_point, target_point, obs_count):
    maskwidth = 1.6*radius
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
    ploy = (first_poly, second_poly, third_poly, fourth_poly)

    polygon = Polygon(ploy)
    shapely_objectballs = Point(obs_ball[0], obs_ball[1])
    
    if polygon.contains(shapely_objectballs):
        obs_count =obs_count+1
        return obs_count, obs_ball
    return obs_count, -1
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
    if deg<=100:
        deg=-deg
    return deg

def cal_score(distance, obj_holeobs,angle1,angle2,n):
    if n==1:
        score = ((angle1 * 22) + (distance * -1) + (obj_holeobs * -4000))
        if angle1>0:
            score=abs(score)
    elif n==2:
        score = ((angle1 * 22)/2 +(angle2*22)/2 +(distance * -1) + (obj_holeobs * -4000))
        if angle1>=0 or angle2 >= 0:
            score = abs(score)
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
    # plt.grid()
    # plt.plot([holex[0],holex[2]],[holey[0],holey[2]],[holex[2],holex[5]],[holey[2],holey[5]],
    #          [holex[5],holex[3]],[holey[5],holey[3]],[holex[3],holex[0]],[holey[3],holey[0]],color='black')
    plt.plot([holex[0],holex[5]],[holey[0],holey[5]],[holex[5],holex[3]],[holey[5],holey[3]],[holex[3],holex[1]],[holey[3],holey[1]],[holex[1],holex[0]],[holey[1],holey[0]],color='black')
    plt.plot(obj[0],obj[1],marker='o',ms=2*radius,color='yellow')
    plt.plot(cue[0],cue[1],marker='o',ms=2*radius,color='red')
    plt.plot(nine[0],nine[1],marker='o',ms=2*radius,color='pink')
    
    for i in range(1,ballcount-1):
        plt.plot(ballx_set[i],bally_set[i],marker='o',ms=2*radius,color='blue')
        plt.text(ballx_set[i], bally_set[i], ((ballx_set[i],bally_set[i]),i+1),color='black', fontweight='bold')
    for i in range(6):
        plt.plot(hole_positions[i][0],hole_positions[i][1],marker = 'o',ms=2*hole_radius,color='black')
        plt.plot(vir_hole_positions[i][0],vir_hole_positions[i][1],marker = 'o',ms=2*hole_radius,color='black')
    plt.show()
    
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

# def method1():
class method_choice():
    def __init__(self,ballx_set,bally_set,ballcount,cuex,cuey):
        self.cue=(cuex,cuey)
        self.nine=(ballx_set[ballcount-1],bally_set[ballcount-1])
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
        hitcuepointx,hitcuepointy=best_cue_hitpoint
        cue_obstacle=0
        if hitcuepointx - radius < x1 or hitcuepointx + radius > x1 + width or hitcuepointy - radius < y1 or hitcuepointy + radius > y1 + height:
            return True
        for i in range(self.ballcount):
            cue_obstacle,_=check_obstacle_ball(self.positions[i],self.cue,best_cue_hitpoint,cue_obstacle)
            return True
        return False

    def final(self,routenumber,bestscore,bestvx,bestvy,obstacle,best_cue_hitpoint,cue_obstacle):
        print("---------------------------------------------")
        print("routenumber",routenumber)
        print("Score:", bestscore)
        print("vx, vy:", bestvx, bestvy)
        print("Obstacles on the route:", obstacle)
        print("x, y:", best_cue_hitpoint)
        print("there have obstacle around cue",cue_obstacle)
    
    
    def main(self):
        #generate judge condition
        print("obj",self.obj)
        print("cue",self.cue)
        print("nine",self.nine)
        print(self.positions)
        print("ballcount",self.ballcount)
        #-------------------hitpoint--------------#
        self.obj_holes_hitpoints = []
        self.nine_holes_hitpoints = []
        self.obj_nines_hitpoints=[]
        for i in range(6):
            objhitpoint = calculate_aim_point(self.obj,vir_hole_positions[i], radius*0.8)
            ninehitpoint =calculate_aim_point(self.nine,vir_hole_positions[i], radius/2)
            obj_nines_hitpoint=calculate_aim_point(self.obj,ninehitpoint,radius/2)
            self.obj_holes_hitpoints.append(objhitpoint)
            self.nine_holes_hitpoints.append(ninehitpoint)
            self.obj_nines_hitpoints.append(obj_nines_hitpoint)
        self.cue_obj_others_hitpoints=[]
        self.others_hitpoints=[]
        for i in range(self.ballcount):
            obj_other_hitpoints=[]
            other_hitpoints=[]
            for j in range(6):
                other_hitpoint=calculate_aim_point(self.positions[i],vir_hole_positions[j],radius/2)
                other_hitpoints.append(other_hitpoint)
                obj_other_hitpoint=calculate_aim_point(self.obj,other_hitpoint,radius/2)
                obj_other_hitpoints.append(obj_other_hitpoint)
            self.cue_obj_others_hitpoints.append(obj_other_hitpoints)
            self.others_hitpoints.append(other_hitpoints)
        #---------angle,obs==>method judge----------#
        cue_obj_nine_obstacles1 = []
        self.cue_obj_nines_angle=[]
        method1_1=False
        method1=False
        method2_1=False
        method2=False
        #--------------method1 judge-------------#
        cue_obj_obs1=[]
        for i in range(6):
            cue_obj_obstacle1 = 0
            cue_obj_nine_angle=vector_angle(self.cue,self.obj,self.nine_holes_hitpoints[i])
            self.cue_obj_nines_angle.append(cue_obj_nine_angle)
            cue_obj_nine_obs=0
            cue_obj_obs=0
            for j in range(1,self.ballcount):
                cue_obj_nine_obs,_=check_obstacle_ball(self.positions[j],self.cue,self.obj_nines_hitpoints[i],cue_obj_nine_obs)
                cue_obj_obs,_=check_obstacle_ball(self.positions[j],self.cue,self.obj_holes_hitpoints[i],cue_obj_obs)
            cue_obj_nine_obstacles1.append(cue_obj_nine_obs)
            cue_obj_obs1.append(cue_obj_obs)
        for i in range(6):
            if cue_obj_nine_obstacles1[i] ==0 and self.cue_obj_nines_angle[i] <=0:
                method1_1=True
            if cue_obj_obs1[i]==0:
                method1=True
        #------------method2 judge--------------#
        print("first_route_choice",cue_obj_nine_obstacles1)
        print("first_route_straight",cue_obj_obs1)
            
        self.reflection_obj_points=[]
        self.reflection_obj_nine_points=[]  
        for i in range(4):
            temp2reflection_obj=[]
            temp2reflection_obj_nine=[]
            for j in range(6):
                temp1mirror=mirror_point(self.slope[i],self.wall_side[i],self.obj_nines_hitpoints[j])
                temp1_1mirror=mirror_point(self.slope[i],self.wall_side[i],self.obj_holes_hitpoints[j])
                temp1reflection=segment_intersection(*self.boundaries[i],temp1_1mirror[0],temp1_1mirror[1])
                temp1_1reflection=segment_intersection(*self.boundaries[i],temp1mirror[0],temp1mirror[1])
                plt.plot(temp1reflection[0],temp1reflection[1],marker = 'o',ms=3,color='red')
                plt.plot(temp1_1reflection[0],temp1_1reflection[1],marker = 'o',ms=3,color='red')
                temp2reflection_obj.append(temp1reflection)
                temp2reflection_obj_nine.append(temp1_1reflection)
            self.reflection_obj_nine_points.append(temp2reflection_obj_nine)   
            self.reflection_obj_points.append(temp2reflection_obj)
        
        reflection_obj_nines_angles=[]
        reflection_obj_angles=[]
        for i in range(4):
            temp1=[]
            temp2=[]
            for j in range(6):
                reflection_obj_nines_angle=vector_angle(self.reflection_obj_nine_points[i][j],self.obj_nines_hitpoints[j],self.nine_holes_hitpoints[j])
                cue_reflection_obj_angle=vector_angle(self.cue,self.reflection_obj_nine_points[i][j],self.obj_nines_hitpoints[j])
                temp1.append(reflection_obj_nines_angle)
                temp2.append(cue_reflection_obj_angle)
            reflection_obj_nines_angles.append(temp1)
            reflection_obj_angles.append(temp2)
        reflection_obj_obs = []
        reflection_obj_nine_obs = []

        for i in range(4):  # 对每组反射点进行迭代
            temp2obj_nine_obs = []
            temp2_1obj_obs = []
            for j in range(6):  # 对每个反射点进行迭代
                temp1obj_nine_obs = 0
                temp1_1obj_obs = 0
                for k in range(1,self.ballcount):  # 对每个球的位置进行迭代
                    # 检查球与反射点的碰撞
                    temp1obj_nine_obs, _ = check_obstacle_ball(self.positions[k], self.cue, self.reflection_obj_nine_points[i][j], temp1obj_nine_obs)
                    temp1obj_nine_obs, _ = check_obstacle_ball(self.positions[k], self.reflection_obj_nine_points[i][j], self.obj_nines_hitpoints[j], temp1obj_nine_obs)
                    temp1_1obj_obs, _ = check_obstacle_ball(self.positions[k], self.cue, self.reflection_obj_points[i][j], temp1_1obj_obs)
                    temp1_1obj_obs, _ = check_obstacle_ball(self.positions[k], self.reflection_obj_points[i][j], self.obj_holes_hitpoints[j], temp1_1obj_obs)
                
                # 将检测结果存储到临时列表中
                temp2obj_nine_obs.append(temp1obj_nine_obs)
                temp2_1obj_obs.append(temp1_1obj_obs)
            # 将临时列表添加到结果列表中
            reflection_obj_nine_obs.append(temp2obj_nine_obs)
            reflection_obj_obs.append(temp2_1obj_obs)
        print("method2",reflection_obj_obs)
        print('method2_1',reflection_obj_nine_obs)
        #------------------method_route_judge---------------------------#        
        for i in range(4):
            for j in range(6):
                if reflection_obj_angles[i][j] <= 0 and reflection_obj_nines_angles[i][j] <= 0 and reflection_obj_nine_obs[i][j]==0 : 
                    method2_1=True
                if reflection_obj_obs[i][j]==0:
                    method2=True
        print("1.1",method1_1)
        print("2.1",method2_1)
        print("1",method1)
        print("2",method2)
        if method1_1==True:
            return method_choice.method1_1(self)
        elif method2_1==True:
            return method_choice.method2_1(self)
        elif method1==True:
            return method_choice.method1(self)
        elif method2==True:
            return method_choice.method2(self)
        else:
            return method_choice.method3(self)
        
        
    def method1_1(self):
        route=1.1
        print(route)
        #--------obs,angle----------#
        obj_nine_hole_obs=[]
        method1_1=False
        #--------obs----------#
        for i in range(6):
            temp1obs=0

            for j in range(1,len(self.positions)-1):

                temp1obs,_=check_obstacle_ball(self.positions[j],self.obj,self.obj_nines_hitpoints[i],temp1obs)
                temp1obs,_=check_obstacle_ball(self.positions[j],self.nine,self.nine_holes_hitpoints[i],temp1obs)
            obj_nine_hole_obs.append(temp1obs)
            if temp1obs==0:
                method1_1=True

        #--------judge------#
            
        if method1_1==False:
            return method_choice.method1_2(self)
        #-----distance,score-----#
        cue_hole_dis=[]
        scores1_1=[]
        hit_vectors=[]  
        obj_nine_angle=[]
        cue_obj_angle=[]
        method1_1judge=False
        for i in range(6):
            temp1dis,temp1vector=distance_and_vector(self.cue,self.obj_nines_hitpoints[i])
            temp1_1dis,_=distance_and_vector(self.obj,self.nine_holes_hitpoints[i])
            temp1_2dis,_=distance_and_vector(self.nine,vir_hole_positions[i])
            cue_hole_dis.append(temp1dis+temp1_1dis+temp1_2dis)
            hit_vectors.append(temp1vector)
            temp1_1cue_obj_nine_angle=vector_angle(self.cue,self.obj_nines_hitpoints[i],self.nine_holes_hitpoints[i])
            temp1obj_nine_angle=vector_angle(self.obj,self.nine_holes_hitpoints[i],vir_hole_positions[i])
            cue_obj_angle.append(temp1_1cue_obj_nine_angle)
            obj_nine_angle.append(temp1obj_nine_angle)
        print(cue_obj_angle)
        print(obj_nine_angle)
        for i in range(6):
            temp1score=cal_score(cue_hole_dis[i],obj_nine_hole_obs[i],cue_obj_angle[i],obj_nine_angle[i],2)
            scores1_1.append(temp1score)
            if temp1score<0:
                method1_1judge=True
        print(method1_1)
        if method1_1judge==True:
            non_positive_scores = [score for score in scores1_1 if score <= 0]
            max_non_positive_score = max(non_positive_scores)
            best_index = scores1_1.index(max_non_positive_score)
            best_virhole = vir_hole_positions[best_index]
            first_hitpoint = self.obj_nines_hitpoints[best_index]
            second_hitpoint = self.nine_holes_hitpoints[best_index]
            best_hit_vector = hit_vectors[best_index]
            routeobs = obj_nine_hole_obs[best_index]
            hitcuepoint = calculate_aim_point(self.cue,first_hitpoint, radius/2)
            
            
            cue_obstacle=method_choice.edge_detect(self,hitcuepoint)
            #----------screen-----------#
            method_choice.final(self,route,max_non_positive_score, best_hit_vector[0], best_hit_vector[1], routeobs, hitcuepoint,cue_obstacle)
            plt.plot([self.cue[0],first_hitpoint[0]],[self.cue[1],first_hitpoint[1]],linestyle='-')
            plt.plot([self.obj[0],second_hitpoint[0]],[self.obj[1],second_hitpoint[1]],linestyle='-')
            plt.plot([self.nine[0],best_virhole[0]],[self.nine[1],best_virhole[1]])
            screen2(self.ballcount,route,self.cue,self.obj,self.nine,self.positions)
            return max_non_positive_score,best_hit_vector[0], best_hit_vector[1], routeobs, hitcuepoint[0], hitcuepoint[1]
        else:
            return method_choice.method1_2(self)
        
    def method1_2(self):
        route=1.2
        print(route)
        method1_2= False
        #---------------#
        reflection_obj_nine_points=[]
        obj_nine_holes_angles=[]
        reflec_obj_nine_obs_group=[]
        #----------cal reflection point-------------#
        for i in range(4):
            temp2reflection_obj_nines=[]
            for j in range(6):
                temp1mirror=mirror_point(self.slope[i],self.wall_side[i],self.nine_holes_hitpoints[j])
                temp1reflection_obj_nine=segment_intersection(*self.boundaries[i],temp1mirror[0],temp1mirror[1])
                temp2reflection_obj_nines.append(temp1reflection_obj_nine)
            reflection_obj_nine_points.append(temp2reflection_obj_nines)
        method1_2obs=[]
        for i in range(4):
            temp2obs=[]
            for j in range(6):
                temp1obs=0
                for k in range(1,len(self.positions)):
                    temp1obs,_=check_obstacle_ball(self.positions[k],self.cue,self.obj_nines_hitpoints[j],temp1obs)
                    temp1obs,_=check_obstacle_ball(self.positions[k],self.obj,reflection_obj_nine_points[i][j],temp1obs)
                    temp1obs,_=check_obstacle_ball(self.positions[k],reflection_obj_nine_points[i][j],self.nine,temp1obs)
                temp2obs.append(temp1obs)
            method1_2obs.append(temp2obs)
        #----------obs、angle----------------------#
        reflection_obj_nine_angles=[]
        obj_nine_hole_angles=[]
        for i in range(4):
            temp2reflection_obj_nine_angle=[]
            for j in range(6):
                temp1reflection_obj_nine_angle=vector_angle(reflection_obj_nine_points[i][j],self.obj_nines_hitpoints[j],self.nine_holes_hitpoints[j])
                temp1obj_nine_hole_angle=vector_angle(self.obj_nines_hitpoints[j],self.nine_holes_hitpoints[j],vir_hole_positions[j])
                temp2reflection_obj_nine_angle.append(temp1reflection_obj_nine_angle)
                obj_nine_hole_angles.append(temp1obj_nine_hole_angle)
            reflection_obj_nine_angles.append(temp2reflection_obj_nine_angle)
        for i in range(4):
            for j in range(6):
                if method1_2obs[i][j]==0 and reflection_obj_nine_angles[i][j] <= 0:
                    method1_2=True
        #------------judge-------------#
        if method1_2==False:
            return method_choice.method1(self)
        #--------------dis,score---------------#
        method1_2_diss1=[]
        method1_2_diss2=[]
        hit_vectors=[]
        for i in range(4):
            method1_2_diss1=[]
            for j in range(6):
                cue_reflect_dis,hit_vector=distance_and_vector(self.cue,reflection_obj_nine_points[i][j])
                hit_vectors.append(hit_vector)
                reflect_obj_dis,_=distance_and_vector(reflection_obj_nine_points[i][j],self.nine_holes_hitpoints[j])
                obj_nine_dis,_=distance_and_vector(self.obj,self.obj_nines_hitpoints[j])
                nine_hole_dis,_=distance_and_vector(self.nine,vir_hole_positions[j])
                method1_2_dis=cue_reflect_dis+reflect_obj_dis+obj_nine_dis+nine_hole_dis
                method1_2_diss1.append(method1_2_dis)
            method1_2_diss2.append(method1_2_diss1)
        method1_2scores2=[]
        for i in range(4):
            method1_2scores=[]
            for j in range(6):
                method1_2score=cal_score(method1_2_diss2[i][j],method1_2obs[i][j],reflection_obj_nine_angles[i][j],obj_nine_hole_angles[j],2)
                method1_2scores.append(method1_2score)
            method1_2scores2.append(method1_2scores)
        max_non_positive_score,best_index1,best_index2=find_min_negative_integer_in_nested_list(method1_2scores2)
        #-------------choice---------------#
        if max_non_positive_score:
            best_virhole = vir_hole_positions[best_index2]
            reflection_point = reflection_obj_nine_points[best_index1][best_index2]
            first_hitpoint = self.obj_holes_hitpoints[best_index2]
            second_hitpoint = self.nine_holes_hitpoints[best_index2]
            best_cue_hitpoint=calculate_aim_point(self.cue,first_hitpoint,radius/2)
            best_hit_vector = hit_vectors[best_index2]
            routeobs = reflec_obj_nine_obs_group[best_index1][best_index2]
            around_cue_hitpoint_detect=method_choice.edge_detect(self,best_cue_hitpoint)
            finalobs=[]
            countobs = 0
            # for i in range(self.ballcount):
            #     countobs, px, py = point_to_line_distance(self.positions[i],self.obj)
            #     if px > 0:
            # #         finalobs.append((px,py))
            # cue_obstacle=method_choice.edge_detect(best_cue_hitpoint)
            # method_choice.final(route,max_non_positive_score, hit_vector[0], hit_vector[1], routeobs, best_cue_hitpoint[0],best_cue_hitpoint[1],cue_obstacle)
            plt.plot([self.cue[0],first_hitpoint[0]],[self.cue[1],first_hitpoint[1]],linestyle='-')
            plt.plot([self.obj[0],reflection_point[0]],[self.obj[1],reflection_point[1]],linestyle='-')
            plt.plot([reflection_point[0],second_hitpoint[0]],[reflection_point[1],second_hitpoint[1]],linestyle='-')
            plt.plot([self.nine[0],best_virhole[0]],[self.nine[1],best_virhole[1]])
            screen2(self.ballcount,route,self.cue,self.obj,self.nine,self.positions)
            return max_non_positive_score,best_hit_vector[0], best_hit_vector[1], routeobs, best_cue_hitpoint[0], best_cue_hitpoint[1]
        else:
            return method_choice.method1(self)    
        
    
    def method1(self):
        route=1
        print(route)
        #--------------#
        obj_holes_dis=[]
        obj_holes_obs=[]
        cue_obj_holes_angle=[]
        method1_scores=[]
        cue_obj_vectors=[]
        #------------obs,angle---------------#
        for i in range(6):
            cue_obj_dis,cue_obj_vector=distance_and_vector(self.cue,self.obj_holes_hitpoints[i])
            cue_obj_vectors.append(cue_obj_vector)
            obj_hole_dis,_=distance_and_vector(self.obj,vir_hole_positions[i])
            obj_holes_dis.append(obj_hole_dis+cue_obj_dis)
        for i in range(6):
            cue_obj_hole_angle=vector_angle(self.cue,self.obj_holes_hitpoints[i],vir_hole_positions[i])
            cue_obj_holes_angle.append(cue_obj_hole_angle)
        for i in range(6):
            temp1obj_hole_obs=0
            for j in range(1,len(self.positions)):
                temp1obj_hole_obs,_=check_obstacle_ball(self.positions[j],self.cue,self.obj_holes_hitpoints[i],temp1obj_hole_obs)
                temp1obj_hole_obs,_=check_obstacle_ball(self.positions[j],self.obj,vir_hole_positions[i],temp1obj_hole_obs)
            obj_holes_obs.append(temp1obj_hole_obs)
            #--------------distance,score----------------#
        method1_judge=False
        negative_scores=[]
        for i in range(6):
            method1=cal_score(obj_holes_dis[i],obj_holes_obs[i],cue_obj_holes_angle[i],-1,1)
            method1_scores.append(method1)
            if method1<0:
                method1_judge=True
                negative_scores.append(method1)
       
        print(cue_obj_holes_angle)
        print(method1_scores)
        if method1_judge==True:
            max_non_positive_score = max(negative_scores)
            best_index = method1_scores.index(max_non_positive_score)
            best_score=method1_scores[best_index]
            best_virhole = vir_hole_positions[best_index]
            first_hitpoint = self.obj_holes_hitpoints[best_index]
            best_cue_hitpoint=calculate_aim_point(self.cue,first_hitpoint,radius/2)
            best_hit_vector = cue_obj_vectors[best_index]
            routeobs = obj_holes_obs[best_index]
            around_cue_hitpoint_detect=method_choice.edge_detect(self,best_cue_hitpoint)
        # method_choice.final(self,route,best_score,best_hit_vector[0],best_hit_vector[1],routeobs,best_cue_hitpoint,around_cue_hitpoint_detect)
            plt.plot(best_cue_hitpoint[0],best_cue_hitpoint[1],marker='o',ms=3,color='red')
            plt.plot([self.cue[0],first_hitpoint[0]],[self.cue[1],first_hitpoint[1]],linestyle='-',color='red')
            plt.plot([self.obj[0],best_virhole[0]],[self.obj[1],best_virhole[1]],linestyle='-',color='red')
            method_choice.final(self,route,max_non_positive_score,best_hit_vector[0],best_hit_vector[1],routeobs,best_cue_hitpoint,around_cue_hitpoint_detect)
            screen2(self.ballcount,route,self.cue,self.obj,self.nine,self.positions)
            return max_non_positive_score,-best_hit_vector[0], -best_hit_vector[1], routeobs, best_cue_hitpoint[0], best_cue_hitpoint[1]
        else:
            return method_choice.method2(self)
    def method2_1(self):
        route=2.1
        print(route)
        #--------obs,angle-------#
        obj_nines_obs=[]
        obj_nine_holes_angles=[]
        for i in range(6):
            temp1obj_nine_obs=0
            for k in range(1,self.ballcount):
                temp1obj_nine_obs,_=check_obstacle_ball(self.positions[k],self.cue,self.obj_nines_hitpoints[i],temp1obj_nine_obs)
                temp1obj_nine_obs,_=check_obstacle_ball(self.positions[k],self.obj,self.nine_holes_hitpoints[i],temp1obj_nine_obs)
                temp1obj_nine_obs,_=check_obstacle_ball(self.positions[k],self.nine,vir_hole_positions[i],temp1obj_nine_obs)
            obj_nines_obs.append(temp1obj_nine_obs)
        cue_obj_nine_reflec_diss=[]
        method2_1scores=[]
        hit_vectors=[]
        reflection_obj_nine_angles=[]
        #---------------distance-----------------#
        for j in range(4):
            cue_obj_nine_reflec_dis1=[]
            temp2reflection_obj_nine_angle=[]
            
            for i in range(6):
                cue_reflec1_dis,hit_vector=distance_and_vector(self.cue,self.reflection_obj_nine_points[j][i])
                hit_vectors.append(hit_vector)
                reflec1_obj_dis,_=distance_and_vector(self.reflection_obj_nine_points[j][i],self.nine_holes_hitpoints[i])
                obj_nine_dis,_=distance_and_vector(self.nine,self.nine_holes_hitpoints[i])
                nine_hole_dis,_=distance_and_vector(self.nine,vir_hole_positions[i])
                cue_obj_nine_reflec_dis1.append(cue_reflec1_dis+reflec1_obj_dis+obj_nine_dis+nine_hole_dis)
                temp1reflection_obj_nine=vector_angle(self.reflection_obj_nine_points[j][i],self.obj_nines_hitpoints[i],self.nine_holes_hitpoints[i])
                temp2reflection_obj_nine_angle.append(temp1reflection_obj_nine)
                temp1obj_nine_hole=vector_angle(self.obj,self.nine_holes_hitpoints[i],vir_hole_positions[i])
                obj_nine_holes_angles.append(temp1obj_nine_hole)
            reflection_obj_nine_angles.append(temp2reflection_obj_nine_angle)
            cue_obj_nine_reflec_diss.append(cue_obj_nine_reflec_dis1)
        #-------------score--------------------#
        method2_1_judge=False
        method2_1scores=[]
        print("method2_1angle",obj_nine_holes_angles)
        print("method2_1_1angle,",reflection_obj_nine_angles)
        for i in range(4):
            temp2scores=[]
            for j in range(6):
                temp1score=cal_score(cue_obj_nine_reflec_diss[i][j],obj_nines_obs[i],obj_nine_holes_angles[i],reflection_obj_nine_angles[i][j],2)
                temp2scores.append(temp1score)
            method2_1scores.append(temp2scores)
        #-------------choice---------------#
        if method2_1_judge==True:
            print(method2_1scores)
            max_non_positive_score,best_index1,best_index2=find_min_negative_integer_in_nested_list(method2_1scores)
            best_virhole = vir_hole_positions[best_index2]
            reflection_point = self.reflection_obj_nine_points[best_index1][best_index2]
            first_hitpoint = self.obj_holes_hitpoints[best_index2]
            best_cue_hitpoint=calculate_aim_point(self.cue,first_hitpoint,radius/2)
            best_hit_vector = hit_vectors[best_index2]
            routeobs = obj_nines_obs[best_index2]
            around_cue_hitpoint_detect=method_choice.edge_detect(self,best_cue_hitpoint)
            plt.plot(best_cue_hitpoint[0],best_cue_hitpoint[1],marker='o',ms=3,color='red')
            plt.plot([self.cue[0],reflection_point[0]],[self.cue[1],reflection_point[1]],linestyle='-',color='red')
            plt.plot([reflection_point[0],first_hitpoint[0]],[reflection_point[1],first_hitpoint[1]],linestyle='-',color='red')
            plt.plot([self.obj[0],best_virhole[0]],[self.obj[1],best_virhole[1]],linestyle='-',color='red')
            method_choice.final(self,route,max_non_positive_score,best_hit_vector[0],best_hit_vector[1],routeobs,best_cue_hitpoint,around_cue_hitpoint_detect)
            screen2(self.ballcount,route,self.cue,self.obj,self.nine,self.positions)
            return max_non_positive_score,hit_vector[0], hit_vector[1], routeobs, best_cue_hitpoint[0], best_cue_hitpoint[1]
        else:
            
            return method_choice.method2(self)   
        
    def method2(self): 
        route=2
        print(route)
        #-------------------#
        obj_holes_obs=[]
        cue_obj_holes_angle=[]
        method2_scores=[]
        hit_vectors=[]
        cue_relfec_obj_hole_diss=[]
        method2=False
        #------------------obs,angle--------------------#
        for j in range(4):
            temp2cue_obj_holes_angle=[]
            for i in range(6):
                temp1cue_obj_hole_angle=vector_angle(self.reflection_obj_points[j][i],self.obj_holes_hitpoints[i],vir_hole_positions[i])
                temp2cue_obj_holes_angle.append(temp1cue_obj_hole_angle)
            cue_obj_holes_angle.append(temp2cue_obj_holes_angle)
        print("method2",cue_obj_holes_angle)
        #------------------distance,score--------#
        cue_relfec_obj_hole_diss2=[]
        for i in range(4):
            cue_relfec_obj_hole_diss1=[]
            temp1hit_vectors=[]
            for j in range(6):
                cue_reflec1_dis,cue_reflec1_vector=distance_and_vector(self.cue,self.reflection_obj_points[i][j])
                temp1hit_vectors.append(cue_reflec1_vector)
                reflec1_obj_dis,_=distance_and_vector(self.reflection_obj_points[i][j],self.obj_holes_hitpoints[j])
                obj_hole_dis,_=distance_and_vector(self.obj,vir_hole_positions[j])
                cue_relfec_obj_hole_dis=(cue_reflec1_dis+reflec1_obj_dis+obj_hole_dis)
                cue_relfec_obj_hole_diss1.append(cue_relfec_obj_hole_dis)
            cue_relfec_obj_hole_diss2.append(cue_relfec_obj_hole_diss1)
            hit_vectors.append(temp1hit_vectors)
        
        for i in range(4):
            for k in range(6):
                temp1obs=0
                for j in range(1,self.ballcount):
                    temp1obs,_=check_obstacle_ball(self.positions[j],self.cue,self.reflection_obj_points[i][k],temp1obs)
                    temp1obs,_=check_obstacle_ball(self.positions[j],self.reflection_obj_points[i][k],self.obj,temp1obs)
                    temp1obs,_=check_obstacle_ball(self.positions[j],self.obj,vir_hole_positions[k],temp1obs)
                obj_holes_obs.append(temp1obs)
                # if temp1obs==0 and cue_obj_holes_angle[k] <= 90:
                #     method2=True
        method2=False
        method2_scores2=[]
        for i in range(4):
            method2_scores=[]
            for j in range(6):
                method2_score=cal_score(cue_relfec_obj_hole_diss2[i][j],obj_holes_obs[j],cue_obj_holes_angle[i][j],-1,1)
                method2_scores.append(method2_score)
            method2_scores2.append(method2_scores)
        max_non_positive_score,best_index1,best_index2=find_min_negative_integer_in_nested_list(method2_scores2)
        print(method2_scores2)
        #-------------choice---------------#
        if max_non_positive_score:
            best_virhole = vir_hole_positions[best_index2]
            reflection_point = self.reflection_obj_points[best_index1][best_index2]
            first_hitpoint = self.obj_holes_hitpoints[best_index2]
            best_cue_hitpoint=calculate_aim_point(self.cue,reflection_point,radius/2)
            best_hit_vector = hit_vectors[best_index1][best_index2]
            routeobs = obj_holes_obs[best_index2]
            around_cue_hitpoint_detect=method_choice.edge_detect(self,best_cue_hitpoint)
            plt.plot(best_cue_hitpoint[0],best_cue_hitpoint[1],marker='o',ms=3,color='red')
            plt.plot([self.cue[0],reflection_point[0]],[self.cue[1],reflection_point[1]],linestyle='-',color='red')
            plt.plot([reflection_point[0],first_hitpoint[0]],[reflection_point[1],first_hitpoint[1]],linestyle='-',color='red')
            plt.plot([self.obj[0],best_virhole[0]],[self.obj[1],best_virhole[1]],linestyle='-',color='red')
            method_choice.final(self,route,max_non_positive_score,best_hit_vector[0],best_hit_vector[1],routeobs,best_cue_hitpoint,around_cue_hitpoint_detect)
            screen2(self.ballcount,route,self.cue,self.obj,self.nine,self.positions)
            return max_non_positive_score,best_hit_vector[0], best_hit_vector[1], around_cue_hitpoint_detect, best_cue_hitpoint[0], best_cue_hitpoint[1]
        else:
            return method_choice.method3(self)
    def method3(self):
        route=3
        print(route)
        method3_judge=False
        method3obs=[]
        method3dis=[]
        method3angle=[]
        method3_1angle=[]
        method3vector=[]
        for i in range(1,self.ballcount-1):
            temp2obs=[]
            temp2dis=[]
            temp2angle=[]
            temp2_1angle=[]
            temp2vector=[]
            for j in range(6):
                temp1dis,temp1vector=distance_and_vector(self.cue,self.others_hitpoints[i][j])
                temp1_1dis,_=distance_and_vector(self.obj,self.cue_obj_others_hitpoints[i][j])
                temp1_2dis,_=distance_and_vector(self.positions[i],vir_hole_positions[j])
                temp2dis.append(temp1_1dis+temp1_2dis+temp1dis)
                temp1angle=vector_angle(self.cue,self.cue_obj_others_hitpoints[i][j],self.others_hitpoints[i][j])
                temp1_1angle=vector_angle(self.cue_obj_others_hitpoints[i][j],self.others_hitpoints[i][j],vir_hole_positions[j])
                temp2_1angle.append(temp1_1angle)
                temp2angle.append(temp1angle)
                temp1obs=0
                for k in range(len(self.positions)):
                    temp1obs,_=check_obstacle_ball(self.positions[k],self.cue,self.cue_obj_others_hitpoints[i][j],temp1obs)
                    temp1obs,_=check_obstacle_ball(self.positions[k],self.obj,self.others_hitpoints[i][j],temp1obs)
                    temp1obs,_=check_obstacle_ball(self.positions[k],self.positions[i],vir_hole_positions[j],temp1obs)
                if temp1obs==0:
                    method3_judge=True
                temp2obs.append(temp1obs)
                temp2vector.append(temp1vector)
            method3vector.append(temp2vector)
            method3angle.append(temp2angle)
            method3obs.append(temp2obs)
            method3dis.append(temp2dis)
            method3_1angle.append(temp1_1angle)
        print("obs3",method3obs)
        print("dis3",method3dis)
        print("angle",method3angle)
        if method3_judge==False:
            return method_choice.method3_2(self)
        method3socre=[]
        temp1score_negative=[]
        method3_judge=False
        for i in range(0,self.ballcount-2):
            temp2socre=[]
            for j in range(6):
                temp1score=cal_score(method3dis[i][j],method3obs[i][j],method3angle[i][j],method3_1angle[i][j],2)
                if temp1score<0:
                    method3_judge=True
                    
                temp2socre.append(temp1score)
            method3socre.append(temp2socre)
        if method3_judge==True:
            max_non_positive_score,best_index1,best_index2=find_min_negative_integer_in_nested_list(method3socre)
            print(best_index1,best_index2)
            best_virhole = vir_hole_positions[best_index2]
            first_hitpoint = self.cue_obj_others_hitpoints[best_index1][best_index2]
            second_hitpoint = self.others_hitpoints[best_index1][best_index2]
            third_obj=self.positions[best_index1]
            best_hit_vector = method3vector[best_index1][best_index2]
            routeobs = method3obs[best_index1][best_index2]
            hitcuepoint = calculate_aim_point(self.cue,first_hitpoint, radius/2)
            finalobs=[]
            countobs = 0
            # for i in range(self.ballcount):
            #     countobs, px, py = point_to_line_distance(self.positions[i],self.obj)
            #     if px > 0:
            #         finalobs.append((px,py))
            cue_obstacle=method_choice.edge_detect(self,hitcuepoint)
            #----------screen-----------#
            around_cue_hitpoint_detect=method_choice.edge_detect(self,hitcuepoint)
            plt.plot([self.cue[0],first_hitpoint[0]],[self.cue[1],first_hitpoint[1]],linestyle='-')
            plt.plot([self.obj[0],second_hitpoint[0]],[self.obj[1],second_hitpoint[1]],linestyle='-')
            plt.plot([third_obj[0],best_virhole[0]],[third_obj[1],best_virhole[1]])
            for i in range(0,self.ballcount-2):
                for j in range(6):
                    plt.plot(self.cue_obj_others_hitpoints[i][j][0],self.cue_obj_others_hitpoints[i][j][1],marker='o',ms=3,color='yellow')
            method_choice.final(self,route,max_non_positive_score,best_hit_vector[0],best_hit_vector[1],routeobs,hitcuepoint,around_cue_hitpoint_detect)
            screen2(self.ballcount,route,self.cue,self.obj,self.nine,self.positions)
            return max_non_positive_score,-best_hit_vector[0], -best_hit_vector[1], around_cue_hitpoint_detect, hitcuepoint[0], hitcuepoint[1]
        
        else:
            return method_choice.method3_2(self)
        
        
    def method3_2(self):
        route=3.2
        print(route)
        method3_2=False
        method3_2_obs=[]
        for i in range(1,self.ballcount-1):
            temp2=[]
            for j in range(6):
                temp1=0
                for k in range(1,len(self.positions)-1):
                    temp1,_=check_obstacle_ball(self.positions[j],self.cue,self.cue_obj_others_hitpoints[i][j],temp1)
                temp2.append(temp1)
                if temp1==0:
                    method3_2=True
            method3_2_obs.append(temp2)
        print("method3_2",method3_2_obs)
        if method3_2==True:
            
            
            method3_2_dis=[]
            method3_2_vector=[]
            method3_2_angle=[]
            method3_2_obs=[]
            method3_2_reflection_point=[]
            method3_2_1angle=[]
            for i in range(4):
                for j in range(self.ballcount):
                    temp2reflection_point=[]
                    for k in range(6):  
                        mirror_obj_part=mirror_point(self.slope[i],self.wall_side[i],self.cue_obj_others_hitpoints[j][k])
                        temp1reflection_point=segment_intersection(*self.boundaries[i],mirror_obj_part[0],mirror_obj_part[1])
                        temp2reflection_point.append(temp1reflection_point)
                    method3_2_reflection_point.append(temp2reflection_point)
            for i in range(0,self.ballcount-2):
                temp2dis=[]
                temp2vector=[]
                temp2angle=[]
                temp2_1angle=[]
                temp2obs=[]
                temp2reflection_point=[]
                method3_2_judge=False
                for j in range(6):
                    temp1dis,temp1vector=distance_and_vector(self.cue,self.cue_obj_others_hitpoints[i][j])
                    temp1_1dis,_=distance_and_vector(self.obj,self.others_hitpoints[i][j])
                    temp1_2dis,_=distance_and_vector(self.positions[i],vir_hole_positions[j])
                    temp_dis_sum=temp1_1dis+temp1_2dis+temp1dis
                    temp1_1angle=vector_angle(method3_2_reflection_point[i][j],self.cue_obj_others_hitpoints[i][j],self.others_hitpoints[i][j])
                    temp1_angle=vector_angle(self.cue_obj_others_hitpoints[i][j],self.others_hitpoints[i][j],vir_hole_positions[j])
                    temp2angle.append(temp1_angle)
                    temp2_1angle.append(temp1_1angle)
                    temp2dis.append(temp_dis_sum)
                    temp2vector.append(temp1vector)
                    temp1obs=0
                    for k in range(1,len(self.positions)-1):
                        temp1obs,_=check_obstacle_ball(self.positions[k],self.cue,method3_2_reflection_point[i][j],temp1obs)
                        temp1obs,_=check_obstacle_ball(self.positions[k],method3_2_reflection_point[i][j],self.others_hitpoints[i][j],temp1obs)
                        temp1obs,_=check_obstacle_ball(self.positions[k],self.obj,self.cue_obj_others_hitpoints[i][j],temp1obs)
                        temp1obs,_=check_obstacle_ball(self.positions[k],self.positions[i],vir_hole_positions[j],temp1obs)
                    temp2obs.append(temp1obs)
                    # if temp1obs==0:
                    #     method3_2_judge=True
                method3_2_1angle.append(temp2_1angle)
                method3_2_reflection_point.append(temp2reflection_point)
                method3_2_obs.append(temp2obs)
                method3_2_vector.append(temp2vector)
                method3_2_dis.append(temp2dis)
                method3_2_angle.append(temp2angle)
            # print("method3_2",method3_2_obs)
            # if method3_2_judge==False:
            #     print("false")
            #     screen2(self.ballcount,route,cuex,cuey,self.obj,self.nine)
            #     return False
            method3_2_judge=False
            method3_2score=[]
            for i in range(0,self.ballcount-2):
                temp2score=[]
                for j in range(6):
                    temp1score=cal_score(method3_2_dis[i][j],method3_2_obs[i][j],method3_2_angle[i][j],method3_2_1angle[i][j],2)
                    if temp1score <0:
                        method3_2_judge=True
                    temp2score.append(temp1score)
                method3_2score.append(temp2score)
            
            if method3_2_judge==True:
                print("3.2",True)
                max_non_positive_score,best_index1,best_index2=find_min_negative_integer_in_nested_list(method3_2score)
                print(best_index1,best_index2)
                best_virhole = vir_hole_positions[best_index2]
                reflection_point = method3_2_reflection_point[best_index1][best_index2]
                first_hitpoint = self.cue_obj_others_hitpoints[best_index1][best_index2]
                second_hitpoint = self.others_hitpoints[best_index1][best_index2]
                third_ball=self.positions[best_index1]
                best_cue_hitpoint=calculate_aim_point(self.cue,reflection_point,radius/2)
                best_hit_vector = method3_2_vector[best_index1][best_index2]
                routeobs = method3_2_obs[best_index2]
                around_cue_hitpoint_detect=method_choice.edge_detect(self,best_cue_hitpoint)
                
                plt.plot(best_cue_hitpoint[0],best_cue_hitpoint[1],marker='o',ms=3,color='red')
                plt.plot([self.cue[0],reflection_point[0]],[self.cue[1],reflection_point[1]],linestyle='-',color='red')
                plt.plot([reflection_point[0],first_hitpoint[0]],[reflection_point[1],first_hitpoint[1]],linestyle='-',color='red')
                plt.plot([self.obj[0],second_hitpoint[0]],[self.obj[1],second_hitpoint[1]],linestyle='-',color='red')
                plt.plot([third_ball[0],best_virhole[0]],[third_ball[1],best_virhole[1]],linestyle='-',color='red')
                method_choice.final(self,route,max_non_positive_score,best_hit_vector[0],best_hit_vector[1],routeobs,best_cue_hitpoint,around_cue_hitpoint_detect)
                screen2(self.ballcount,route,self.cue,self.obj,self.nine,self.positions)
                return max_non_positive_score,best_hit_vector[0], best_hit_vector[1], around_cue_hitpoint_detect, best_cue_hitpoint[0], best_cue_hitpoint[1]
            else:
                print("false")
                screen2(self.ballcount,route,self.cue,self.obj,self.nine,self.positions)
                # return False
if __name__== '__main__':
    balls=[]
    ballcount=8
    #def generate the ball
    cuex, cuey, ballx_set, bally_set, ball_count=generate_balls(ballcount,radius)
    print(ballx_set)
    print(bally_set)
    # ballcount+=1
    print("self.ballcount",ballcount)
    main=method_choice(ballx_set,bally_set,ballcount,cuex,cuey)
    main.main()
