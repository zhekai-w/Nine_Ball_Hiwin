import matplotlib.pyplot as plt
import matplotlib.path as mplPath
from matplotlib.patches import Polygon as MatplotlibPolygon
from shapely.geometry import Polygon, Point, LineString
import random
import numpy as np
import math
import time

# define table height width
# tablewidth = 1920
# tableheight = 932
tablewidth = 627
tableheight = 304

# actual table height and width
actualwidth = 627
actualheight = 304

# radius of balls (30.4cm: 1.6cm = 932pixels : 97.5pixels)
# R = 1.6/actualheight*tableheight
# r = round(R) #97
r = 16
R = 16

#radius of holes (62.6cm : 1920pixels = 2cm : 60pixels)
# RB = tablewidth/actualwidth*2
# rb = round(RB)
rb = 20

TOP_LEFT = [-296.364, 592.533]

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
    x = toballx-fromballx
    y = tobally-frombally
    d = math.sqrt(abs(x)**2+abs(y)**2)
    #round for the sake of visual, don't round it for accuracy
    d = round(d,2)
    return d, x, y

# GENERATE RANDOM NUMBER TO SIMULATE BALL LOCATION
def generateballs(numberofballs, r):
    print("number of balls:",numberofballs)

    # generate cue ball
    cuex = random.uniform(aimpointx[0], aimpointx[3])
    cuex = round(cuex, 2)
    cuey = random.uniform(aimpointy[0], aimpointy[1])
    cuey = round(cuey, 2)


    # generate cue ball location
    objectballx = []
    objectbally = []
    for _ in range(0,numberofballs):
        x = random.uniform(aimpointx[0], aimpointx[3])
        objectballx.append(round(x, 2))
        y = random.uniform(aimpointy[0], aimpointy[1])
        objectbally.append(round(y, 2))
    return cuex, cuey, objectballx, objectbally, numberofballs

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

#make this a class with less in put(max input cue, objectballi, objectballk2, objectballk1, aimpoint, n)
def route(cue, cuetoivector, objectballi, itok2vector, objectballk2 ,k2tok1vector, objectballk1, toholevector,n):
    #fix cuefinalvector
    score = None
    cuefinalvector = None
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

    return score,cuefinalvector,cue,cuetoivector, objectballi, itok2vector, objectballk2 ,k2tok1vector, objectballk1, toholevector,n

def route_process(ValidRoutes, bestrouteindex, obstacle_flag):
    best_route = ValidRoutes[bestrouteindex]
    score = best_route[0]
    vx = best_route[3][0]
    vy = best_route[3][1]
    cuex = best_route[2][0]
    cuey = best_route[2][1]
    hitpointx, hitpointy = findhitpoint(cuex, cuey, vx, vy)
    return [score, vx, vy, obstacle_flag, hitpointx, hitpointy]


def check_obstacle(ballx, bally, vectorx, vectory, objx, objy):
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
    l = len(objx)
    for i in range(l):
        shapely_point = Point(objx[i], objy[i])
        if polygon.contains(shapely_point):
            points_inside.append((objx[i], objy[i]))
            obstacle_flag = 1
    return obstacle_flag, points_inside

def draw_end_effector_shadow(ballx, bally, vectorx, vectory):
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


