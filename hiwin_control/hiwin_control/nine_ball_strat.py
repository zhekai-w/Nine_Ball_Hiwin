import matplotlib.pyplot as plt
import matplotlib.path as mplPath
from matplotlib.patches import Polygon as MatplotlibPolygon
from shapely.geometry import Polygon, Point, LineString
import random
import numpy as np
import math
import time
from typing import Tuple
import yaml

'''
measure in mm
'''
# define table height width
tablewidth = 627
tableheight = 304

# radius of balls (30.4cm: 1.6cm = 932pixels : 97.5pixels)
r = 16

#radius of holes (62.6cm : 1920pixels = 2cm : 60pixels)
# rb = round(RB)
rb = 20

TOP_LEFT = [-311.196, 612.0]

#define hole locations and aiming point
holex =     [TOP_LEFT[0],            TOP_LEFT[0],            TOP_LEFT[0]+tablewidth/2,
             TOP_LEFT[0]+tablewidth, TOP_LEFT[0]+tablewidth, TOP_LEFT[0]+tablewidth/2]
holey =     [TOP_LEFT[1],             TOP_LEFT[1]-tableheight, TOP_LEFT[1]-tableheight,
             TOP_LEFT[1]-tableheight, TOP_LEFT[1],             TOP_LEFT[1]]
aimpointx = [TOP_LEFT[0]+r,            TOP_LEFT[0]+r,            TOP_LEFT[0]+tablewidth/2,
             TOP_LEFT[0]+tablewidth-r, TOP_LEFT[0]+tablewidth-r, TOP_LEFT[0]+tablewidth/2]
aimpointy = [TOP_LEFT[1]-r,             TOP_LEFT[1]-tableheight+r, TOP_LEFT[1]-tableheight+r,
             TOP_LEFT[1]-tableheight+r, TOP_LEFT[1]-r,             TOP_LEFT[1]-r]
aimtoholex = [-r,-r,0,r,r,0]
aimtoholey = [r,-r,-r,-r,r,r]

def SET_TABLE(config_file:str) -> None:
    '''
    Base on robot arm coordinate
    '''
    config_file = 'arm.yaml'
    with open(config_file, 'r') as file:
        data = yaml.safe_load(file)

    hole_0 = np.array(data['pot0'][0:2])
    hole_1 = np.array(data['pot3'][0:2])
    hole_3 = np.array(data['pot2'][0:2])
    hole_4 = np.array(data['pot1'][0:2])
    vx = hole_4 - hole_0
    vx_lengh = np.sqrt(vx[0]**2 + vx[1]**2)
    unit_vx = vx/vx_lengh
    hole_2 = hole_1 + vx*(vx_lengh/2)
    hole_5 = hole_0 +vx*(vx_lengh/2)
    vy = hole_1 - hole_0
    vy_lengh = np.sqrt(vy[0]**2 + vy[1]**2)
    unit_vy = vy/vy_lengh


# DISTANCE BETWEEN TWO BALLS
def disandvec(toballx, tobally, fromballx, frombally):
    vector_x = toballx-fromballx
    vector_y = tobally-frombally
    distance = math.sqrt(abs(vector_x)**2+abs(vector_y)**2)
    #round for the sake of visual, don't round it for accuracy
    distance = round(distance,2)
    return distance, vector_x, vector_y

# GENERATE RANDOM NUMBER TO SIMULATE BALL LOCATION
def generateballs(number_of_objectballs):
    print("number of balls:",number_of_objectballs)

    # generate cue ball
    cuex = random.uniform(aimpointx[0], aimpointx[3])
    cuex = round(cuex, 2)
    cuey = random.uniform(aimpointy[0], aimpointy[1])
    cuey = round(cuey, 2)


    # generate cue ball location
    objectballx = []
    objectbally = []
    for _ in range(0,number_of_objectballs):
        x = random.uniform(aimpointx[0], aimpointx[3])
        objectballx.append(round(x, 2))
        y = random.uniform(aimpointy[0], aimpointy[1])
        objectbally.append(round(y, 2))
    return cuex, cuey, objectballx, objectbally, number_of_objectballs

#CHECK IF BALL IS IN HOLE
def ballinhole(ballx, bally):
    balltohole = []
    for i in range(0,6):
        x, y, z= disandvec(holex[i], holey[i], ballx, bally)
        balltohole.append(x)
    mindis = min(balltohole)
    return mindis

#CALCULATE VOCTOR TO DOT DISTANCE
def dottovector(fromdotx, fromdoty, vectorx, vectory, dotx, doty):
    disoto = math.sqrt(abs(vectorx)**2+abs(vectory)**2)
    balltoballx = dotx-fromdotx
    balltobally = doty-fromdoty
    dotproduct = vectorx*balltoballx + vectory*balltobally
    if dotproduct > 0:
        shadowlengh = dotproduct/disoto
        ratio = shadowlengh/disoto
        shadowx = fromdotx+vectorx*ratio
        shadowy = fromdoty+vectory*ratio
        #normallengh, normalvectorx, normalvectory = disandvec(dotx, doty, shadowx, shadowy)
        normallengh = disandvec(dotx, doty, shadowx, shadowy)[0]

        return normallengh#, normalvectorx, normalvectory, shadowx, shadowy
    else:
        return -1

def findhitpoint(ballx, bally, vectorx, vectory):
    vectorlengh = math.sqrt(abs(vectorx)**2+abs(vectory)**2)
    x = vectorx*2*r/vectorlengh
    y = vectory*2*r/vectorlengh
    hitpointx = ballx-x
    hitpointy = bally-y
    return hitpointx, hitpointy

def hitpoint(ballx, bally, vectorx, vectory):
    vectorlengh = math.sqrt(abs(vectorx)**2+abs(vectory)**2)
    x = vectorx*1.5*r/vectorlengh
    y = vectory*1.5*r/vectorlengh
    hitpointx = ballx-x
    hitpointy = bally-y
    return hitpointx, hitpointy

def outofbound(hitx, hity):
    checkhitxplus = hitx + r
    checkhityplus = hity + r
    checkhitxminus = hitx - r
    checkhityminus = hity - r
    if checkhitxplus > holex[3] or checkhityplus > holey[0] or checkhitxminus < holex[0] or checkhityminus < holey[1]:
        hitoutbound = 1
    else:
        hitoutbound = 0
    return hitoutbound


