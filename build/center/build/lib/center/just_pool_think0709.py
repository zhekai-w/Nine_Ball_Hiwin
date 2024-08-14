import random
import math
import sys
import time 
import numpy as np
import matplotlib.pyplot as plt
 
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
x1 = 100
y1 = 100
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

def distance_and_vector(point1,point2):
    n1x,n1y=point1
    n2x,n2y=point2
    dx = n1x - n2x
    dy = n1y - n2y
    dist = math.sqrt(dx ** 2 + dy ** 2)
    return round(dist, 2), dx, dy

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

def generate_balls(ball_count, radius):
    cuex = random.randint(x1 + radius, x1 + width - radius)
    cuey = random.randint(y1 + radius, y1 + height - radius)
    ball_positions = []

    while len(ball_positions) <= ballcount+1:
        x = random.randint(x1 + radius, x1 + width - radius)
        y = random.randint(y1 + radius, y1 + height - radius)
        if not is_overlapping(x, y,cuex,cuey, ball_positions, radius):
            ball_positions.append((x, y))

    ballx_set = [pos[0] for pos in ball_positions]
    bally_set = [pos[1] for pos in ball_positions]

    return cuex, cuey, ballx_set, bally_set, ball_count
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

def point_to_line_distance(obs_ball, obj_point, target_point, i, obs_value):
    x1, y1 = obj_point
    x2, y2 = target_point
    px, py = obs_ball
    dx = x2 - x1
    dy = y2 - y1
    apx = px - x1
    apy = py - y1
    d_mag_squared = dx ** 2 + dy ** 2
    
    if d_mag_squared == 0:  # 线段退化为一个点
        dist = math.sqrt(apx ** 2 + apy ** 2)
    else:
        t = (apx * dx + apy * dy) / d_mag_squared
        
        if t < 0:
            closest_x, closest_y = x1, y1
        elif t > 1:
            closest_x, closest_y = x2, y2
        else:
            closest_x = x1 + t * dx
            closest_y = y1 + t * dy
        
        dist = math.sqrt((px - closest_x) ** 2 + (py - closest_y) ** 2)
        # plt.plot([cuex,first_hitpoint[0]],[cuey,first_hitpoint[1]],linestyle='-')
    # if temp==1:
    #     plt.plot([px,closest_x],[py,closest_y],linestyle='-')
    if dist < 3.1*radius:
        obs_value += 1
        return obs_value, i, py
    return obs_value, 0, 0

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

def cal_score(distance, angle, obj_holeobs):
    score = ((angle * 22) + (distance * -1) + (obj_holeobs * -4000))
    if angle > 0:
        score = abs(score)
    return score