def main(objectballx, objectbally, cuex, cuey):
    start_time = time.time()
    inholeindex = []
    n = len(objectballx)
    for i in range(0,n): #because cue ball is in objectball[-1]
        distohole = ballinhole(objectballx[i], objectbally[i])
        if distohole < rb:
            print("objectball[%d] is in hole\n"%i)
            inholeindex.append(i)
            # print("objectball[%d] is deleted\n"%i)
        else:
            print("objectball[%d] is out of hole\n"%i)

    for j in range(0, len(inholeindex)):
        del objectballx[inholeindex[j]]
        del objectbally[inholeindex[j]]
        print("objectball[%d] is deleted\n"%j)

    n = len(objectballx)

    # Plot vector from each objectballs to each aiming point
    balltoholedis = []*6
    Vx = []*6
    Vy = []*6
    all_balltoholedis = []*n
    all_vectors_BHx = []*n
    all_vectors_BHy = []*n
    cuetohitx = []*6
    cuetohity = []*6
    all_cuetohitx = []*n
    all_cuetohity = []*n
    c=['red','orange','black','green','blue','purple']

    for j in range(0,n):
        for i in range(0,6):
            dis, vx, vy = disandvec(aimpointx[i],aimpointy[i],objectballx[j],objectbally[j])
            balltoholedis.append(dis)
            Vx.append(vx)
            Vy.append(vy)

            hitx, hity = findhitpoint(objectballx[j],objectbally[j],vx,vy)
            _,tempcuetohitx, tempcuetohity = disandvec(hitx,hity,cuex,cuey)
            cuetohitx.append(tempcuetohitx)
            cuetohity.append(tempcuetohity)

        all_balltoholedis.append(balltoholedis)
        all_vectors_BHx.append(Vx)
        all_vectors_BHy.append(Vy)
        all_cuetohitx.append(cuetohitx)
        all_cuetohity.append(cuetohity)
        balltoholedis = []*6
        Vx = []*6
        Vy = []*6
        cuetohitx = []*6
        cuetohity = []*6

    # print("all vectors ball to hole x:\n",all_vectors_BHx)
    # print("all vectors ball to hole y:\n",all_vectors_BHy)

    """
    #plot vector from aiming point to hole
    for i in range(0,6):
        plt.quiver(aimpointx[i],aimpointy[i],aimtoholex[i],aimtoholey[i],color='red',units="xy",angles="xy",scale_units="xy",scale=1, width=1)

    #Draw vector from ball to aiming point and cueball to hitpoint
    for i in range(0,n):
        for j in range(0,6):
            plt.quiver(objectballx[i],objectbally[i],all_vectors_BHx[i][j],all_vectors_BHy[i][j],color=c[j],units="xy",angles="xy",scale_units="xy",scale=1, width=1)
            plt.quiver(cuex,cuey,all_cuetohitx[i][j],all_cuetohity[i][j],color='black',units="xy",angles="xy",scale_units="xy",scale=1, width=2,alpha=0.5)



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
    for i in range(len(objectballx)-1):
        objectball = plt.Circle((objectballx[i], objectbally[i]),
                            r, color='blue', alpha=0.5)
        plt.text(objectballx[i],objectbally[i],i,fontsize=15)
        plt.gca().add_patch(objectball)

    #plot cue ball
    plt.gca().add_patch(plt.Circle((cuex, cuey), r, color='red'))


    #plot holes
    for j in range(len(holex)):
        hole = plt.Circle((holex[j], holey[j]),
                            rb, color="black", alpha=0.7)
        #plt.text(holex[j],holey[j],j,color='white',fontsize=15)
        plt.gca().add_patch(hole)

    plt.title("sim pool table")
    plt.axis([0, tablewidth, 0, tableheight])
    plt.axis("equal")
    plt.show(block=False)
    # input("Enter to continue...")
    plt.pause(0.5)
    plt.cla()
    """

    #check if there are balls in between objectball and aiming point / cueball to hit point
    btball = []*n
    all_btball = []*6
    count = 0
    KinwayofI = []*n
    all_KinwayofI = []*6
    whoinway = []
    for i in range(0,n):
        for j in range(0,6):
            for k in range(0,n):
                btvdis = dottovector(objectballx[i], objectbally[i], all_vectors_BHx[i][j],all_vectors_BHy[i][j], objectballx[k], objectbally[k])
                # compare objectball[i] to aimpoint distance and objectball[i] to objectball[k] distance
                # if the previous distance is lesser than the later distance then objectball[k] is not in the way of objectball[i] to aimpoint
                disota = disandvec(aimpointx[j],aimpointy[j],objectballx[i],objectbally[i])[0]
                disoto = disandvec(objectballx[k],objectbally[k],objectballx[i],objectbally[i])[0]
                if 0 <= btvdis < 2*r and disota+R > disoto:
                    count = count+1
                    #if count = 1 or 2, record objectball[k]s is in way of vector objectball[i] to aimpoint[j](index)
                    # Better solution ? just record k and let the index of all_KinwayofI do the rest(meaning k is in who's way)
                    whoinway.append(k)

            btball.append(count)
            count = 0
            KinwayofI.append(whoinway)
            whoinway = []
        all_btball.append(btball)
        btball = []*n
        all_KinwayofI.append(KinwayofI)
        KinwayofI = []*n

    print("how many ball(s) is in way of object to hole:\n",all_btball)
    print("who is in way of this vector:\n",all_KinwayofI)

    ValidRoute = []
    #route(cuetoivector, itok2vector, k2tok1vector, toholevector,n):
    #plot vectors from objectballs to holes which have no balls between
    for i in range(0,n):
        for j in range(0,6):
            if all_btball[i][j] == 0:
                #check if there is ball in way of cueball to hitpoint/check hitpoint out of bound ?
                hitx,hity = findhitpoint(objectballx[i],objectbally[i],all_vectors_BHx[i][j],all_vectors_BHy[i][j])
                temx = hitx-cuex
                temy = hity-cuey
                dotproduct = all_vectors_BHx[i][j]*temx + all_vectors_BHy[i][j]*temy
                BH_dis = math.sqrt((all_vectors_BHx[i][j])**2+(all_vectors_BHy[i][j])**2)
                temp_dis = math.sqrt((temx)**2+(temy)**2)
                #check if there is/are ball(s) in between cue to hit point
                for k in range(0,n):
                    CtoIdis = dottovector(cuex,cuey,temx,temy,objectballx[k],objectbally[k])
                    disCtoI = math.sqrt(abs(temx)**2+abs(temy)**2)
                    disCtoK = disandvec(objectballx[k],objectbally[k],cuex,cuey)[0]
                    if 0 <= CtoIdis < 2*r and disCtoK < disCtoI+R:
                        ballinwayCI0 = 1
                        break
                    else:
                        ballinwayCI0 = 0
                # dotproduct/(BH_dis*temp_dis) > math.cos(4/9*math.pi)
                #if no ball in cue to hitpoint and both vectors' angle smaller than 90 degrees and hitpoint is not out of bound
                if ballinwayCI0 == 0 and dotproduct > 0 and outofbound(hitx,hity) == 0:
                    plt.quiver(objectballx[i],objectbally[i],all_vectors_BHx[i][j],all_vectors_BHy[i][j],color='green',units="xy",angles="xy",scale_units="xy",scale=1, width=1)
                    plt.quiver(cuex,          cuey,          temx,temy,color='green',units="xy",angles="xy",scale_units="xy",scale=1, width=1)
                    temproute = route(cue=[cuex,cuey],cuetoivector=[temx, temy], objectballi=[objectballx[i],objectbally[i]],
                                      toholevector=[all_vectors_BHx[i][j],all_vectors_BHy[i][j]],n=0,
                                      itok2vector=[0,0],objectballk2=[0,0],k2tok1vector=[0,0],objectballk1=[0,0])

                    ValidRoute.append(temproute)


            if all_btball[i][j] == 1:
                #check objectball[k] to hitpoint (ball_btball[k][j])
                k = all_KinwayofI[i][j][0]
                if all_btball[k][j] == 0:
                    #draw objectball[j] to objectball[k]'s hitpoint
                    hitkx,hitky = findhitpoint(objectballx[k],objectbally[k],all_vectors_BHx[k][j],all_vectors_BHy[k][j])
                    temkx = hitkx-objectballx[i]
                    temky = hitky-objectbally[i]
                    dotproductk = all_vectors_BHx[k][j]*temkx + all_vectors_BHy[k][j]*temky
                    for l in range(0,n):
                        tempItoKdis = dottovector(objectballx[i],objectbally[i],temkx,temky,objectballx[l],objectbally[l])
                        disItoK = math.sqrt(abs(temkx)**2+abs(temky)**2)
                        disItoL = disandvec(objectballx[l],objectbally[l],objectballx[i],objectbally[i])[0]
                        if 0 <= tempItoKdis < 2*r and disItoL < disItoK+R:
                            ballinwayIK = 1
                            break
                        else:
                            ballinwayIK = 0
                    if  ballinwayIK == 0 and dotproductk > 0 and outofbound(hitkx,hitky) == 0:
                        #plt.quiver(objectballx[i],objectbally[i],temkx,temky,color='blue',units="xy",angles="xy",scale_units="xy",scale=1, width=5)
                        #draw cue to objectball[i]'s hitpoint
                        hitix, hitiy = findhitpoint(objectballx[i],objectbally[i],temkx,temky)
                        temix = hitix - cuex
                        temiy = hitiy - cuey
                        dotproducti = temix*temkx + temiy*temky
                        for m in range(0,n):
                            tempCtoKdis = dottovector(cuex,cuey,temix,temiy,objectballx[m],objectbally[m])
                            disCtoI = math.sqrt(abs(temix)**2+abs(temiy)**2)
                            disCtoM = disandvec(cuex,cuey,objectballx[m],objectbally[m])[0]
                            if 0 <= tempCtoKdis < 2*r and disCtoM < disCtoI+R:
                                ballinwayCI1 = 1
                                break
                            else:
                                ballinwayCI1 = 0
                        if  ballinwayCI1 == 0 and dotproducti > 0 and outofbound(hitix, hitiy) == 0:
                            plt.quiver(objectballx[k],objectbally[k],all_vectors_BHx[k][j],all_vectors_BHy[k][j],color='blue',units="xy",angles="xy",scale_units="xy",scale=1, width=1)
                            plt.quiver(objectballx[i],objectbally[i],temkx,temky,color='blue',units="xy",angles="xy",scale_units="xy",scale=1, width=2)
                            plt.quiver(cuex,cuey,temix,temiy,color='blue',units="xy",angles="xy",scale_units="xy",scale=1, width=1)
                            temproute = route(cue=[cuex,cuey],cuetoivector=[temix, temiy], objectballi=[objectballx[i],objectbally[i]],itok2vector=[temkx,temky],
                                              objectballk2=[objectballx[k],objectbally[k]],toholevector=[all_vectors_BHx[k][j],all_vectors_BHy[k][j]],n=1,
                                              k2tok1vector=[0,0],objectballk1=[0,0])
                            ValidRoute.append(temproute)


            if all_btball[i][j] == 2:
                k1 = all_KinwayofI[i][j][0]
                k2 = all_KinwayofI[i][j][1]

                #to decide who is closer to objectball[j]. Need to compare (k1 to i dis) and (k2 to i dis) otherwise the vector could be reversed
                #DEFINE k1 is closer to hole and k2 is closer to j
                k1dis = disandvec(objectballx[k1],objectbally[k1],objectballx[i],objectbally[i])[0]
                k2dis = disandvec(objectballx[k2],objectbally[k2],objectballx[i],objectbally[i])[0]
                if k1dis > k2dis:
                    k1 = k1
                    k2 = k2
                elif k1dis < k2dis:
                    temp = k1
                    k1 = k2
                    k2 = temp
                elif k1dis == k2dis:
                    #compare (k1 to hole dis) and (k2 to hole dis), use the shortest
                    k1toadis = disandvec(aimpointx[j],aimpointy[j],objectballx[k1],objectbally[k1])[0]
                    k2toadis = disandvec(aimpointx[j],aimpointy[j],objectballx[k2],objectbally[k2])[0]
                    if k1toadis >= k2toadis:
                        temp = k1
                        k1 = k2
                        k2 = temp
                    elif k1toadis < k2toadis:
                        k1 = k1
                        k2 = k2
                #start to find valid route
                if all_btball[k1][j] == 0 and all_btball[k2][j] == 0:
                    hitk1xpere, hitk1ypere = findhitpoint(objectballx[k1],objectbally[k1],all_vectors_BHx[k1][j],all_vectors_BHy[k1][j])
                    hitk2xpere, hitk2ypere = findhitpoint(objectballx[k2],objectbally[k2],all_vectors_BHx[k2][j],all_vectors_BHy[k2][j])
                    #objectballi to both hitpoints
                    temk1xpere = hitk1xpere-objectballx[i]
                    temk1ypere = hitk1ypere-objectbally[i]
                    temk2xpere = hitk2xpere-objectballx[i]
                    temk2ypere = hitk2ypere-objectbally[i]
                    dotproductK1 = all_vectors_BHx[k1][j]*temk1xpere + all_vectors_BHy[k1][j]*temk1ypere
                    dotproductK2 = all_vectors_BHx[k2][j]*temk2xpere + all_vectors_BHy[k2][j]*temk2ypere
                    #2 interrupting ball but only kiss one ball
                    #K1
                    for p in range(0,n):
                        tempItoK1dis = dottovector(objectballx[k1],objectbally[k1],temk1xpere,temk1ypere,objectballx[p],objectbally[p])
                        disItoK1 = math.sqrt(abs(temk1xpere)**2+abs(temk1ypere)**2)
                        disItoP = disandvec(objectballx[p],objectbally[p],objectballx[i],objectbally[i])[0]
                        if 0 <= tempItoK1dis < 2*r and disItoP < disItoK1+R:
                            ballinwayItoK1 = 1
                            break
                        else:
                            ballinwayItoK1 = 0
                    if ballinwayItoK1 == 0 and dotproductK1 > 0 and outofbound(hitk1xpere, hitk1ypere) == 0:
                        hitix, hitiy = findhitpoint(objectballx[i],objectbally[i],temk1xpere,temk1ypere)
                        temix = hitix - cuex
                        temiy = hitiy - cuey
                        dotproducti = temix*temk1xpere + temiy*temk1ypere
                        for o in range(0,n):
                            tempCtoK1dis = dottovector(cuex,cuey,temix,temiy,objectballx[o],objectbally[o])
                            disCtoI = math.sqrt(abs(temix)**2+abs(temiy)**2)
                            disCtoO = disandvec(cuex,cuey,objectballx[o],objectbally[o])[0]
                            if 0 <= tempCtoK1dis < 2*r and disCtoO < disCtoI+R:
                                ballinwayCI2 = 1
                                break
                            else:
                                ballinwayCI2 = 0
                        if  ballinwayCI2 == 0 and dotproducti > 0 and outofbound(hitix, hitiy) == 0:
                            plt.quiver(objectballx[k1],objectbally[k1],all_vectors_BHx[k1][j],all_vectors_BHy[k1][j],color='brown',units="xy",angles="xy",scale_units="xy",scale=1, width=2)
                            plt.quiver(objectballx[i],objectbally[i],temk1xpere,temk1ypere,color='brown',units="xy",angles="xy",scale_units="xy",scale=1, width=2)
                            plt.quiver(cuex,cuey,temix,temiy,color='brown',units="xy",angles="xy",scale_units="xy",scale=1, width=1)
                            temproute = route(cue=[cuex,cuey],cuetoivector=[temix, temiy], objectballi=[objectballx[i],objectbally[i]],itok2vector=[temk1xpere,temk1ypere],
                                              objectballk2=[objectballx[k1],objectbally[k1]],toholevector=[all_vectors_BHx[k1][j],all_vectors_BHy[k1][j]],n=1,
                                              k2tok1vector=[0,0],objectballk1=[0,0])
                            ValidRoute.append(temproute)
                    #K2
                    for p in range(0,n):
                        tempItoK2dis = dottovector(objectballx[k2],objectbally[k2],temk2xpere,temk2ypere,objectballx[p],objectbally[p])
                        disItoK2 = math.sqrt(abs(temk2xpere)**2+abs(temk2ypere)**2)
                        disItoP = disandvec(objectballx[p],objectbally[p],objectballx[i],objectbally[i])[0]
                        if 0 <= tempItoK2dis < 2*r and disItoP < disItoK2+R:
                            ballinwayItoK2 = 1
                            break
                        else:
                            ballinwayItoK2 = 0
                    if ballinwayItoK2 == 0 and dotproductK2 > 0 and outofbound(hitk2xpere, hitk2ypere) == 0:
                        hitix, hitiy = findhitpoint(objectballx[i],objectbally[i],temk2xpere,temk2ypere)
                        temix = hitix - cuex
                        temiy = hitiy - cuey
                        dotproducti = temix*temk2xpere + temiy*temk2ypere
                        for o in range(0,n):
                            tempCtoK2dis = dottovector(cuex,cuey,temix,temiy,objectballx[o],objectbally[o])
                            disCtoI = math.sqrt(abs(temix)**2+abs(temiy)**2)
                            disCtoO = disandvec(cuex,cuey,objectballx[o],objectbally[o])[0]
                            if 0 <= tempCtoK2dis < 2*r and disCtoO < disCtoI+R:
                                ballinwayCI2 = 1
                                break
                            else:
                                ballinwayCI2 = 0
                        if  ballinwayCI2 == 0 and dotproducti > 0 and outofbound(hitix, hitiy) == 0:
                            plt.quiver(objectballx[k2],objectbally[k2],all_vectors_BHx[k2][j],all_vectors_BHy[k2][j],color='brown',units="xy",angles="xy",scale_units="xy",scale=1, width=2)
                            plt.quiver(objectballx[i],objectbally[i],temk2xpere,temk2ypere,color='brown',units="xy",angles="xy",scale_units="xy",scale=1, width=2)
                            plt.quiver(cuex,cuey,temix,temiy,color='brown',units="xy",angles="xy",scale_units="xy",scale=1, width=1)
                            temproute = route(cue=[cuex,cuey],cuetoivector=[temix, temiy], objectballi=[objectballx[i],objectbally[i]],itok2vector=[temk2xpere,temk2ypere],
                                              objectballk2=[objectballx[k2],objectbally[k2]],toholevector=[all_vectors_BHx[k2][j],all_vectors_BHy[k2][j]],n=1,
                                              k2tok1vector=[0,0],objectballk1=[0,0])
                            ValidRoute.append(temproute)

                if all_btball[k1][j] == 0:
                    hitk1x, hitk1y = findhitpoint(objectballx[k1],objectbally[k1],all_vectors_BHx[k1][j],all_vectors_BHy[k1][j])
                    temk1x = hitk1x-objectballx[k2]
                    temk1y = hitk1y-objectbally[k2]
                    dotproductk1 = all_vectors_BHx[k1][j]*temk1x + all_vectors_BHy[k1][j]*temk1y

                    #before checking if any ball(s) in K2 to K1, check cueball to K1
                    for l in range(0,n):
                        tempK2toK1dis = dottovector(objectballx[k2],objectbally[k2],temk1x,temk1y,objectballx[l],objectbally[l])
                        disK2toK1 = math.sqrt(abs(temk1x)**2+abs(temk1y)**2)
                        disK2toL = disandvec(objectballx[l],objectbally[l],objectballx[k2],objectbally[k2])[0]
                        if 0 <= tempK2toK1dis < 2*r and disK2toL < disK2toK1+R:
                            ballinwayIK1 = 1
                            break
                        else:
                            ballinwayIK1 = 0
                    if ballinwayIK1 == 0 and dotproductk1 > 0 and outofbound(hitk1x, hitk1y) == 0:
                        hitk2x, hitk2y = findhitpoint(objectballx[k2],objectbally[k2],temk1x,temk1y)
                        temk2x = hitk2x-objectballx[i]
                        temk2y = hitk2y-objectbally[i]
                        dotproductk2 = temk1x*temk2x + temk1y*temk2y
                        for m in range(0,n):
                            tempItoK2dis = dottovector(objectballx[i],objectbally[i],temk2x,temk2y,objectballx[m],objectbally[m])
                            disItoK2 = math.sqrt(abs(temk2x)**2+abs(temk2y)**2)
                            disItoM = disandvec(objectballx[m],objectbally[m],objectballx[k2],objectbally[k2])[0]
                            if 0 <= tempK2toK1dis < 2*r and disItoM < disItoK2+R:
                                ballinwayIK2 = 1
                                break
                            else:
                                ballinwayIK2 = 0
                        if  ballinwayIK2 == 0 and dotproductk2 > 0 and outofbound(hitk2x, hitk2y) == 0:
                            #plt.quiver(objectballx[i],objectbally[i],temkx,temky,color='blue',units="xy",angles="xy",scale_units="xy",scale=1, width=5)
                            #draw cue to objectball[i]'s hitpoint
                            hitix, hitiy = findhitpoint(objectballx[i],objectbally[i],temk2x,temk2y)
                            temix = hitix - cuex
                            temiy = hitiy - cuey
                            dotproducti = temix*temk2x + temiy*temk2y
                            for o in range(0,n):
                                tempCtoKdis = dottovector(cuex,cuey,temix,temiy,objectballx[o],objectbally[o])
                                disCtoI = math.sqrt(abs(temix)**2+abs(temiy)**2)
                                disCtoO = disandvec(cuex,cuey,objectballx[o],objectbally[o])[0]
                                if 0 <= tempCtoKdis < 2*r and disCtoO < disCtoI+R:
                                    ballinwayCI2 = 1
                                    break
                                else:
                                    ballinwayCI2 = 0
                            if  ballinwayCI2 == 0 and dotproducti > 0 and outofbound(hitix, hitiy) == 0:
                                plt.quiver(objectballx[k1],objectbally[k1],all_vectors_BHx[k1][j],all_vectors_BHy[k1][j],color='red',units="xy",angles="xy",scale_units="xy",scale=1, width=2)
                                plt.quiver(objectballx[k2],objectbally[k2],temk1x,temk1y,color='red',units="xy",angles="xy",scale_units="xy",scale=1, width=2)
                                plt.quiver(objectballx[i],objectbally[i],temk2x,temk2y,color='red',units="xy",angles="xy",scale_units="xy",scale=1, width=2)
                                plt.quiver(cuex,cuey,temix,temiy,color='red',units="xy",angles="xy",scale_units="xy",scale=1, width=1)
                                temproute = route(cue=[cuex,cuey],cuetoivector=[temix, temiy], objectballi=[objectballx[i],objectbally[i]],itok2vector=[temk2x,temk2y],
                                                  objectballk2=[objectballx[k2],objectbally[k2]],k2tok1vector=[temk1x,temk1y], objectballk1=[objectballx[k1],objectbally[k1]],
                                                  toholevector=[all_vectors_BHx[k1][j],all_vectors_BHy[k1][j]],n=2)
                                # temproute[0] = 0
                                ValidRoute.append(temproute)

    countN = [0]*6
    who1 = []
    who2 = []
    who3 = []
    who4 = []
    who5 = []
    who6 = []
    who = []
    #Check if ValidRoute is empty
    Numberofroute = len(ValidRoute)
    if Numberofroute == 0:
        print("No valid route, start searching for lucky ball")
        #Method: cut table into six portion and look for the most dense area and meximum effort to that area
        for i in range(0,n):
            if TOP_LEFT[0] <= objectballx[i] <= TOP_LEFT[0]+(tablewidth/7)*3 and TOP_LEFT[1]-tableheight*2/3 <= objectbally[i] <= TOP_LEFT[1]:
                countN[0] = countN[0] + 1
                who1.append(i)
            if TOP_LEFT[0]+(tablewidth/7)*2 <= objectballx[i] <= TOP_LEFT[0]+(tablewidth/7)*5 and TOP_LEFT[1]-tableheight*2/3 <= objectbally[i] <= TOP_LEFT[1]:
                countN[1] = countN[1] + 1
                who2.append(i)
            if TOP_LEFT[0]+(tablewidth/7)*4 <= objectballx[i] <= TOP_LEFT[0]+tablewidth and TOP_LEFT[1]-tableheight*2/3 <= objectbally[i] <= TOP_LEFT[1]:
                countN[2] = countN[2] + 1
                who3.append(i)
            if TOP_LEFT[0]+(tablewidth/7)*4 <= objectballx[i] <= TOP_LEFT[0]+tablewidth and TOP_LEFT[1]-tableheight <= objectbally[i] <= TOP_LEFT[1]-tableheight*1/3:
                countN[3] = countN[3] + 1
                who4.append(i)
            if TOP_LEFT[0]+(tablewidth/7)*2 <= objectballx[i] <= TOP_LEFT[0]+(tablewidth/7)*5 and TOP_LEFT[1]-tableheight <= objectbally[i] <= TOP_LEFT[1]-tableheight*1/3:
                countN[4] = countN[4] + 1
                who5.append(i)
            if TOP_LEFT[0] <= objectballx[i] <= TOP_LEFT[0]+(tablewidth/7)*3 and TOP_LEFT[1]-tableheight <= objectbally[i] <= TOP_LEFT[1]-tableheight*1/3:
                countN[5] = countN[5] + 1
                who6.append(i)
        who.append(who1)
        who.append(who2)
        who.append(who3)
        who.append(who4)
        who.append(who5)
        who.append(who6)

        print("area 1:",countN[0])
        print("area 2:",countN[1])
        print("area 3:",countN[2])
        print("area 4:",countN[3])
        print("area 5:",countN[4])
        print("area 6:",countN[5])
        print("most dense area:",countN.index(max(countN)))
        print("Number of ball in this area:",max(countN))
        print("who is in this area:",who[countN.index(max(countN))])
        #form route from closest ball in most dense area
        thisareadis = []
        for i in range(0,len(who[countN.index(max(countN))])):
            tempdis = disandvec(objectballx[who[countN.index(max(countN))][i]],objectbally[who[countN.index(max(countN))][i]],cuex, cuey)[0]
            thisareadis.append(tempdis)

        # find the second smallest element because the smallest element is zero(meaning cueball itself)
        # for i in range(0, len(thisareadis)):

        print("this area all dis:",thisareadis)


        luckyindex = who[countN.index(max(countN))][thisareadis.index(min(thisareadis))]
        luckyvectorx = objectballx[luckyindex] - cuex
        luckyvectory = objectbally[luckyindex] - cuey
        print('lucky index', luckyindex)
        print('lucky ball x:', objectballx[luckyindex])
        print('lucky ball y:', objectbally[luckyindex])

        luckyroute = route(cue=[cuex,cuey],cuetoivector=[luckyvectorx, luckyvectory], objectballi=[objectballx[luckyindex],objectbally[luckyindex]],
                                      toholevector=[1,1],n=-1,
                                      itok2vector=[0,0],objectballk2=[0,0],k2tok1vector=[0,0],objectballk1=[0,0])
        # luckyroute[0] = -6000
        ValidRoute.append(luckyroute)

    """
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

    #plot vector from aiming point to hole
    for i in range(0,6):
        plt.quiver(aimpointx[i],aimpointy[i],aimtoholex[i],aimtoholey[i],color='red',units="xy",angles="xy",scale_units="xy",scale=1, width=3)

    #PLOT ALL BALLS AND HOLES
        #plot objectballs
    for i in range(len(objectballx)-1):
        objectball = plt.Circle((objectballx[i], objectbally[i]),
                            r, color='blue', alpha=0.5)
        plt.text(objectballx[i],objectbally[i],i,fontsize=15)
        plt.gca().add_patch(objectball)

    #plot cue ball
    plt.gca().add_patch(plt.Circle((cuex, cuey), r, color='red'))

    #plot holes
    for j in range(len(holex)):
        hole = plt.Circle((holex[j], holey[j]),
                            rb, color="black", alpha=0.7)
        #plt.text(holex[j],holey[j],j,color='white',fontsize=15)
        plt.gca().add_patch(hole)

    plt.title("strategy possible route")
    plt.axis([0, tablewidth, 0, tableheight])
    plt.axis("equal")
    plt.show(block=False)
    # input("Enter to continue...")
    plt.pause(0.5)
    plt.cla()
    """

    #plot the best route
    #return score,cuefinalvector,cue,cuetoivector, objectballi, itok2vector, objectballk2 ,k2tok1vector, objectballk1, toholevector,n
    score = []
    print("Number of valid route:",len(ValidRoute))
    for i in range(0,len(ValidRoute)):
        tempscore = ValidRoute[i][0]
        score.append(tempscore)

    bestrouteindex = score.index(max(score))
    print("all score:",score)
    print("best score:",max(score))
    print("best route index:",bestrouteindex)

    Nofinterruptball = ValidRoute[bestrouteindex][-1]
    if Nofinterruptball == 0:
        plt.quiver(ValidRoute[bestrouteindex][4][0],ValidRoute[bestrouteindex][4][1],ValidRoute[bestrouteindex][-2][0],ValidRoute[bestrouteindex][-2][1],color='green',units="xy",angles="xy",scale_units="xy",scale=1, width=1)
        plt.quiver(cuex,cuey,ValidRoute[bestrouteindex][3][0],ValidRoute[bestrouteindex][3][1],color='green',units="xy",angles="xy",scale_units="xy",scale=1, width=1)
        #final cuevector
        #plt.quiver(cuex+ValidRoute[bestrouteindex][3][0],cuey+ValidRoute[bestrouteindex][3][1],ValidRoute[bestrouteindex][2][0],ValidRoute[bestrouteindex][2][1],color='green',units="xy",angles="xy",scale_units="xy",scale=1, width=3)
    elif Nofinterruptball == 1:
        plt.quiver(ValidRoute[bestrouteindex][6][0],ValidRoute[bestrouteindex][6][1],ValidRoute[bestrouteindex][-2][0],ValidRoute[bestrouteindex][-2][1],color='red',units="xy",angles="xy",scale_units="xy",scale=1, width=2)
        plt.quiver(ValidRoute[bestrouteindex][4][0],ValidRoute[bestrouteindex][4][1],ValidRoute[bestrouteindex][5][0],ValidRoute[bestrouteindex][5][1],color='red',units="xy",angles="xy",scale_units="xy",scale=1, width=2)
        plt.quiver(cuex,cuey,ValidRoute[bestrouteindex][3][0],ValidRoute[bestrouteindex][3][1],color='red',units="xy",angles="xy",scale_units="xy",scale=1, width=1)
    elif Nofinterruptball == 2:
        plt.quiver(ValidRoute[bestrouteindex][8][0],ValidRoute[bestrouteindex][8][1],ValidRoute[bestrouteindex][9][0],ValidRoute[bestrouteindex][9][1],color='blue',units="xy",angles="xy",scale_units="xy",scale=1, width=2)
        plt.quiver(ValidRoute[bestrouteindex][6][0],ValidRoute[bestrouteindex][6][1],ValidRoute[bestrouteindex][7][0],ValidRoute[bestrouteindex][7][1],color='blue',units="xy",angles="xy",scale_units="xy",scale=1, width=2)
        plt.quiver(ValidRoute[bestrouteindex][4][0],ValidRoute[bestrouteindex][4][1],ValidRoute[bestrouteindex][5][0],ValidRoute[bestrouteindex][5][1],color='blue',units="xy",angles="xy",scale_units="xy",scale=1, width=2)
        plt.quiver(cuex,cuey,ValidRoute[bestrouteindex][3][0],ValidRoute[bestrouteindex][3][1],color='blue',units="xy",angles="xy",scale_units="xy",scale=1, width=1)


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

    #plot vector from aiming point to hole
    for i in range(0,6):
        plt.quiver(aimpointx[i],aimpointy[i],aimtoholex[i],aimtoholey[i],color='red',units="xy",angles="xy",scale_units="xy",scale=1, width=1)

    #PLOT ALL BALLS AND HOLES
        #plot objectballs
    for i in range(len(objectballx)-1):
        objectball = plt.Circle((objectballx[i], objectbally[i]),
                            r, color='blue', alpha=0.5)
        plt.text(objectballx[i],objectbally[i],i,fontsize=15)
        plt.gca().add_patch(objectball)

    #plot cue ball
    plt.gca().add_patch(plt.Circle((cuex, cuey), r, color='red'))

    #plot holes
    for j in range(len(holex)):
        hole = plt.Circle((holex[j], holey[j]),
                            rb, color="black", alpha=0.7)
        #plt.text(holex[j],holey[j],j,color='white',fontsize=15)
        plt.gca().add_patch(hole)

    #plot end effector shadow
    first_poly, second_poly, third_poly, fourth_poly = draw_end_effector_shadow(cuex,cuey,ValidRoute[bestrouteindex][3][0],ValidRoute[bestrouteindex][3][1])

    obstacle_flag, points_inside = check_obstacle(cuex,cuey,ValidRoute[bestrouteindex][3][0],ValidRoute[bestrouteindex][3][1],objectballx, objectbally)
    if obstacle_flag==1:
        x_inside, y_inside = zip(*points_inside)
        plt.scatter(x_inside, y_inside, c="green")

    print("obstacle in way:", obstacle_flag)

    polygon_vertices = [first_poly, second_poly, third_poly, fourth_poly]
    polygon = MatplotlibPolygon(polygon_vertices, closed=True, edgecolor='blue', facecolor='none')
    plt.gca().add_patch(polygon)
    # #colored background
    # plt.axvspan(0,(tablewidth/7)*3,facecolor='b',alpha=0.3)
    # plt.axvspan((tablewidth/7)*2,(tablewidth/7)*5,facecolor='g',alpha=0.3)
    # plt.axvspan((tablewidth/7)*4,tablewidth,facecolor='y',alpha=0.3)


    plt.title("best route")
    plt.axis([0, tablewidth, 0, tableheight])
    plt.axis("equal")
    plt.show(block=False)
    input("Enter to continue...")
    # plt.pause(0.5)
    plt.cla()
    # end_time = time.time()
    # print("Execution time:", end_time - start_time, "seconds")

    return ValidRoute, bestrouteindex, obstacle_flag