def end_effector_mask(ballx, bally, vectorx, vectory):
    maskheight = 39+r
    maskwidth = 87+r
    vectorlengh = math.sqrt(abs(vectorx)**2+abs(vectory)**2)
    unit_vector = np.array([vectorx/vectorlengh, vectory/vectorlengh])
    normal_unit_vector = np.array([unit_vector[1], -unit_vector[0]])
    tengentdot = np.array([ballx-unit_vector[0]*r, bally-unit_vector[1]*r])
    first_poly = tengentdot - normal_unit_vector*maskheight/2
    second_poly = tengentdot + normal_unit_vector*maskheight/2
    third_poly = second_poly - unit_vector*maskwidth
    fourth_poly = first_poly - unit_vector*maskwidth

    return first_poly, second_poly, third_poly, fourth_poly


def check_obstacle(first_poly, second_poly, third_poly, fourth_poly, objectballx, objectbally):
    # polygon
    points_inside = []
    obstacle_flag = 0
    polygon_vertices = [first_poly, second_poly, third_poly, fourth_poly]
    polygon = Polygon(polygon_vertices)

    #table lines
    table_line_1 = [(holex[0], holey[0]), (holex[4], holey[4])]
    table_line_2 = [(holex[4], holey[4]), (holex[3], holey[3])]
    table_line_3 = [(holex[1], holey[1]),(holex[3], holey[3])]
    table_line_4 = [(holex[0], holey[0]), (holex[1], holey[1])]
    #check table intersect with polygon
    line1 = LineString(table_line_1)
    line2 = LineString(table_line_2)
    line3 = LineString(table_line_3)
    line4 = LineString(table_line_4)
    if line1.intersects(polygon) or line2.intersects(polygon) or line3.intersects(polygon) or line4.intersects(polygon):
        obstacle_flag = 1
        points_inside = [(0,0)]
    else:
        obstacle_flag = 0
    #check ball in polygon
    l = len(objectballx)
    for i in range(l):
        shapely_point = Point(objectballx[i], objectbally[i])
        if polygon.contains(shapely_point):
            points_inside.append((objectballx[i], objectbally[i]))
            obstacle_flag = 1
    return obstacle_flag, points_inside

def check_ball_inhole(all_ball_x:list, all_ball_y:list):
    inholeindex = []
    n = len(all_ball_x)
    for i in range(0,n): #because cue ball is in objectball[-1]
        distohole = ballinhole(all_ball_x[i], all_ball_y[i])
        if distohole < rb:
            print("objectball[%d] is in hole\n"%i)
            inholeindex.append(i)
            # print("objectball[%d] is deleted\n"%i)
        else:
            print("objectball[%d] is out of hole\n"%i)

    for j in range(0, len(inholeindex)):
        del all_ball_x[inholeindex[j]]
        del all_ball_y[inholeindex[j]]
        print("objectball[%d] is deleted\n"%j)
    return all_ball_x, all_ball_y

def angle_between_vector(v1, v2):
    v1_u = v1 / np.linalg.norm(v1)  # Unit vector of v1
    v2_u = v2 / np.linalg.norm(v2)  # Unit vector of v2
    theta_radians = np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))
    return np.degrees(theta_radians)

def vector_mask(ballx, bally, vectorx, vectory):
    maskwidth = 2*r
    vectorlengh = math.sqrt(abs(vectorx)**2+abs(vectory)**2)
    unit_vector = np.array([vectorx/vectorlengh, vectory/vectorlengh])
    vector = np.array([vectorx+unit_vector[0]*r, vectory+unit_vector[1]*r])
    normal_unit_vector = np.array([unit_vector[1], -unit_vector[0]])
    # tengentdot = np.array([ballx-unit_vector[0]*r, bally-unit_vector[1]*r])
    ball = np.array([ballx, bally])
    first_poly = ball - normal_unit_vector*maskwidth
    second_poly = ball + normal_unit_vector*maskwidth
    third_poly = second_poly + vector
    fourth_poly = first_poly + vector

    return first_poly, second_poly, third_poly, fourth_poly

def check_ball_in_way(first_poly, second_poly, third_poly, fourth_poly, objectballx, objectbally):
    points_in_poly_indices = []
    obstacle_number  = 0
    polygon_vertices = [first_poly, second_poly, third_poly, fourth_poly]
    polygon = Polygon(polygon_vertices)
    for i in range(len(objectballx)):
        shapely_objectballs = Point(objectballx[i], objectbally[i])
        if polygon.contains(shapely_objectballs) and i != 0:
            points_in_poly_indices.append(i)
            obstacle_number += 1
    return obstacle_number, points_in_poly_indices

class ReflectPointsVectors:
    def __init__(self, target_hitpoint_x, target_hitpoint_y, cuex, cuey, aimpointx, aimpointy):
        self.target_hitpoint_x = target_hitpoint_x
        self.target_hitpoint_y = target_hitpoint_y
        self.reflect_top_vectors = []
        self.reflect_right_vectors = []
        self.reflect_bot_vectors = []
        self.reflect_left_vectors = []
        self.top_reflect_point_x = []
        self.bot_reflect_point_x = []
        self.left_reflect_point_y = []
        self.right_reflect_point_y = []
        self.cuex = cuex
        self.cuey = cuey
        self.aimpointx = aimpointx
        self.aimpointy = aimpointy

    def calculate_reflect_points_vectors(self):
        # global aimpointy, cuey, aimpointx, cuex

        # do every aimpoint mirror vector
        for i in range(6):
            # calculate top reflection points
            target_to_top_dis = abs(self.aimpointy[0] - self.target_hitpoint_y[i])
            cue_to_top_dis = abs(self.aimpointy[0] - self.cuey)
            cue_to_hitpoint_x_dis = self.target_hitpoint_x[i] - self.cuex
            reflect_point_x = self.cuex + cue_to_hitpoint_x_dis * cue_to_top_dis / (target_to_top_dis + cue_to_top_dis)
            self.top_reflect_point_x.append(reflect_point_x)
            # calculate top reflection vectors
            self.reflect_top_vectors.append([reflect_point_x - self.cuex, self.aimpointy[0] - self.cuey,
                                             self.target_hitpoint_x[i] - reflect_point_x,
                                             self.target_hitpoint_y[i] - self.aimpointy[0]])

            # calculate bottom reflection points
            target_to_bot_dis = abs(self.aimpointy[1] - self.target_hitpoint_y[i])
            cue_to_bot_dis = abs(self.aimpointy[1] - self.cuey)
            cue_to_hitpoint_x_dis = self.target_hitpoint_x[i] - self.cuex
            reflect_point_x = self.cuex + cue_to_hitpoint_x_dis * cue_to_bot_dis / (target_to_bot_dis + cue_to_bot_dis)
            self.bot_reflect_point_x.append(reflect_point_x)
            # calculate bot reflection vectors
            self.reflect_bot_vectors.append([reflect_point_x - self.cuex, self.aimpointy[1] - self.cuey,
                                             self.target_hitpoint_x[i] - reflect_point_x,
                                             self.target_hitpoint_y[i] - self.aimpointy[1]])

            # calculate left reflection points
            target_to_left_dis = abs(self.aimpointx[0] - self.target_hitpoint_x[i])
            cue_to_left_dis = abs(self.aimpointx[0] - self.cuex)
            cue_to_hitpoint_y_dis = self.target_hitpoint_y[i] - self.cuey
            reflect_point_y = self.cuey + cue_to_hitpoint_y_dis * cue_to_left_dis / (target_to_left_dis + cue_to_left_dis)
            self.left_reflect_point_y.append(reflect_point_y)
            # calculate left reflection vectors
            self.reflect_left_vectors.append([self.aimpointx[0] - self.cuex, reflect_point_y - self.cuey,
                                              self.target_hitpoint_x[i] - self.aimpointx[0],
                                              self.target_hitpoint_y[i] - reflect_point_y])

            # calculate right reflection points
            target_to_right_dis = abs(self.aimpointx[3] - self.target_hitpoint_x[i])
            cue_to_right_dis = abs(self.aimpointx[3] - self.cuex)
            cue_to_hitpoint_y_dis = self.target_hitpoint_y[i] - self.cuey
            reflect_point_y = self.cuey + cue_to_hitpoint_y_dis * cue_to_right_dis / (target_to_right_dis + cue_to_right_dis)
            self.right_reflect_point_y.append(reflect_point_y)
            # calculate right reflection vectors
            self.reflect_right_vectors.append([self.aimpointx[3] - self.cuex, reflect_point_y - self.cuey,
                                               self.target_hitpoint_x[i] - self.aimpointx[3],
                                               self.target_hitpoint_y[i] - reflect_point_y])