def mirror_point(line_m, line_b, point):
    x1,y1=(point)
    if line_m == 'inf':  # 直线垂直的情况
        x2 = line_b  # 这里 line_b 是 x 的值
        y2 = y1
    else:
        # 计算交点
        x2 = (line_m * (y1 - line_b) + x1) / (line_m**2 + 1)
        y2 = (line_m * x2 + line_b)
    
    # 计算镜像点
    x_mirror = 2 * x2 - x1
    y_mirror = 2 * y2 - y1
    
    return (x_mirror, y_mirror)

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

    
def screen2(ballcount,routenumber,cuex,cuey,obj,nine):
    plt.title('Basic Plot in Matplotlib')
    plt.xlabel('X Axis Label')
    plt.ylabel('Y Axis Label')
    plt.grid()
    plt.plot([holex[0],holex[2]],[holey[0],holey[2]],[holex[2],holex[5]],[holey[2],holey[5]],
             [holex[5],holex[3]],[holey[5],holey[3]],[holex[3],holex[0]],[holey[3],holey[0]],color='black')
    # for i in range(linecount):
    #    plt.plot((lines[i],lines[i+2]),(lines[i+1],lines[i+3]), linestyle = '-') 
    plt.plot(obj[0],obj[1],marker='o',ms=radius,color='yellow')
    plt.plot(cuex,cuey,marker='o',ms=radius,color='red')
    plt.plot(nine[0],nine[1],marker='o',ms=radius,color='pink')
    for i in range(1,ballcount-1):
        plt.plot(ballx_set[i],bally_set[i],marker='o',ms=radius,color='blue')
    for i in range(6):
        plt.plot(hole_positions[i][0],hole_positions[i][1],marker = 'o',ms=holeradius,color='black')
        plt.plot(vir_hole_positions[i][0],vir_hole_positions[i][1],marker = 'o',ms=holeradius,color='black')
        # plt.plot(obj_hitpoints[i],marker = 'o',ms=3,color='green')
        # plt.plot(nine_hitpoints[i],marker = 'o',ms=3,color='green')
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
        self.positions = [(ballx_set[i], bally_set[i]) for i in range(ballcount+1)]
        self.boundaries = [
        (x1,y1,x1+width,y1,cuex,cuey),  # top
        (x1,y1+height,x1+width,y1+height,cuex,cuey),  # bottom
        (x1,y1,x1,y1+height,cuex,cuey),  # left
        (x1+width,y1,x1+width,y1+height,cuex,cuey)  # right
        ]
        self.slope=[0,0,'inf','inf']
        self.wall_side=[x1,x1+height,y1,y1+width]
        
    def edge_detect(self,best_cue_hitpoint):
        hitcuepointx,hitcuepointy=best_cue_hitpoint
        cue_obstacle=0
        if hitcuepointx - radius < x1 or hitcuepointx + radius > x1 + width or hitcuepointy - radius < y1 or hitcuepointy + radius > y1 + height:
            return True
        for i in range(ballcount):
            cue_obstacle,_,_=point_to_line_distance(self.positions[i],self.cue,best_cue_hitpoint,i,cue_obstacle)
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
        #-------------------hitpoint--------------#
        print(self.positions)
        self.obj_holes_hitpoints = []
        self.nine_holes_hitpoints = []
        self.obj_nines_hitpoints=[]
        for i in range(6):
            objhitpoint = calculate_aim_point(self.obj, vir_hole_positions[i], radius)
            ninehitpoint =calculate_aim_point(self.nine,vir_hole_positions[i], radius)
            obj_nines_hitpoint=calculate_aim_point(self.obj,ninehitpoint,radius)
            self.obj_holes_hitpoints.append(objhitpoint)
            self.nine_holes_hitpoints.append(ninehitpoint)
            self.obj_nines_hitpoints.append(obj_nines_hitpoint)
        self.cue_obj_others_hitpoints=[]
        self.others_hitpoints=[]
        for i in range(1,ballcount):
            cue_obj_other_hitpoints=[]
            other_hitpoints=[]
            for j in range(6):
                other_hitpoint=calculate_aim_point(self.positions[i],vir_hole_positions[j],radius)
                other_hitpoints.append(other_hitpoint)
                cue_obj_other_hitpoint=calculate_aim_point(self.obj,other_hitpoint,radius)
                cue_obj_other_hitpoints.append(cue_obj_other_hitpoint)
            self.cue_obj_others_hitpoints.append(cue_obj_other_hitpoints)
            self.others_hitpoints.append(other_hitpoints)
        print(self.cue_obj_others_hitpoints)
        #---------angle,obs==>method judge----------#
        cue_obj_obstacles1 = []
        self.cue_obj_nines_angle=[]
        method1_1=False
        method1=False
        method2_1=False
        method2=False
        #--------------method1 judge-------------#
        for i in range(6):
            cue_obj_obstacle1 = 0
            cue_obj_nine_angle=vector_angle(self.cue,self.obj,self.nine_holes_hitpoints[i])
            self.cue_obj_nines_angle.append(cue_obj_nine_angle)
            for j in range(1,ballcount):
                cue_obj_obstacle1, _, _ = point_to_line_distance(self.positions[j],self.cue,self.obj_holes_hitpoints[i],1,cue_obj_obstacle1)
            cue_obj_obstacles1.append(cue_obj_obstacle1)
        for i in range(6):
            if cue_obj_obstacles1[i] ==0 and self.cue_obj_nines_angle[i] <=0:
                method1_1=True
            if cue_obj_obstacles1[i]==0:
                method1=True
        #------------method2 judge--------------#
        print("first_route_choice",self.cue_obj_nines_angle,cue_obj_obstacles1,method1_1)
        print("first_route_straight",cue_obj_obstacles1,method1)
        print("radius",radius)
        self.reflection_obj_points_group=[]
        for i in range(4):
            reflection_obj_points=[]
            for j in range(6):
                mirror_obj_part=mirror_point(self.slope[i],self.wall_side[i],self.obj_holes_hitpoints[j])
                reflection_obj_point=segment_intersection(*self.boundaries[i],mirror_obj_part[0],mirror_obj_part[1])
                reflection_obj_points.append(reflection_obj_point)
            self.reflection_obj_points_group.append(reflection_obj_points)
        reflection_obj_nines_angles=[]
        cue_reflection_obj_angles=[]
        for i in range(4):
            temp1=[]
            temp2=[]
            for j in range(6):
                reflection_obj_nines_angle=vector_angle(self.reflection_obj_points_group[i][j],self.obj_nines_hitpoints[j],self.nine_holes_hitpoints[j])
                cue_reflection_obj_angle=vector_angle(self.cue,self.reflection_obj_points_group[i][j],self.obj_nines_hitpoints[j])
                temp1.append(reflection_obj_nines_angle)
                temp2.append(cue_reflection_obj_angle)
            reflection_obj_nines_angles.append(temp1)
            cue_reflection_obj_angles.append(temp2)
        self.cue_obj_nines_obs2=[]
        for i in range(4):
            cue_obj_nines_obs1=[]
            for j in range(6):
                cue_obj_nines_obs=0
                for k in range(1,ballcount):
                    cue_obj_nines_obs,_,_=point_to_line_distance(self.positions[k],self.cue,self.reflection_obj_points_group[i][j],2*radius,cue_obj_nines_obs)
                    cue_obj_nines_obs,_,_=point_to_line_distance(self.positions[k],self.reflection_obj_points_group[i][j],self.obj_holes_hitpoints[j],2*radius,cue_obj_nines_obs)
                cue_obj_nines_obs1.append(cue_obj_nines_obs)
            self.cue_obj_nines_obs2.append(cue_obj_nines_obs1)
        print(self.cue_obj_nines_obs2)
        for i in range(4):
            for j in range(6):
                if reflection_obj_nines_angles[i][j] <= 0 and cue_reflection_obj_angles[i][j] <= 0 and self.cue_obj_nines_obs2[i][j]==0 : 
                    method2_1=False
                if self.cue_obj_nines_obs2[i][j]==0:
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

    # def striagt_cal(self,obj,target,obs1,obs2,angle,dis):
        
        
    def method1_1(self):
        route=1.1
        print(route)
        #--------obs,angle----------#
        obj_nine_hole_obss=[]
        cue_hole_dis=[]
        self.route=route
        obj_nine_hitpoints=[]
        method1_1=False
        #--------obs----------#
        
        for i in range(6):
            obj_nine_hole_hitpoint_obs=0
            for j in range(1,ballcount-1):
                obj_nine_hole_hitpoint_obs,_,_= point_to_line_distance(self.positions[j],self.obj,self.obj_nines_hitpoints[i],2*radius,obj_nine_hole_hitpoint_obs)
                obj_nine_hole_hitpoint_obs,_,_ = point_to_line_distance(self.positions[j],self.nine,vir_hole_positions[i],2*radius,obj_nine_hole_hitpoint_obs)
                obj_nine_hole_obss.append(obj_nine_hole_hitpoint_obs)
        #--------judge------#
            if obj_nine_hole_obss==0:
                method1_1=True
        if method1_1==False:
            return method_choice.method1_2(self)
        #-----distance,score-----#
        cue_hole_diss=[]
        scores1_1=[]
        hit_vectors=[]
        for i in range(6):
            cue_objs_dis,vx,vy= distance_and_vector(self.cue,self.obj_nines_hitpoints[i])
            obj_nines_dis,_,_=distance_and_vector(self.obj,self.nine_holes_hitpoints[i])
            nine_holes_dis,_,_=distance_and_vector(self.nine,vir_hole_positions[i])
            cue_hole_diss.append(cue_objs_dis+obj_nines_dis,nine_holes_dis)
            hit_vector = (vx,vy)
            hit_vectors.append(hit_vector)
            cue_obj_nine_angle=vector_angle(self.cue,self.obj_nines_hitpoints[i],self.nine_holes_hitpoints[i])
            score1_1=cal_score(cue_hole_diss[i],cue_obj_nine_angle,obj_nine_hole_obss[i])
            scores1_1.append(score1_1)
            if score1_1<0:
                print(score1_1)
        non_positive_scores = [score for score in scores1_1 if score <= 0]
        if non_positive_scores:
            max_non_positive_score = max(non_positive_scores)
            best_index = scores1_1.index(max_non_positive_score)
            best_virhole = vir_hole_positions[best_index]
            first_hitpoint = self.obj_nines_hitpoints[best_index]
            second_hitpoint = self.nine_holes_hitpoints[best_index]
            best_hit_vector = hit_vectors[best_index]
            routeobs = obj_nine_hole_obss[best_index]
            hitcuepointx, hitcuepointy = calculate_aim_point(cuex, cuey, first_hitpoint[0], first_hitpoint[1], radius)
            finalobs=[]
            countobs = 0
            for i in range(ballcount):
                countobs, px, py = point_to_line_distance(self.positions[i],self.obj)
                if px > 0:
                    finalobs.append((px,py))
            cue_obstacle=method_choice.edge_detect(hitcuepointx,hitcuepointy)
            #----------screen-----------#
            method_choice.final(route,max_non_positive_score, hit_vector[0], hit_vector[1], routeobs, hitcuepointx, hitcuepointy,cue_obstacle)
            plt.plot([cuex,first_hitpoint[0]],[cuey,first_hitpoint[1]],linestyle='-')
            plt.plot([self.obj[0],second_hitpoint[0]],[self.obj[1],second_hitpoint[1]],linestyle='-')
            plt.plot([self.nine[0],best_virhole[0]],[self.nine[1],best_virhole[1]])
            screen2(ballcount,route,cuex,cuey,self.obj,self.nine)
            return max_non_positive_score,best_hit_vector[0], best_hit_vector[1], routeobs, hitcuepointx, hitcuepointy
        else:
            return method_choice.method1_2(self)

    def method1_2(self):
        route=1.2
        print(route)
        method1_2= False
        #---------------#
        reflection_obj_points_group=[]
        obj_nine_holes_angles=[]
        reflec_obj_nine_obs_group=[]
        #----------cal reflection point-------------#
        for i in range(4):
            reflection_obj_nines_point=[]
            reflection_obj_nine_obs=[]
            for j in range(6):
                mirror_obj_part=mirror_point(self.slope[i],self.wall_side[i],self.nine_holes_hitpoints[j])
                reflection_obj_nine_point=segment_intersection(*self.boundaries[i],mirror_obj_part[0],mirror_obj_part[1])
                reflection_obj_nines_point.append(reflection_obj_nine_point)
            reflection_obj_points_group.append(reflection_obj_nines_point)
                # obj_nine_hole_angle=vector_angle(reflection_obj_nine_point,self.nine_holes_hitpoints[j],vir_hole_positions[j])
                # obj_nine_holes_angles.append(obj_nine_hole_angle)
        for i in range(4):
            for j in range(6):
                reflec_obj_nine_obs=0
                for k in range(1,ballcount):
                    reflec_obj_nine_obs,_,_=point_to_line_distance(self.positions[k],self.obj,reflection_obj_points_group[i][j],2*radius,reflec_obj_nine_obs)
                    reflec_obj_nine_obs,_,_=point_to_line_distance(self.positions[k],reflection_obj_points_group[i][j],vir_hole_positions[j],2*radius,reflec_obj_nine_obs)
                reflec_obj_nine_obs_group.append(reflection_obj_nine_obs)
        #----------obs、angle----------------------#
        reflection_obj_nine_angles=[]
        for i in range(4):
            for j in range(6):
                reflection_obj_nine_angle=vector_angle(reflection_obj_points_group[i][j],self.obj_nines_hitpoints[j],self.nine_holes_hitpoints[j])
                reflection_obj_nine_angles.append(reflection_obj_nine_angle)
        for i in range(4):
            for j in range(6):
                if reflec_obj_nine_obs_group[j]==0 and reflection_obj_nine_angles[i][j] <= 0:
                    method1_2=True
            reflection_obj_nine_obs.append(reflec_obj_nine_obs)
            
            
        print("reflection",reflection_obj_points_group)
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
                cue_reflect_dis,vx,vy=distance_and_vector(self.cue,self.reflection_obj_points_group[i][j])
                hit_vector=(vx,vy)
                hit_vectors.append(hit_vector)
                reflect_obj_dis,_,_=distance_and_vector(reflection_obj_points_group[i][j],self.nine_holes_hitpoints[j])
                obj_nine_dis,_,_=distance_and_vector(self.obj,self.obj_nines_hitpoints[j])
                nine_hole_dis,_,_=distance_and_vector(self.nine,vir_hole_positions[j])
                method1_2_dis=cue_reflect_dis+reflect_obj_dis+obj_nine_dis+nine_hole_dis
                method1_2_diss1.append(method1_2_dis)
            method1_2_diss2.append(method1_2_diss1)
        method1_2scores2=[]
        for i in range(4):
            method1_2scores=[]
            for j in range(6):
                method1_2score=cal_score(method1_2_diss2[i][j],obj_nine_holes_angles[j],reflec_obj_nine_obs_group[i][j])
                method1_2scores.append(method1_2score)
            method1_2scores2.append(method1_2scores)
        max_non_positive_score,best_index1,best_index2=find_min_negative_integer_in_nested_list(method1_2scores2)
        #-------------choice---------------#
        if max_non_positive_score:
            best_virhole = vir_hole_positions[best_index2]
            reflection_point = self.reflection_obj_points_group[best_index1][best_index2]
            first_hitpoint = self.obj_holes_hitpoints[best_index2]
            second_hitpoint = self.nine_holes_hitpoints[best_index2]
            best_cue_hitpoint=calculate_aim_point(self.cue,first_hitpoint,radius)
            best_hit_vector = hit_vectors[best_index2]
            routeobs = reflec_obj_nine_obs_group[best_index1][best_index2]
            around_cue_hitpoint_detect=method_choice.edge_detect(self,best_cue_hitpoint)
            finalobs=[]
            countobs = 0
            # for i in range(ballcount):
            #     countobs, px, py = point_to_line_distance(self.positions[i],self.obj)
            #     if px > 0:
            # #         finalobs.append((px,py))
            # cue_obstacle=method_choice.edge_detect(best_cue_hitpoint)
            # method_choice.final(route,max_non_positive_score, hit_vector[0], hit_vector[1], routeobs, best_cue_hitpoint[0],best_cue_hitpoint[1],cue_obstacle)
            plt.plot([cuex,first_hitpoint[0]],[cuey,first_hitpoint[1]],linestyle='-')
            plt.plot([self.obj[0],reflection_point[0]],[self.obj[1],reflection_point[1]],linestyle='-')
            plt.plot([reflection_point[0],second_hitpoint[0]],[reflection_point[1],second_hitpoint[1]],linestyle='-')
            plt.plot([self.nine[0],best_virhole[0]],[self.nine[1],best_virhole[1]])
            screen2(ballcount,route,cuex,cuey,self.obj,self.nine)
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
        hit_vectors=[]
        negative=False
        #------------obs,angle---------------#
        for i in range(6):
            cue_obj_dis,vx,vy=distance_and_vector(self.cue,self.obj_holes_hitpoints[i])
            hit_vector=(vx,vy)
            hit_vectors.append(hit_vector)
            obj_hole_dis,_,_=distance_and_vector(self.obj,vir_hole_positions[i])
            obj_holes_dis.append(obj_hole_dis+cue_obj_dis)
        for i in range(6):
            cue_obj_hole_angle=vector_angle(self.cue,self.obj_holes_hitpoints[i],vir_hole_positions[i])
            cue_obj_holes_angle.append(cue_obj_hole_angle)
        for i in range(6):
            obj_hole_obs=0
            for j in range(1,ballcount):
                obj_hole_obs,_,_=point_to_line_distance(self.positions[j],self.obj,vir_hole_positions[i],2*radius,obj_hole_obs)
            obj_holes_obs.append(obj_hole_obs)
            #--------------distance,score----------------#
        negative_scores =[]
        for i in range(6):
            method1=cal_score(obj_holes_dis[i],cue_obj_holes_angle[i],obj_holes_obs[i])
            method1_scores.append(method1)
            if method1<=0:
                negative=True
        print(cue_obj_holes_angle)
        print(method1_scores)
        if negative==True:
            max_non_positive_score = max(non_positive_scores)
            best_index = method1_scores.index(max_non_positive_score)
            best_score=method1_scores[best_index]
            best_virhole = vir_hole_positions[best_index]
            first_hitpoint = self.obj_holes_hitpoints[best_index]
            best_cue_hitpoint=calculate_aim_point(self.cue,first_hitpoint,radius)
            best_hit_vector = hit_vectors[best_index]
            routeobs = obj_holes_obs[best_index]
            around_cue_hitpoint_detect=method_choice.edge_detect(self,best_cue_hitpoint)
        # method_choice.final(self,route,best_score,best_hit_vector[0],best_hit_vector[1],routeobs,best_cue_hitpoint,around_cue_hitpoint_detect)
            plt.plot(best_cue_hitpoint[0],best_cue_hitpoint[1],marker='o',ms=3,color='red')
            plt.plot([cuex,first_hitpoint[0]],[cuey,first_hitpoint[1]],linestyle='-',color='red')
            plt.plot([self.obj[0],best_virhole[0]],[self.obj[1],best_virhole[1]],linestyle='-',color='red')
            screen2(ballcount,route,cuex,cuey,self.obj,self.nine)
            return max_non_positive_score,hit_vector[0], hit_vector[1], routeobs, best_cue_hitpoint[0], best_cue_hitpoint[1]
        else:
            return method_choice.method2(self)
    def method2_1(self):
        route=2.1
        print(route)
        method2_1=False
        #--------obs,angle-------#
        obj_nines_obss=[]
        obj_nine_holes_angles=[]
        for i in range(6):
            obj_nine_obs=0
            for k in range(1,ballcount):
                obj_nine_obs,_,_=point_to_line_distance(self.positions[k],self.obj,self.nine_holes_hitpoints[i],2*radius,obj_nine_obs)
                obj_nine_obs,_,_=point_to_line_distance(self.positions[k],self.nine,vir_hole_positions[i],2*radius,obj_nine_obs)
                obj_nine_hole_angle=vector_angle(self.obj,self.nine_holes_hitpoints[i],vir_hole_positions[i])
                obj_nine_holes_angles.append(obj_nine_hole_angle)
                
                if obj_nine_obs==0 and obj_nine_hole_angle <=90:
                    method2_1=True
            obj_nines_obss.append(obj_nine_obs)
            
        if method2_1==False:
            return method_choice.method2(self)
        cue_obj_nine_reflec_diss=[]
        method2_1scores=[]
        hit_vectors=[]
        
        #---------------distance-----------------#
        for j in range(4):
            cue_obj_nine_reflec_dis1=[]
            for i in range(6):
                cue_reflec1_dis,vx,vy=distance_and_vector(self.cue,self.reflection_obj_points_group[j][i])
                hit_vector=(vx,vy)
                hit_vectors.append(hit_vector)
                reflec1_obj_dis,_,_=distance_and_vector(self.reflection_obj_points_group[j][i],self.nine_holes_hitpoints[i])
                obj_nine_dis,_,_=distance_and_vector(self.nine,self.nine_holes_hitpoints[i])
                nine_hole_dis,_,_=distance_and_vector(self.nine,vir_hole_positions[i])
                cue_obj_nine_reflec_dis1.append(cue_reflec1_dis+reflec1_obj_dis+obj_nine_dis+nine_hole_dis)
            cue_obj_nine_reflec_diss.append(cue_obj_nine_reflec_dis1)
        #-------------score--------------------#
        method2_1scores2=[]
        for i in range(4):
            method2_1scores1=[]
            for j in range(6):
                method2_1score=cal_score(cue_obj_nine_reflec_diss[i][j],obj_nine_holes_angles[i],obj_nines_obss[i])
                method2_1scores1.append(method2_1score)
            method2_1scores2.append(method2_1scores1)
        print(method2_1scores)
        max_non_positive_score,best_index1,best_index2=find_min_negative_integer_in_nested_list(method2_1scores)
        #-------------choice---------------#
        if max_non_positive_score:
            best_virhole = vir_hole_positions[best_index2]
            reflection_point = self.reflection_obj_points_group[best_index1][best_index2]
            first_hitpoint = self.obj_holes_hitpoints[best_index2]
            best_cue_hitpoint=calculate_aim_point(self.cue,first_hitpoint,radius)
            best_hit_vector = hit_vectors[best_index2]
            routeobs = obj_nine_obs[best_index2]
            around_cue_hitpoint_detect=method_choice.edge_detect(self,best_cue_hitpoint)
            plt.plot(best_cue_hitpoint[0],best_cue_hitpoint[1],marker='o',ms=3,color='red')
            plt.plot([cuex,reflec1_obj_dis[0]],[cuey,reflection_point[1]],linestyle='-',color='red')
            plt.plot([reflection_point[0],first_hitpoint[0]],[reflection_point[1],first_hitpoint[1]],linestyle='-',color='red')
            plt.plot([self.obj[0],best_virhole[0]],[self.obj[1],best_virhole[1]],linestyle='-',color='red')
            
            screen2(ballcount,route,cuex,cuey,self.obj,self.nine)
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
        for i in range(6):
             cue_obj_hole_angle=vector_angle(self.cue,self.obj_holes_hitpoints[i],vir_hole_positions[i])
             cue_obj_holes_angle.append(cue_obj_hole_angle)
        #------------------distance,score--------#
        cue_relfec_obj_hole_diss2=[]
        for i in range(4):
            cue_relfec_obj_hole_diss1=[]
            for j in range(6):
                cue_reflec1_dis,vx,vy=distance_and_vector(self.cue,self.reflection_obj_points_group[i][j])
                hit_vector=(vx,vy)
                hit_vectors.append(hit_vector)
                reflec1_obj_dis,_,_=distance_and_vector(self.reflection_obj_points_group[i][j],self.obj_holes_hitpoints[j])
                obj_hole_dis,_,_=distance_and_vector(self.obj,vir_hole_positions[j])
                cue_relfec_obj_hole_dis=(cue_reflec1_dis+reflec1_obj_dis+obj_hole_dis)
                cue_relfec_obj_hole_diss1.append(cue_relfec_obj_hole_dis)
            cue_relfec_obj_hole_diss2.append(cue_relfec_obj_hole_diss1)
        for k in range(6):
            obj_hole_obs=0
            for j in range(1,ballcount):
                obj_hole_obs,_,_=point_to_line_distance(self.positions[j],self.obj,vir_hole_positions[k],2*radius,obj_hole_obs)
            obj_holes_obs.append(obj_hole_obs)
            if obj_hole_obs==0 and cue_obj_holes_angle[k] <= 90:
                method2=True
        method2_scores2=[]
        for i in range(4):
            method2_scores=[]
            for j in range(6):
                method2_score=cal_score(cue_relfec_obj_hole_diss2[i][j],cue_obj_holes_angle[j],obj_holes_obs[j])
                method2_scores.append(method2_score)
            method2_scores2.append(method2_scores)
        max_non_positive_score,best_index1,best_index2=find_min_negative_integer_in_nested_list(method2_scores2)
        print(method2_scores2)
        #-------------choice---------------#
        if max_non_positive_score:
            best_virhole = vir_hole_positions[best_index2]
            reflection_point = self.reflection_obj_points_group[best_index1][best_index2]
            first_hitpoint = self.obj_holes_hitpoints[best_index2]
            best_cue_hitpoint=calculate_aim_point(self.cue,reflection_point,radius)
            best_hit_vector = hit_vectors[best_index2]
            routeobs = obj_holes_obs[best_index2]
            around_cue_hitpoint_detect=method_choice.edge_detect(self,best_cue_hitpoint)
            plt.plot(best_cue_hitpoint[0],best_cue_hitpoint[1],marker='o',ms=3,color='red')
            plt.plot([cuex,reflection_point[0]],[cuey,reflection_point[1]],linestyle='-',color='red')
            plt.plot([reflection_point[0],first_hitpoint[0]],[reflection_point[1],first_hitpoint[1]],linestyle='-',color='red')
            plt.plot([self.obj[0],best_virhole[0]],[self.obj[1],best_virhole[1]],linestyle='-',color='red')
            screen2(ballcount,route,cuex,cuey,self.obj,self.nine)
            return max_non_positive_score,hit_vector[0], hit_vector[1], routeobs, best_cue_hitpoint[0], best_cue_hitpoint[1]
        else:
            return method_choice.method3(self)
    def method3(self):
        route=3
        print(route)
        method3=False
        cue_others_obs=[]
        obj_other_holes_angles=[]
        for i in range(1,ballcount-1):
            for j in range(6):
                obj_other_holes_angle=[]
                cue_other_obs=0
                for k in range(1,ballcount):
                    cue_other_obs,_,_=point_to_line_distance(self.positions[k],self.obj,self.cue_obj_others_hitpoints[i][j],radius,cue_other_obs)
                cue_others_obs.append(cue_other_obs)
        for j in range(1,ballcount-1):
            for k in range(6):
                obj_other_hole_angle=vector_angle(self.obj,self.cue_obj_others_hitpoints[j][k],vir_hole_positions[k])
                obj_other_holes_angle.append(obj_other_hole_angle)
            obj_other_holes_angles.append(obj_other_holes_angle)
                
        for i in range(6):
            for j in range(1,ballcount):
                if cue_others_obs[j]==0 and obj_other_holes_angles[i][j] <=0:
                    method3==True
        print("method3",method3)
        if method3==False:
            print("error")
            screen2(ballcount,route,cuex,cuey,self.obj,self.nine)
            return False
        other_route_dis2=[]
        hit_vectors=[]
        for i in range(1,ballcount):
            other_route_dis1=[]
            hit_vector=[]
            for j in range(6):
                cue_obj_dis,vx,vy=distance_and_vector(self.cue,self.cue_obj_others_hitpoints[i][j])
                hit_vector.append((vx,vy))
                obj_other_dis,_,_=distance_and_vector(self.obj,self.others_hitpoints[j])
                other_hole_dis,_,_=distance_and_vector(self.positions[i],vir_hole_positions[j])
                other_route_dis1.append(cue_obj_dis+obj_other_dis+other_hole_dis)
            other_route_dis2.append(other_route_dis1)
            hit_vectors.append(hit_vector)
        print(other_route_dis2)
        method3socre2=[]
        for i in range(1,ballcount-1):
            method3socre1=[]
            for j in range(6):
                method3score=cal_score(other_route_dis2[i][j],obj_other_holes_angles[i][j],cue_others_obs[i])
                method3socre1.append(method3score)
            method3socre2.append(method3socre1)
        non_positive_scores = [score for score in method3socre2 if score <= 0]
        if non_positive_scores:
            max_non_positive_score = max(non_positive_scores)
            best_index = method3socre2.index(max_non_positive_score)
            best_virhole = vir_hole_positions[best_index]
            first_hitpoint = self.obj_nines_hitpoints[best_index]
            second_hitpoint = self.nine_holes_hitpoints[best_index]
            best_hit_vector = hit_vectors[best_index]
            routeobs = cue_others_obs[best_index]
            hitcuepointx, hitcuepointy = calculate_aim_point(cuex, cuey, first_hitpoint[0], first_hitpoint[1], radius)
            finalobs=[]
            countobs = 0
            for i in range(ballcount):
                countobs, px, py = point_to_line_distance(self.positions[i],self.obj)
                if px > 0:
                    finalobs.append((px,py))
            cue_obstacle=method_choice.edge_detect(hitcuepointx,hitcuepointy)
            #----------screen-----------#
            method_choice.final(route,max_non_positive_score, hit_vector[0], hit_vector[1], routeobs, hitcuepointx, hitcuepointy,cue_obstacle)
            plt.plot([cuex,first_hitpoint[0]],[cuey,first_hitpoint[1]],linestyle='-')
            plt.plot([self.obj[0],second_hitpoint[0]],[self.obj[1],second_hitpoint[1]],linestyle='-')
            plt.plot([self.nine[0],best_virhole[0]],[self.nine[1],best_virhole[1]])
            for i in range(6):
                for j in range(1,ballcount):
                    plt.plot(self.cue_obj_others_hitpoints[i][j][0],self.cue_obj_others_hitpoints[i][j][1],marker='o',ms=3,color='yellow')
            screen2(ballcount,route,cuex,cuey,self.obj,self.nine)
            return max_non_positive_score,best_hit_vector[0], best_hit_vector[1], routeobs, hitcuepointx, hitcuepointy
            

if __name__=='__main__':
    balls=[]
    ballcount=8
    #def generate the ball
    cuex, cuey, ballx_set, bally_set, ball_count=generate_balls(ballcount,radius)
    print(ballx_set)
    print(bally_set)
    print("ballcount",ballcount)
    method=method_choice(ballx_set,bally_set,ballcount,cuex,cuey)
    method.main()
    

    
    
    