if __name__ == '__main__':
    # # objectball[-1] is cue ball
    # objectballx = [300,300,300,300,300,300+2*r,300+2*r,300+2*r,300+2*r,300+4*r,300+4*r,300+4*r,300+6*r,300+6*r,300+8*r]
    # objectbally = [457,457+2*r,457+4*r,457-2*r,457-4*r,457+r,457+3*r,457-r,457-3*r,457,457+2*r,457-2*r,457+r,457-r,457]
    # cuex = 1620
    # cuey = 457
    # n = 15
    ####################### for testing use
    cuex = None
    cuey = None
    objectballx = None
    objectbally = None
    n = 0
    illogical = 1
    while illogical:
        cuex, cuey, objectballx, objectbally, n = generateballs(10, r)
        objectballx.append(cuex)
        objectbally.append(cuey)
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
                d, x, y = disandvec(objectballx[j+1], objectbally[j+1], objectballx[i], objectbally[i])
                dis.append(d)
                balltoballx.append(x)
                balltobally.append(y)
            k=k+1
        print("distance between each balls:",dis)

        flag = 0
        lengh = len(dis)
        mindis = min(dis)
        print("minimum in distance:",mindis)
        for i in range(0,lengh):
            if dis[i] < 2*r:
                flag = flag + 1
        if flag == 0:
            illogical = 0
        else:
            illogical = 1
    #############################
    '''
    objectballx.append(cuex)
    objectbally.append(cuey)
    '''
    ValidRoute, bestrouteindex, obstacle_flag = main(objectballx, objectbally, cuex, cuey)
    # Process route for newer arm controller
    score, vx, vy, obstacle_flag, hitpointx, hitpointy = route_process(ValidRoute, bestrouteindex, obstacle_flag)
    print('Route Score:', score)
    print(f'Vector[{vx},{vy}]')
    print(f'Hit points[{hitpointx},{hitpointy}]')
    print('Obstacle Flag:', obstacle_flag)