def simple_route(cue=[0, 0], cuetoivector=[0, 0], itok2vector=[0, 0] ,k2tok1vector=[0, 0], toholevector=[0, 0],n=0):
    #fix cuefinalvector
    score = None
    if n == 0 or n == -1:
        if n == 0:
            cuefinalvector = [cuetoivector[0]-toholevector[0], cuetoivector[1]-toholevector[1]]
            cuetoiL = math.sqrt(abs(cuetoivector[0])**2+abs(cuetoivector[1])**2)
            itohL = math.sqrt(abs(toholevector[0])**2+abs(toholevector[1])**2)
            dotproduct0 = cuetoivector[0]*toholevector[0] + cuetoivector[1]*toholevector[1]
            cos = dotproduct0/(cuetoiL*itohL)
            angle = math.acos(cos)
            score = (-angle*1273 + 2000) + (- 3.16*(cuetoiL+itohL) + 2000) + (-n*1000 + 2000)
        else:
            cuefinalvector = [cuetoivector[0]-toholevector[0], cuetoivector[1]-toholevector[1]]
            cuetoiL = math.sqrt(abs(cuetoivector[0])**2+abs(cuetoivector[1])**2)
            itohL = math.sqrt(abs(toholevector[0])**2+abs(toholevector[1])**2)
            dotproduct0 = cuetoivector[0]*toholevector[0] + cuetoivector[1]*toholevector[1]
            score = -6000.0

    elif n == 1:
        cuefinalvector = [cuetoivector[0]-itok2vector[0],cuetoivector[1]-itok2vector[1]]
        cuetoiL = math.sqrt(abs(cuetoivector[0])**2+abs(cuetoivector[1])**2)
        itok2L = math.sqrt(abs(itok2vector[0])**2+abs(itok2vector[1])**2)
        k2toholeL = math.sqrt(abs(toholevector[0])**2+abs(toholevector[1])**2)
        angle0 = math.acos((cuetoivector[0]*itok2vector[0]+cuetoivector[1]*itok2vector[1])/(cuetoiL*itok2L))
        angle1 = math.acos((itok2vector[0]*toholevector[0]+itok2vector[1]*toholevector[1])/(k2toholeL*itok2L))
        score = (-angle0*1273 + 2000)/2 + (-angle1*1273 + 2000)/2 + (- 3.16*(cuetoiL+itok2L+k2toholeL) + 2000)  + (-n*1000 + 2000)

    elif n == 2:
        cuefinalvector = [cuetoivector[0]-itok2vector[0],cuetoivector[1]-itok2vector[1]]
        cuetoiL = math.sqrt(abs(cuetoivector[0])**2+abs(cuetoivector[1])**2)
        itok2L = math.sqrt(abs(itok2vector[0])**2+abs(itok2vector[1])**2)
        k2tok1L = math.sqrt(abs(k2tok1vector[0])**2+abs(k2tok1vector[1])**2)
        k1toholeL = math.sqrt(abs(toholevector[0])**2+abs(toholevector[1])**2)
        angle0 = math.acos((cuetoivector[0]*itok2vector[0]+cuetoivector[1]*itok2vector[1])/(cuetoiL*itok2L))
        angle1 = math.acos((itok2vector[0]*k2tok1vector[0]+itok2vector[1]*k2tok1vector[1])/(k2tok1L*itok2L))
        angle2 = math.acos((k2tok1vector[0]*toholevector[0]+k2tok1vector[1]*toholevector[1])/(k1toholeL*k2tok1L))
        score = (-angle0*1273 + 2000)/3 + (-angle1*1273 + 2000)/3 + (-angle2*1273 + 2000)/3 + (- 3.16*(cuetoiL+itok2L+k2tok1L+k1toholeL) + 2000) + (-n*1000 + 2000)

    final_hitpoint_x, final_hitpoint_y = hitpoint(cue[0], cue[1], cuetoivector[0], cuetoivector[1])
    return score, cuetoivector, [final_hitpoint_x, final_hitpoint_y]
    # return score,cuefinalvector,cue,cuetoivector, objectballi, itok2vector, objectballk2 ,k2tok1vector, objectballk1, toholevector,n

