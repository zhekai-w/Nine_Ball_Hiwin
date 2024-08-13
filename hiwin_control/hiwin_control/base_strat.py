import matplotlib.pyplot as plt
import matplotlib.path as mplPath
from matplotlib.patches import Polygon as MatplotlibPolygon
from shapely.geometry import Polygon, Point, LineString
import random
import numpy as np
import math
import time
from typing import Tuple

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

def route(cue=[0, 0], cuetoivector=[0, 0], itok2vector=[0, 0] ,k2tok1vector=[0, 0], toholevector=[0, 0],n=0):
    # A·B =|A||B|cos(θ)
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


def DISPLAY_OBSTACLE_BALL(who_in_cue_to_target_way, who_in_target_to_aim_way, objectballx, objectbally) -> None:
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

def main(objectballx, objectbally, cuex, cuey):
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

if __name__ == "__main__":
    main()