def reflected_route(cue, cue_to_wall_v, wall_to_target_v, target_to_aim_v):
    cue_to_wall_dis = math.sqrt(abs(cue_to_wall_v[0])**2+abs(cue_to_wall_v[1])**2)
    wall_to_target_dis = math.sqrt(abs(wall_to_target_v[0])**2+abs(wall_to_target_v[1])**2)
    target_to_aim_dis = math.sqrt(abs(target_to_aim_v[0])**2+abs(target_to_aim_v[1])**2)
    angle0 = angle_between_vector(cue_to_wall_v, wall_to_target_v)
    angle1 = angle_between_vector(wall_to_target_v, target_to_aim_v)
    score =  (-angle0*1273 + 2000)/2 + (-angle1*1273 + 2000)/2 + (- 3.16*(cue_to_wall_dis+wall_to_target_dis+target_to_aim_dis) + 2000)
    final_hitpoint_x, final_hitpoint_y = hitpoint(cue[0], cue[1], cue_to_wall_v[0], cue_to_wall_v[1])

    return score, cue_to_wall_v, [final_hitpoint_x, final_hitpoint_y]



def DISPLAY_OBSTACLE_BALL(who_in_cue_to_target_way, who_in_target_to_aim_way, objectballx, objectbally):
    for indices in who_in_cue_to_target_way:
        if len(indices) == 1:
            for i in indices:
                inway = plt.Circle((objectballx[i], objectbally[i]),
                                    2, color="black", alpha=0.7)
                plt.gca().add_patch(inway)
        else:
            for i in indices:
                inway = plt.Circle((objectballx[i], objectbally[i]),
                                    2, color="black", alpha=0.7)
                plt.gca().add_patch(inway)

    for indices in who_in_target_to_aim_way:
        if len(indices) == 1:
            for i in indices:
                inway = plt.Circle((objectballx[i], objectbally[i]),
                                    2, color="black", alpha=0.7)
                plt.gca().add_patch(inway)
        else:
            for i in indices:
                inway = plt.Circle((objectballx[i], objectbally[i]),
                                    2, color="black", alpha=0.7)
                plt.gca().add_patch(inway)

def DISPLAY_MASK(first_poly, second_poly, third_poly, fourth_poly) -> None:
    polygon_vertices = [first_poly, second_poly, third_poly, fourth_poly]
    polygon = MatplotlibPolygon(polygon_vertices, closed=True, edgecolor='pink', facecolor='pink', alpha = 0.3)
    plt.gca().add_patch(polygon)

def DISPLAY_POOL_TABLE(objectballx, objectbally, cuex, cuey) -> None:
    #plot vector from aiming point to hole
    for i in range(0,6):
        plt.quiver(aimpointx[i],aimpointy[i],aimtoholex[i],aimtoholey[i],color='red',units="xy",angles="xy",scale_units="xy",scale=1, width=1)

    #Plot table boundry
    plt.plot([holex[0],holex[1]],[holey[0],holey[1]],[holex[1],holex[2]],[holey[1],holey[2]],
             [holex[2],holex[3]],[holey[2],holey[3]],[holex[3],holex[4]],[holey[3],holey[4]],
             [holex[4],holex[5]],[holey[4],holey[5]],[holex[5],holex[0]],[holey[5],holey[0]],color='black')

    #plot aim point
    for j in range(len(aimpointx)):
        aimpoint = plt.Circle((aimpointx[j], aimpointy[j]),
                            r, color="red", alpha=0.2)
        plt.text(aimpointx[j],aimpointy[j],j,color='red',fontsize=15)
        plt.gca().add_patch(aimpoint)

    #PLOT ALL BALLS AND HOLES
        #plot objectballs
    # objectballcolor = ['r','orange','blue','green','purple','black','brown','cyan']
    for i in range(len(objectballx)):
        if i == 0:
            objectball = plt.Circle((objectballx[i], objectbally[i]), r, color='green', alpha=0.5)
        else:
            objectball = plt.Circle((objectballx[i], objectbally[i]), r, color='blue', alpha=0.5)
        plt.text(objectballx[i],objectbally[i],i,fontsize=15)
        plt.gca().add_patch(objectball)

    #plot cue ball
    plt.gca().add_patch(plt.Circle((cuex, cuey), r, color='red', alpha=0.5))


    #plot holes
    for j in range(len(holex)):
        hole = plt.Circle((holex[j], holey[j]),
                            rb, color="black", alpha=0.7)
        #plt.text(holex[j],holey[j],j,color='white',fontsize=15)
        plt.gca().add_patch(hole)



def main(objectballx, objectbally, cuex, cuey) -> Tuple:
    target_to_aimpoint_x = []
    target_to_aimpoint_y = []
    target_hitpoint_x = []
    target_hitpoint_y = []
    cue_to_target_x = []
    cue_to_target_y = []
    angles = []
    who_in_target_to_aim_way = []
    who_in_cue_to_target_way = []

    objectballx, objectbally = check_ball_inhole(objectballx, objectbally)

    for i in range(6):
        # calculate vector from target ball to hole
        target_dis, target_vx, target_vy = disandvec(aimpointx[i],aimpointy[i], objectballx[0], objectbally[0])
        target_to_aimpoint_x.append(target_vx)
        target_to_aimpoint_y.append(target_vy)

        # calculate target ball hitpoint and cue to target ball hitpoint vector
        temp_hit_x, temp_hit_y = findhitpoint(objectballx[0], objectbally[0], target_vx, target_vy)
        target_hitpoint_x.append(temp_hit_x)
        target_hitpoint_y.append(temp_hit_y)
        cue_dis, cue_vx, cue_vy = disandvec(temp_hit_x, temp_hit_y, cuex, cuey)
        cue_to_target_x.append(cue_vx)
        cue_to_target_y.append(cue_vy)

        # calculate each routes vectors angle
        angle = angle_between_vector([target_vx, target_vy], [cue_vx,cue_vy])
        angles.append(angle)

    # check who is in target-aimpoint vectors and cue-targetaimpoint vector(check only if angle < 80)
    # and check if target hitpoint is out table bound
    All_simple_routes = []
    for i in range(6):
        '''display target hitpoint'''
        if  outofbound(target_hitpoint_x[i], target_hitpoint_y[i]) == 0:
            plt.gca().add_patch(plt.Circle((target_hitpoint_x[i], target_hitpoint_y[i]), 3, color='green'))
        else:
            plt.gca().add_patch(plt.Circle((target_hitpoint_x[i], target_hitpoint_y[i]), 3, color='red'))
        '''display target hitpoint'''

        if angles[i] < 80 and outofbound(target_hitpoint_x[i], target_hitpoint_y[i]) == 0:
            # cue-targetaimpoint mask
            poly1, poly2, poly3, poly4 = vector_mask(cuex, cuey, cue_to_target_x[i], cue_to_target_y[i])
            DISPLAY_MASK(poly1, poly2, poly3, poly4)
            in_cue_target_obs_number, in_cue_target_poly_indices = check_ball_in_way(poly1, poly2, poly3, poly4, objectballx, objectbally)
            who_in_cue_to_target_way.append(in_cue_target_poly_indices)
            if in_cue_target_obs_number == 0:
                # target-aimpoint mask
                poly1, poly2, poly3, poly4 = vector_mask(objectballx[0], objectbally[0], target_to_aimpoint_x[i], target_to_aimpoint_y[i])
                DISPLAY_MASK(poly1, poly2, poly3, poly4)
                in_target_aim_obs_number, in_target_aim_poly_indices = check_ball_in_way(poly1, poly2, poly3, poly4, objectballx, objectbally)
                who_in_target_to_aim_way.append(in_target_aim_poly_indices)
                if in_target_aim_obs_number == 0:
                    print("route clear")
                    plt.quiver(objectballx[0], objectbally[0], target_to_aimpoint_x[i], target_to_aimpoint_y[i], color='green',
                        units="xy",angles="xy",scale_units="xy",scale=1, width=2)
                    plt.quiver(cuex, cuey, cue_to_target_x[i], cue_to_target_y[i], color='green',
                        units="xy",angles="xy",scale_units="xy",scale=1, width=2)
                    """
                    SAVE ROUTE (score, obstacle_flag, hitpoint, vector)
                    """
                    # route(cue=[0, 0], cuetoivector=[0, 0], itok2vector=[0, 0] ,k2tok1vector=[0, 0], toholevector=[0, 0],n=0)
                    route_info = simple_route(cue=[cuex, cuey], cuetoivector=[cue_to_target_x[i], cue_to_target_y[i]],
                                       toholevector=[target_to_aimpoint_x[i], target_to_aimpoint_y[i]], n=0)
                    All_simple_routes.append(route_info)


                elif in_target_aim_obs_number == 1:
                    print("kiss ball")
                    '''
                    STILL NEED TO CHECK ANGLE
                    '''
                    kiss_aim_dis, kiss_aim_vx, kiss_aim_vy = disandvec(aimpointx[i], aimpointy[i], objectballx[in_target_aim_poly_indices[0]], objectbally[in_target_aim_poly_indices[0]])
                    kiss_hitpoint_x, kiss_hitpoint_y = findhitpoint(objectballx[in_target_aim_poly_indices[0]], objectbally[in_target_aim_poly_indices[0]], kiss_aim_vx, kiss_aim_vy)
                    target_kiss_dis, target_kiss_vx, target_kiss_vy = disandvec(kiss_hitpoint_x, kiss_hitpoint_y, objectballx[0], objectbally[0])
                    target_kiss_hitpoint_x, target_kiss_hitpoint_y = findhitpoint(objectballx[0], objectbally[0], target_kiss_vx, target_kiss_vy)
                    cue_target_dis, cue_target_vx, cue_target_vy = disandvec(target_kiss_hitpoint_x, target_kiss_hitpoint_y, cuex, cuey)
                    # cue_hitpoint_x, cue_hitpoint_y = findhitpoint(cuex, cuey, cue_target_vx, cue_target_vy)
                    cue_target_kiss_angle = angle_between_vector([cue_target_vx, cue_target_vy], [target_kiss_vx, target_kiss_vy])
                    target_kiss_aim_angle = angle_between_vector([target_kiss_vx, target_kiss_vy], [kiss_aim_vx, kiss_aim_vy])

                    if cue_target_kiss_angle < 80 and target_kiss_aim_angle < 80:
                        plt.quiver(objectballx[in_target_aim_poly_indices[0]], objectbally[in_target_aim_poly_indices[0]], kiss_aim_vx, kiss_aim_vy, color='green',
                            units="xy",angles="xy",scale_units="xy",scale=1, width=2)
                        plt.quiver(objectballx[0], objectbally[0], target_kiss_vx, target_kiss_vy, color='green',
                            units="xy",angles="xy",scale_units="xy",scale=1, width=2)
                        plt.quiver(cuex, cuey, cue_target_vx, cue_target_vy, color='green',
                            units="xy",angles="xy",scale_units="xy",scale=1, width=2)

                        """
                        SAVE ROUTE (score, obstacle_flag, hitpoint, vector)
                        """
                        route_info = simple_route(cue=[cuex, cuey], cuetoivector=[cue_target_vx, cue_target_vy],
                                       itok2vector=[target_kiss_vx, target_kiss_vy], toholevector=[kiss_aim_vx, kiss_aim_vy], n=1)
                        All_simple_routes.append(route_info)

                    else:
                        print("kiss angle is off")

                else:
                    print("Too many balls in between target and aimpoint")
                    print("going for reflect ball")
            print("All Simple Routes:", All_simple_routes)


            '''display'''
            plt.quiver(objectballx[0], objectbally[0], target_to_aimpoint_x[i], target_to_aimpoint_y[i], color='black',
                        units="xy",angles="xy",scale_units="xy",scale=1, width=10, alpha=0.2)
            plt.quiver(cuex, cuey, cue_to_target_x[i], cue_to_target_y[i], color='black',
                        units="xy",angles="xy",scale_units="xy",scale=1, width=10, alpha=0.2)
            '''display'''

    print("who is between cue and target:", who_in_cue_to_target_way)
    print("who is between target and aimpoint:",who_in_target_to_aim_way)

    if len(All_simple_routes) > 0:
        # simple_route return this -> score, cuetoivector, [final_hitpoint_x, final_hitpoint_y]

        score = []
        for route in All_simple_routes:
            tempscore = route[0]
            score.append(tempscore)

        best_route_index = score.index(max(score))
        print("Best Simple Route:", All_simple_routes[best_route_index])
        score, cuetotarget_v, hitpoint = All_simple_routes[best_route_index]
        # check obstacle or outofbound
        out_flag = outofbound(hitpoint[0], hitpoint[1])
        first_poly, second_poly, third_poly, fourth_poly = end_effector_mask(cuex, cuey, cuetotarget_v[0], cuetotarget_v[1])

        obstacle_flag, points_in_poly = check_obstacle(first_poly, second_poly, third_poly, fourth_poly, objectballx, objectbally)
        obstacle_flag = out_flag or obstacle_flag
        print("obstacle flag:", obstacle_flag)
        DISPLAY_MASK(first_poly, second_poly, third_poly, fourth_poly)
        DISPLAY_OBSTACLE_BALL(who_in_cue_to_target_way, who_in_target_to_aim_way, objectballx, objectbally)
        DISPLAY_POOL_TABLE(objectballx, objectbally, cuex, cuey)
        plt.title("sim pool table")
        plt.axis([0, tablewidth, 0, tableheight])
        plt.axis("equal")
        plt.show(block=False)
        input("Enter to continue...")
        plt.pause(0.5)
        plt.cla()

        return [score, cuetotarget_v[0], cuetotarget_v[1], obstacle_flag, hitpoint[0], hitpoint[1]]
        # [score, cuetotarget_v[0], cuetotarget_v[1], obstacle_flag, hitpoint[0], hitpoint[1]]

    else:
        print("No valid simple route")
        print("Going for reflected route")

    reflect_points_vectors = ReflectPointsVectors(target_hitpoint_x, target_hitpoint_y, cuex, cuey, aimpointx, aimpointy)

    # Call the method to calculate the reflect points and vectors
    reflect_points_vectors.calculate_reflect_points_vectors()

    # Access the calculated values from the instance variables
    reflect_top_vectors = reflect_points_vectors.reflect_top_vectors
    reflect_right_vectors = reflect_points_vectors.reflect_right_vectors
    reflect_bot_vectors = reflect_points_vectors.reflect_bot_vectors
    reflect_left_vectors = reflect_points_vectors.reflect_left_vectors
    top_reflect_point_x = reflect_points_vectors.top_reflect_point_x
    bot_reflect_point_x = reflect_points_vectors.bot_reflect_point_x
    left_reflect_point_y = reflect_points_vectors.left_reflect_point_y
    right_reflect_point_y = reflect_points_vectors.right_reflect_point_y

    All_reflected_routes = []
    for i in range(6):
        # check target hitpoint out of bound
        if outofbound(target_hitpoint_x[i], target_hitpoint_y[i]) == 0:
            plt.gca().add_patch(plt.Circle((target_hitpoint_x[i], target_hitpoint_y[i]), 3, color='red'))

            # top reflection points and vectors
            cue_top_and_cue_target_angle = angle_between_vector([reflect_top_vectors[i][0], reflect_top_vectors[i][1]], [objectballx[0]-cuex, objectbally[0]-cuey])
            top_target_and_target_aim_angle = angle_between_vector([reflect_top_vectors[i][2], reflect_top_vectors[i][3]], [target_to_aimpoint_x[i], target_to_aimpoint_y[i]])
            if cue_top_and_cue_target_angle < 135 and top_target_and_target_aim_angle < 80:

                first_poly_0_T, second_poly_0_T, third_poly_0_T, fourth_poly_0_T = vector_mask(cuex, cuey, reflect_top_vectors[i][0], reflect_top_vectors[i][1])
                number_of_obstacle_T, in_poly_indices = check_ball_in_way(first_poly_0_T, second_poly_0_T, third_poly_0_T, fourth_poly_0_T, objectballx, objectbally)
                if number_of_obstacle_T == 0:
                        first_poly_1_T, second_poly_1_T, third_poly_1_T, fourth_poly_1_T = vector_mask(top_reflect_point_x[i], aimpointy[0], reflect_top_vectors[i][2], reflect_top_vectors[i][3])
                        number_of_obstacle_T, in_poly_indices = check_ball_in_way(first_poly_1_T, second_poly_1_T, third_poly_1_T, fourth_poly_1_T, objectballx, objectbally)
                        if number_of_obstacle_T == 0:
                            first_poly_2_T, second_poly_2_T, third_poly_2_T, fourth_poly_2_T = vector_mask(target_hitpoint_x[i], target_hitpoint_y[i], target_to_aimpoint_x[i], target_to_aimpoint_y[i])
                            number_of_obstacle_T, in_poly_indices = check_ball_in_way(first_poly_2_T, second_poly_2_T, third_poly_2_T, fourth_poly_2_T, objectballx, objectbally)
                            if number_of_obstacle_T <= 1:
                                route_info = reflected_route([cuex, cuey], [reflect_top_vectors[i][0], reflect_top_vectors[i][1]],
                                                             [reflect_top_vectors[i][2], reflect_top_vectors[i][3]], [target_to_aimpoint_x[i], target_to_aimpoint_y[i]])
                                All_reflected_routes.append(route_info)
                                plt.gca().add_patch(plt.Circle((top_reflect_point_x[i], aimpointy[0]), 3, color='red'))
                                plt.quiver(cuex, cuey, reflect_top_vectors[i][0], reflect_top_vectors[i][1], color='black',
                                            units="xy",angles="xy",scale_units="xy",scale=1, width=1)
                                plt.quiver(top_reflect_point_x[i], aimpointy[0], reflect_top_vectors[i][2], reflect_top_vectors[i][3], color='black',
                                            units="xy",angles="xy",scale_units="xy",scale=1, width=1)
                                plt.quiver(target_hitpoint_x[i], target_hitpoint_y[i], target_to_aimpoint_x[i], target_to_aimpoint_y[i], color='red',
                                        units="xy",angles="xy",scale_units="xy",scale=1, width=1)
                                DISPLAY_MASK(first_poly_0_T, second_poly_0_T, third_poly_0_T, fourth_poly_0_T )
                                DISPLAY_MASK(first_poly_1_T, second_poly_1_T, third_poly_1_T, fourth_poly_1_T)
                                DISPLAY_MASK(first_poly_2_T, second_poly_2_T, third_poly_2_T, fourth_poly_2_T)
                else:
                    continue

            # bot reflection points and vectors
            cue_bot_and_cue_target_angle = angle_between_vector([reflect_bot_vectors[i][0], reflect_bot_vectors[i][1]], [objectballx[0]-cuex, objectbally[0]-cuey])
            bot_target_and_target_aim_angle = angle_between_vector([reflect_bot_vectors[i][2], reflect_bot_vectors[i][3]], [target_to_aimpoint_x[i], target_to_aimpoint_y[i]])
            if cue_bot_and_cue_target_angle < 135 and bot_target_and_target_aim_angle < 80:

                first_poly_0_B, second_poly_0_B, third_poly_0_B, fourth_poly_0_B = vector_mask(cuex, cuey, reflect_bot_vectors[i][0], reflect_bot_vectors[i][1])
                number_of_obstacle_B, in_poly_indices = check_ball_in_way(first_poly_0_B, second_poly_0_B, third_poly_0_B, fourth_poly_0_B, objectballx, objectbally)
                if number_of_obstacle_B == 0:
                        first_poly_1_B, second_poly_1_B, third_poly_1_B, fourth_poly_1_B = vector_mask(bot_reflect_point_x[i], aimpointy[1], reflect_bot_vectors[i][2], reflect_bot_vectors[i][3])
                        number_of_obstacle_B, in_poly_indices = check_ball_in_way(first_poly_1_B, second_poly_1_B, third_poly_1_B, fourth_poly_1_B, objectballx, objectbally)
                        if number_of_obstacle_B == 0:
                            first_poly_2_B, second_poly_2_B, third_poly_2_B, fourth_poly_2_B = vector_mask(target_hitpoint_x[i], target_hitpoint_y[i], target_to_aimpoint_x[i], target_to_aimpoint_y[i])
                            number_of_obstacle_B, in_poly_indices = check_ball_in_way(first_poly_2_B, second_poly_2_B, third_poly_2_B, fourth_poly_2_B, objectballx, objectbally)
                            if number_of_obstacle_B <= 1:
                                route_info = reflected_route([cuex, cuey], [reflect_bot_vectors[i][0], reflect_bot_vectors[i][1]],
                                                             [reflect_bot_vectors[i][2], reflect_bot_vectors[i][3]], [target_to_aimpoint_x[i], target_to_aimpoint_y[i]])
                                All_reflected_routes.append(route_info)

                                plt.gca().add_patch(plt.Circle((bot_reflect_point_x[i], aimpointy[1]), 3, color='red'))
                                plt.quiver(cuex, cuey, reflect_bot_vectors[i][0], reflect_bot_vectors[i][1], color='black',
                                            units="xy",angles="xy",scale_units="xy",scale=1, width=1)
                                plt.quiver(bot_reflect_point_x[i], aimpointy[1], reflect_bot_vectors[i][2], reflect_bot_vectors[i][3], color='black',
                                            units="xy",angles="xy",scale_units="xy",scale=1, width=1)
                                plt.quiver(target_hitpoint_x[i], target_hitpoint_y[i], target_to_aimpoint_x[i], target_to_aimpoint_y[i], color='red',
                                        units="xy",angles="xy",scale_units="xy",scale=1, width=1)
                                DISPLAY_MASK(first_poly_0_B, second_poly_0_B, third_poly_0_B, fourth_poly_0_B)
                                DISPLAY_MASK(first_poly_1_B, second_poly_1_B, third_poly_1_B, fourth_poly_1_B)
                                DISPLAY_MASK(first_poly_2_B, second_poly_2_B, third_poly_2_B, fourth_poly_2_B)

                else:
                    continue

            # left reflection points and vectors
            cue_left_and_cue_target_angle = angle_between_vector([reflect_left_vectors[i][0], reflect_left_vectors[i][1]], [objectballx[0]-cuex, objectbally[0]-cuey])
            left_target_and_target_aim_angle = angle_between_vector([reflect_left_vectors[i][2], reflect_left_vectors[i][3]], [target_to_aimpoint_x[i], target_to_aimpoint_y[i]])
            if cue_left_and_cue_target_angle < 135 and left_target_and_target_aim_angle < 80:

                first_poly_0_L, second_poly_0_L, third_poly_0_L, fourth_poly_0_L = vector_mask(cuex, cuey, reflect_left_vectors[i][0], reflect_left_vectors[i][1])
                number_of_obstacle_L, in_poly_indices = check_ball_in_way(first_poly_0_L, second_poly_0_L, third_poly_0_L, fourth_poly_0_L, objectballx, objectbally)
                if number_of_obstacle_L == 0:
                        first_poly_1_L, second_poly_1_L, third_poly_1_L, fourth_poly_1_L = vector_mask(aimpointx[0], left_reflect_point_y[i], reflect_left_vectors[i][2], reflect_left_vectors[i][3])
                        number_of_obstacle_L, in_poly_indices = check_ball_in_way(first_poly_1_L, second_poly_1_L, third_poly_1_L, fourth_poly_1_L, objectballx, objectbally)
                        if number_of_obstacle_L == 0:
                            first_poly_2_L, second_poly_2_L, third_poly_2_L, fourth_poly_2_L = vector_mask(target_hitpoint_x[i], target_hitpoint_y[i], target_to_aimpoint_x[i], target_to_aimpoint_y[i])
                            number_of_obstacle_L, in_poly_indices = check_ball_in_way(first_poly_2_L, second_poly_2_L, third_poly_2_L, fourth_poly_2_L, objectballx, objectbally)
                            if number_of_obstacle_L <= 1:
                                route_info = reflected_route([cuex, cuey], [reflect_left_vectors[i][0], reflect_left_vectors[i][1]],
                                                             [reflect_left_vectors[i][2], reflect_left_vectors[i][3]], [target_to_aimpoint_x[i], target_to_aimpoint_y[i]])
                                All_reflected_routes.append(route_info)

                                plt.gca().add_patch(plt.Circle((aimpointx[0], left_reflect_point_y[i]), 3, color='red'))
                                plt.quiver(cuex, cuey, reflect_left_vectors[i][0], reflect_left_vectors[i][1], color='black',
                                            units="xy",angles="xy",scale_units="xy",scale=1, width=1)
                                plt.quiver(aimpointx[0], left_reflect_point_y[i], reflect_left_vectors[i][2], reflect_left_vectors[i][3], color='black',
                                            units="xy",angles="xy",scale_units="xy",scale=1, width=1)
                                plt.quiver(target_hitpoint_x[i], target_hitpoint_y[i], target_to_aimpoint_x[i], target_to_aimpoint_y[i], color='red',
                                        units="xy",angles="xy",scale_units="xy",scale=1, width=1)
                                DISPLAY_MASK(first_poly_0_L, second_poly_0_L, third_poly_0_L, fourth_poly_0_L)
                                DISPLAY_MASK(first_poly_1_L, second_poly_1_L, third_poly_1_L, fourth_poly_1_L)
                                DISPLAY_MASK(first_poly_2_L, second_poly_2_L, third_poly_2_L, fourth_poly_2_L)
                else:
                    continue

            # right reflection points and vectors
            cue_right_and_cue_target_angle = angle_between_vector([reflect_right_vectors[i][0], reflect_right_vectors[i][1]], [objectballx[0]-cuex, objectbally[0]-cuey])
            right_target_and_target_aim_angle = angle_between_vector([reflect_right_vectors[i][2], reflect_right_vectors[i][3]], [target_to_aimpoint_x[i], target_to_aimpoint_y[i]])
            if  cue_right_and_cue_target_angle< 135 and right_target_and_target_aim_angle < 80:

                first_poly_0_R, second_poly_0_R, third_poly_0_R, fourth_poly_0_R = vector_mask(cuex, cuey, reflect_right_vectors[i][0], reflect_right_vectors[i][1])
                number_of_obstacle_R, in_poly_indices = check_ball_in_way(first_poly_0_R, second_poly_0_R, third_poly_0_R, fourth_poly_0_R, objectballx, objectbally)
                if number_of_obstacle_R == 0:
                        first_poly_1_R, second_poly_1_R, third_poly_1_R, fourth_poly_1_R = vector_mask(aimpointx[3], right_reflect_point_y[i], reflect_right_vectors[i][2], reflect_right_vectors[i][3])
                        number_of_obstacle_R, in_poly_indices = check_ball_in_way(first_poly_1_R, second_poly_1_R, third_poly_1_R, fourth_poly_1_R, objectballx, objectbally)
                        if number_of_obstacle_R == 0:
                            first_poly_2_R, second_poly_2_R, third_poly_2_R, fourth_poly_2_R = vector_mask(target_hitpoint_x[i], target_hitpoint_y[i], target_to_aimpoint_x[i], target_to_aimpoint_y[i])
                            number_of_obstacle_R, in_poly_indices = check_ball_in_way(first_poly_2_R, second_poly_2_R, third_poly_2_R, fourth_poly_2_R, objectballx, objectbally)
                            if number_of_obstacle_R <= 1:
                                route_info = reflected_route([cuex, cuey], [reflect_right_vectors[i][0], reflect_right_vectors[i][1]],
                                                             [reflect_right_vectors[i][2], reflect_right_vectors[i][3]], [target_to_aimpoint_x[i], target_to_aimpoint_y[i]])
                                All_reflected_routes.append(route_info)

                                plt.gca().add_patch(plt.Circle((aimpointx[3], right_reflect_point_y[i]), 3, color='red'))
                                plt.quiver(cuex, cuey, reflect_right_vectors[i][0], reflect_right_vectors[i][1], color='black',
                                            units="xy",angles="xy",scale_units="xy",scale=1, width=1)
                                plt.quiver(aimpointx[3], right_reflect_point_y[i], reflect_right_vectors[i][2], reflect_right_vectors[i][3], color='black',
                                            units="xy",angles="xy",scale_units="xy",scale=1, width=1)
                                plt.quiver(target_hitpoint_x[i], target_hitpoint_y[i], target_to_aimpoint_x[i], target_to_aimpoint_y[i], color='red',
                                        units="xy",angles="xy",scale_units="xy",scale=1, width=1)
                                DISPLAY_MASK(first_poly_0_R, second_poly_0_R, third_poly_0_R, fourth_poly_0_R)
                                DISPLAY_MASK(first_poly_1_R, second_poly_1_R, third_poly_1_R, fourth_poly_1_R)
                                DISPLAY_MASK(first_poly_2_R, second_poly_2_R, third_poly_2_R, fourth_poly_2_R)
                else:
                    continue



    if len(All_reflected_routes) > 0:
        # route return this -> score, cue_to_wall_v, [final_hitpoint_x, final_hitpoint_y]
        score = []
        for route in All_reflected_routes:
            tempscore = route[0]
            score.append(tempscore)

        print("ALL REFLECTED ROUTE SCORE:", score)
        best_route_index = score.index(max(score))
        print("Best reflected Route:", All_reflected_routes[best_route_index])
        score, cuetoi_v, hitpoint = All_reflected_routes[best_route_index]
        # check obstacle
        first_poly, second_poly, third_poly, fourth_poly = end_effector_mask(cuex, cuey, cuetoi_v[0], cuetoi_v[1])
        # check obstacle or outofbound
        out_flag = outofbound(hitpoint[0], hitpoint[1])
        obstacle_flag, points_in_poly = check_obstacle(first_poly, second_poly, third_poly, fourth_poly, objectballx, objectbally)
        print("obstacle flag:", obstacle_flag)
        DISPLAY_MASK(first_poly, second_poly, third_poly, fourth_poly)
        DISPLAY_OBSTACLE_BALL(who_in_cue_to_target_way, who_in_target_to_aim_way, objectballx, objectbally)
        DISPLAY_POOL_TABLE(objectballx, objectbally, cuex, cuey)
        plt.title("sim pool table")
        plt.axis([0, tablewidth, 0, tableheight])
        plt.axis("equal")
        plt.show(block=False)
        input("Enter to continue...")
        plt.pause(0.5)
        plt.cla()

        # return best reflected route
        return [0, cuetoi_v[0], cuetoi_v[1], obstacle_flag, hitpoint[0], hitpoint[1]]
    else:
        print("No valid reflected route")
        print("Going for lucky route")
        # this is a place holder
        dis, vx, vy = disandvec(objectballx[0], objectbally[0], cuex, cuey)
        hitpointx, hitpointy = findhitpoint(cuex, cuey, vx, vy)
        first_poly, second_poly, third_poly, fourth_poly = end_effector_mask(cuex, cuey, vx, vy)
        # check obstacle or outofbound
        out_flag = outofbound(hitpointx, hitpointy)
        obstacle_flag, points_in_poly = check_obstacle(first_poly, second_poly, third_poly, fourth_poly, objectballx, objectbally)
        obstacle_flag = obstacle_flag or out_flag
        print("obstacle flag:", obstacle_flag)
        plt.cla()
        return [0, vx, vy, obstacle_flag, hitpointx, hitpointy]

if __name__ == '__main__':

    illogical = 1
    while illogical:
        cuex, cuey, objectballx, objectbally, n = generateballs(5)
        # objectballx.append(cuex)
        # objectbally.append(cuey)
        print("number of balls:",n)
        print("objectball x axis:",objectballx)
        print("objectball y axis:",objectbally)

        # check if distance and vectors between balls are logical(meaning they are not stacked)
        dis = []
        balltoballx = []
        balltobally = []
        k = 0
        for i in range(0,n):
            for j in range(0+k,n):
                d, x, y = disandvec(objectballx[i], objectbally[i], objectballx[j], objectbally[j])
                dis.append(d)
                balltoballx.append(x)
                balltobally.append(y)
            k=k+1
        print("distance between each balls:",dis)

        lengh = len(dis)
        mindis = min(dis)
        print("minimum in distance:",mindis)
        for i in range(0,lengh):
            if dis[i] < 2*r and dis[i] != 0:
                illogical = 1
            else:
                illogical = 0

    #############################
    '''
    objectballx.append(cuex)
    objectbally.append(cuey)
    '''
    main(objectballx, objectbally, cuex, cuey)
