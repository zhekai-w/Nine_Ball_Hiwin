 
from matplotlib.patches import Polygon as MatplotlibPolygon
import random
import math
import pygame as pg,random,math,time
import sys
import pygame
# tablewidth =1920
# tableheight =932
# radius of balls (30.4cm: 1.6cm = 932pixels : 97.5pixels)
# R = 1.6/actualheight*tableheight
# r = round(R) #97
# #radius of holes (62.6cm : 1920pixels = 2cm : 60pixels)
# hole = tablewidth/actualwidth*2
# rb = round(hole)
actualwidth =62.7
actualheight=30.4
width=627
height=304
radius=int(1.6/actualheight*height)
holeradius=int(width/actualwidth*2)
#background
pygame.init()
WIDTH, HEIGHT = 1000,500
WINDOW_SIZE = (WIDTH, HEIGHT)
screen = pygame.display .set_mode(WINDOW_SIZE)
pygame.display.set_caption("table tennis")

value=0
#color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (225, 0, 0)
YELLOW = (225, 225, 0)
BLUE = (0, 128, 255)
PURPLE = (225, 0, 255)
ORANGE = (225, 128, 0)
GREEN = ( 0, 255, 0)
DARK_GREEN=(76,153,0)
BROWN = (102, 0, 0)
PINK = (255,102,102)
colorname=["yellow","blue","red","purple","orange","green","brown","black","pink"]
colors=[WHITE,YELLOW,BLUE,RED,PURPLE,ORANGE,GREEN,BROWN,BLACK,PINK]
#table left down axis
x1=100
y1=100
holenumber=[1,2,3,4,5,6]     
holex=[x1,x1+width/2,x1+width,x1,x1+width/2,x1+width]
holey=[y1,y1,y1,y1+height,y1+height,y1+height]
virholex=[x1+radius,x1+width/2,x1+width-radius,x1+radius,x1+width/2,x1+width-radius]
virholey=[y1+radius,y1+radius,y1+radius,y1+height-radius,y1+height-radius,y1+height-radius]
#distance to two ball
def disandvec(n1x,n1y,n2x,n2y):
    x=n1x-n2x
    y=n1y-n2y
    dis=math.sqrt(abs(x)**2+abs(y)**2)
    dis=round(dis,2)#unknown
    return dis,x,y
def dottovector(n1x,n1y,vectorx,vectory,dotx,doty):
    disto=math.sqrt(abs(vectorx)**2+abs(vectory)**2)
    balltoballx=dotx-n1x
    balltobally=doty-n1y
    dotproduct=vectorx*balltoballx+vectory*balltobally
    if dotproduct>=0:
        shadowlengh = dotproduct/disto
        ratio = shadowlengh/disto
        shadowx = n1x+vectorx*ratio
        shadowy = n1y+vectory*ratio
        normallengh = disandvec(dotx, doty, shadowx, shadowy)[0]
        return normallengh
    else:
        return -1
def get_ball_centers(balls):
    centers = []
    for ball in balls:
        center = (ball.x, ball.y)
        centers.append(center)
    return centers
class generateball():
    def __init__(ball,ballcolor,x,y,radius,ballnumber):
        ball.color=ballcolor
        ball.x=x
        ball.y=y
        ball.radius=radius
        ball.number=ballnumber
            
    def __str__(ball):
        return f"(x={ball.x}, y={ball.y}, number={ball.number})"

    
        #draw the ball
    def drawball(ball, screen):
        ball.number=pygame.draw.circle(screen, ball.color, (ball.x, ball.y), ball.radius)
        ball.ballcenter=ball.number.center
        return ball.ballcenter
        
    # def errorball(ball):


#需要母球及其他球位置及顏色編號

def cal_score(distance,angle,cue_objobs,obj_holeobs):
    # print("score",distance,angle,cue_objobs,obj_holeobs)
    score = ((angle * -22) + (distance * -1) + (obj_holeobs*-4000))
    if angle<0:
        score=abs(score)
    elif cue_objobs>0:
        score=abs(score)
    return score

def generate(ballcount):
    ballnumber=[]
    ballnumber=random.sample(range(1,9),ballcount)
    ballnumber.append(9)
    ballnumber.sort()
    ballcount=ballcount+1
    for i in range(0,ballcount):
        color = colors[ballnumber[i]]        
        x = random.randint(x1+radius,x1+width-radius)
        y = random.randint(y1+radius,y1+height-radius)
        balls.append(generateball(color,x,y,radius,ballnumber))
    return ballcount,ballnumber
def oneball(objcolor):
    x = random.randint(x1+radius,x1+width-radius)
    y = random.randint(y1+radius,y1+height-radius)
    pygame.draw.circle(screen,objcolor,(x,y),radius,width=radius)
    return objcolor,x,y
def checkball(x1,y1,x2,y2,radius,firstname,secondname):
    disx=x2-x1
    disy=y2-y1
    dis=math.sqrt(abs(disx)**2+abs(disy)**2)
    if dis<=radius:
        print("cover",firstname,secondname)      
def line(color,n1x,n1y,n2x,n2y,radius):
    pygame.draw.line(screen, color, (n1x,n1y),(n2x,n2y), width=radius) 
    return n1x,n1y,n2x,n2y 
def circle(x1,y1):
    pygame.draw.circle(screen,BLACK,(x1,y1),radius=15,width=15)
def vector(n1x,n1y,n2x,n2y):
    vectorx=n2x-n1x
    vectory=n2y-n1y
    return vectorx,vectory
def vector_angle(n1x,n1y,n2x,n2y,n3x,n3y):
    vx1,vy1=vector(n1x,n1y,n2x,n2y)
    vx2,vy2=vector(n2x,n2y,n3x,n3y)
    dotproduct=vx1*vx2+vy1*vy2
    magnitude1=math.sqrt(vx1**2+vy1**2)
    magnitude2=math.sqrt(vx2**2+vy2**2)
    cos=dotproduct/(magnitude1*magnitude2)
    cos = max(-1, min(1, cos))
    rad = math.acos(cos)
    deg = math.degrees(rad)
    return deg
def point_to_line_distance(px, py, x1, y1, x2, y2, radius,i, j,value):
    dx = x2 - x1
    dy = y2 - y1
    apx = px - x1
    apy = py - y1
    d_mag_squared = dx**2 + dy**2
    if d_mag_squared == 0:
        dist = math.sqrt(apx**2 + apy**2)
        closest_point = (x1, y1)
    else:
        t = (apx * dx + apy * dy) / d_mag_squared
        if t < 0:
            closest_point = (x1, y1)
            dist = math.sqrt((px - x1)**2 + (py - y1)**2)
        elif t > 1:
            closest_point = (x2, y2)
            dist = math.sqrt((px - x2)**2 + (py - y2)**2)
        else:

            qx = x1 + t * dx
            qy = y1 + t * dy
            dist = math.sqrt((px - qx)**2 + (py - qy)**2)
    #pygame.draw.line(screen,BLACK,closest_point,(px,py),3)
    # 判断是否碰撞
    if dist <= radius:
        value+=1
        return value,px,py
    return value,0,0
def find_min_negative_integer_in_nested_list(lst):
    min_negative = None
    min_position1 = None
    min_position2=None

    for i, sublist in enumerate(lst):
        for j, value in enumerate(sublist):
            if isinstance(value, (int, float)) and value < 0:
                if min_negative is None or value > min_negative:
                    min_negative = value
                    min_position1,min_position2= (i, j)
    
    return min_negative, min_position1,min_position2

def text():
    font = pygame.font.SysFont("Arial", 20)
    balltext=font.render("the ball exist:",True,BLACK)
    screen.blit(balltext,(450,50))
    for i in range(0,3):
        holenumbertop=font.render(str(holenumber[i]),True,BLACK)
        screen.blit(holenumbertop,(virholex[i],virholey[i]-50))
    for i in range(3,6):
        holenumberdown=font.render(str(holenumber[i]),True,BLACK)
        screen.blit(holenumberdown,(virholex[i],virholey[i]+50))
    for i in range(0,ballcount):
        txtexistball = font.render(str(ballnumber[i]), True, BLACK)
        screen.blit(txtexistball, (550+10*i, 50))
    for i in range(0,9):
        txtexistball = font.render((colorname[i]), True, BLACK)
        screen.blit(txtexistball, (900, 50+20*i))  
def calculate_aim_point(ball_x, ball_y, target_x, target_y, ball_diameter):
    vector_x = target_x - ball_x
    vector_y = target_y - ball_y
    length = math.sqrt(vector_x**2 + vector_y**2)
    unit_vector_x = vector_x / length
    unit_vector_y = vector_y / length
    aim_distance = 2 * ball_diameter
    aim_point_x = ball_x - unit_vector_x * aim_distance
    aim_point_y = ball_y - unit_vector_y * aim_distance
    return aim_point_x, aim_point_y

# def edge_detect(rectrange,ballx,bally):
#     if rectrange.collidepoint(ballx, bally):
#         print("點在矩形內")
#         return True
#     else:
#         print("點在矩形外")
#         return False
    
def main(cuex,cuey,objx,objy,):
    objtoholes=[]
    vxs=[]
    vys=[]
    for i in range(0,6):
        cuetoobjdis,objtocuex,objtocuey=disandvec(cuex,cuey,objx,objy)
        objtohole,objtoholevx,objtoholevy=disandvec(objx,objy,virholex[i],virholey[i])
        objtoholes.append(objtohole)
        vxs.append(objtocuex)
        vys.append(objtocuey)  
    cue_obj_holeangle=[]
    print("obj ball",objx,objy)
    for i in range(0,6):
        cue_obj_hole1=vector_angle(cuex,cuey,objx,objy,virholex[i],virholey[i])
        if cue_obj_hole1>90:
            cue_obj_holeangle.append(-cue_obj_hole1)
        else:
            cue_obj_holeangle.append(cue_obj_hole1)
    main1obstacles=[]
    main1obstacles=target_hole(hitpointxs,hitpointys,main1obstacles)
    way1scores=[]
    for i in range(0,6):
        way1score=cal_score(cuetoobjdis+objtoholes[i],cue_obj_holeangle[i],values1[i],main1obstacles[i])
        way1scores.append(way1score)
    non_positive_scores = [score for score in way1scores if score <= 0]
# 找到小於或等於0的最大分數
    if non_positive_scores:
        max_non_positive_score = non_positive_scores[0]
        for score in non_positive_scores:
            if score > max_non_positive_score:
                max_non_positive_score = score
        best_index = way1scores.index(max_non_positive_score)
        best_virholex = virholex[best_index]
        best_virholey = virholey[best_index]
        final_hitpointx = hitpointxs[best_index]
        final_hitpointy = hitpointys[best_index]
        ballx=ballx_set[best_index]
        bally=bally_set[best_index]
        bestvx=vxs[best_index]
        bestvy=vys[best_index]
        routeobs=main1obstacles[best_index]
        bestx,besty=calculate_aim_point(cuex,cuey,final_hitpointx,final_hitpointy,radius)
        pygame.draw.circle(screen,RED,(bestx,besty),3,3)
        line(WHITE, bestx, besty, final_hitpointx, final_hitpointy, 3)
        line(WHITE, objx, objy, best_virholex, best_virholey, 3)
        finalobsx=[]
        finalobsy=[]
        countobs=0
        for i in range(1,ballcount):
            countobs,px,py=point_to_line_distance(ballx_set[i],bally_set[i],objx,objy,best_virholex,best_virholey,2*radius,i,j+1,countobs)
            if px>0:
                finalobsx.append(px)
                finalobsy.append(py)
        print("finalobs",countobs,"finalobsy",finalobsx,"finalobsx",finalobsy)
        print("score", way1scores)
        print("best", max_non_positive_score)
        final(max_non_positive_score,bestvx,bestvy,routeobs,bestx,besty)
    else:
        print("沒有小於或等於0的分數")
        main2(cuex,cuey,objx,objy)

def main2(cuex,cuey,objx,objy):
    cue_obj_diss=[]
    cue_objvxs=[]
    cue_objvys=[]
    obj_tar_diss=[]
    obj_tarvxs=[]
    obj_tarvys=[]
    middlex_nums=[]
    middley_nums=[]
    pointxs=[]
    pointys=[]
    #給予計算初始化向量
    for i in range(0,6):
        cue_obj_dis,cue_obj_vx,cue_obj_vy=disandvec(cuex,cuey,hitpointxs[i],hitpointys[i])
        cue_obj_diss.append(cue_obj_dis)
        cue_objvxs.append(cue_obj_vx)
        cue_objvxs.append(cue_obj_vy)
        obj_tar_dis,obj_tar_vx,obj_tar_vy=disandvec(hitpointxs[i],hitpointys[i],objx,objy)
        obj_tar_diss.append(obj_tar_dis)
        obj_tarvxs.append(obj_tar_vx)
        obj_tarvys.append(obj_tar_vy)
        middlex_num=cue_obj_vx/2
        middley_num=cue_obj_vy/2
        middlex_nums.append(middlex_num)
        middley_nums.append(middley_num)
    print("middlex",middlex_nums)
    print("middley",middley_nums)
    pointx_groups = [
        [cuex - middlex_nums[i] for i in range(6)],
        [cuex - middlex_nums[i] for i in range(6)],
        [x1 + width for i in range(6)],
        [x1 for i in range(6)]
    ]

    pointy_groups = [
        [y1 + height for i in range(6)],
        [y1 for i in range(6)],
        [cuey - middley_nums[i] for i in range(6)],
        [cuey - middley_nums[i] for i in range(6)]
    ]
    print("pointx:", pointx_groups)
    print("pointy:", pointy_groups)
    main2obstacles1=[]
    for i in range(0,4):
        values2=[]
        for j in range(0,6):
            value2=0
            for k in range(1,ballcount):
                value2,z,z=point_to_line_distance(ballx_set[k],bally_set[k],cuex,cuey,pointx_groups[i][j],pointy_groups[i][j],2*radius+2,i+1,j,value2)
                value2,z,z=point_to_line_distance(ballx_set[k],bally_set[k],hitpointxs[i],hitpointys[i],pointx_groups[i][j],pointy_groups[i][j],2*radius+2,i+1,j,value2)
            # if hitpointxs[i]==virholex[i] and hitpointys[i]==virholey[i]:
            #     value2+1
            # if value2==0:
            #     line(GREEN,pointx_groups[i][j],pointy_groups[i][j],cuex,cuey,3)
            #     line(GREEN,hitpointxs[j],hitpointys[j],pointx_groups[i][j],pointy_groups[i][j],3)
            values2.append(value2)
        main2obstacles1.append(values2)
    print("values2",main2obstacles1)  
    all_angle2=[]
    for i in range(0,4):
        cue_obj_holeangle2=[]
        for j in range(0,6):
            cue_obj_hole1=vector_angle(pointx_groups[i][j],pointy_groups[i][j],objx,objy,virholex[j],virholey[j])
            if cue_obj_hole1>90:
                cue_obj_holeangle2.append(-cue_obj_hole1)
            else:
                cue_obj_holeangle2.append(cue_obj_hole1)
        all_angle2.append(cue_obj_holeangle2)   
    print(all_angle2)
    main2obstacles2=[]
    main2obstacles2=target_hole(hitpointxs,hitpointys,main2obstacles2)
    print("main2obs",main2obstacles2)
    print("main2cue_target_obs",main2obstacles1)
    way2scores2=[]
    for i in range(0,4):
        way2scores1=[]
        for j in range(0,6):
            score=cal_score(cue_obj_diss[j]+obj_tar_diss[j],all_angle2[i][j],main2obstacles1[i][j],main2obstacles2[j])
            if score<0:
                print(score)
                pygame.draw.line(screen,GREEN,(pointx_groups[i][j],pointy_groups[i][j]),(cuex,cuey),3)
                pygame.draw.line(screen,GREEN,(pointx_groups[i][j],pointy_groups[i][j]),(hitpointxs[j],hitpointys[j]),3) 
                pygame.draw.line(screen,GREEN,(objx,objy),(virholex[j],virholey[j]),3) 
            way2scores1.append(score)
        way2scores2.append(way2scores1) 
        print("way2score",i+1,way2scores2[i])
    bestscore, best_index1,best_index2 = find_min_negative_integer_in_nested_list(way2scores2)
    vxs2=[]
    vys2=[]
    for i in range(0,4):
        vxs1=[]
        vys1=[]
        for j in range(0,6):
            cue_point_dis,vx,vy=disandvec(cuex,cuey,pointx_groups[i][j],pointy_groups[i][j])
            vxs1.append(vx)
            vys1.append(vy)
        vxs2.append(vxs1)
        vys2.append(vxs1)
    if bestscore:
        best_virholex = virholex[best_index2]
        best_virholey = virholey[best_index2]
        final_hitpointx = hitpointxs[best_index2]
        final_hitpointy = hitpointys[best_index2]
        x=ballx_set[best_index1]
        y=bally_set[best_index1]
        bestvx=vxs2[best_index1][best_index2]
        bestvy=vys2[best_index1][best_index2]
        finalobsx=[]
        finalobsy=[]
        countobs=0
        for i in range(1,ballcount):
            countobs,px,py=point_to_line_distance(ballx_set[i],bally_set[i],objx,objy,best_virholex,best_virholey,2*radius,i,j+1,countobs)
            if px>0:
                finalobsx.append(px)
                finalobsy.append(py)
        print("finalobs",countobs,"finalobsy",finalobsx,"finalobsx",finalobsy)
        print(bestscore,bestvx,bestvy,1,x,y)
        pygame.draw.line(screen,RED,(cuex,cuey),(pointx_groups[best_index1][best_index2],pointy_groups[best_index1][best_index2]),3)
        pygame.draw.line(screen,RED,(final_hitpointx,final_hitpointy),(pointx_groups[best_index1][best_index2],pointy_groups[best_index1][best_index2]),3)
        pygame.draw.line(screen,RED,(objx,objy),(best_virholex,best_virholey),3)
    print(f"最小的負數是: {bestscore}")
    print(f"最大負數的位置是: {best_index1,best_index2}")
    # bestvx=vxs[best_index]
    # bestvy=vys[best_index]
    # routeobs=main1obstacles[best_index]
    
    
def target_hole(hitx,hity,obstacle):
    obstacles = []
    for i in range(0,6):
        count = 0 
        for j in range(1, ballcount):
            count ,z,z= point_to_line_distance(ballx_set[j], bally_set[j], hitpointxs[i], hitpointys[i], virholex[i], virholey[i], 2*radius, i+1, j, count)
        obstacles.append(count)
    print("count",obstacles)
    return obstacles
        
def final(bestscore,bestvx,bestvy,obstacle,x,y):
    print("score",bestscore)
    print("vx,vy",bestvx,bestvy)
    print("obstacle on the route",obstacle)
    print("x,y",x,y)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 填充背景色
                screen.fill(WHITE)
                # table.line(畫布, 顏色, [x坐標, y坐標, 寬度, 高度, 線寬)
                talbe_inside=pygame.draw.rect(screen, DARK_GREEN, [x1, y1, width, height], 400)
                tablewall=pygame.draw.rect(screen,BLACK,(x1,y1,width,height),5)
                #hole(畫布, 顏色, (x坐標, y坐標), 半徑, 線寬)
                for i in range(0,6):
                    circle(holex[i],holey[i])
                    pygame.draw.circle(screen,BLACK,(virholex[i],virholey[i]),holeradius,3)
                #balls:all the ball  
                balls=[]
                #generate the ball 
                # ballcount = random.randint(2,8)
                ballcount=8
                #def generate the ball
                ballcount,ballnumber=generate(ballcount)
                print("ballcount",ballcount)
                #draw the ball
                ballx_set = [ball.x for ball in balls]#read the information from balls 
                bally_set = [ball.y for ball in balls]
                color=[ball.color for ball in balls]
                for ball in balls:
                    ball.drawball(screen)
                #nine=ball.nineball(screen)
                cue,cuex,cuey=oneball(WHITE)
                print("X coordinates:", ballx_set)
                print("Y coordinates:", bally_set)
                print("ballnumber:",ballnumber)
                print("cue",cuex,cuey)
                targetball=min(ballnumber)
                print("targetball",targetball,ballx_set[0],bally_set[0])
                hitpointxs=[]
                hitpointys=[]
                for i in range(0,6):
                    hitpointx,hitpointy=calculate_aim_point(ballx_set[0],bally_set[0],virholex[i],virholey[i],radius)
                    hitpointys.append(hitpointy)
                    hitpointxs.append(hitpointx)
                values1=[]
                for i in range(0,6):
                    value1=0
                    for j in range(1,ballcount):
                       value1,z,z=point_to_line_distance(ballx_set[j], bally_set[j], cuex,cuey,hitpointxs[i],hitpointys[i], 2*radius,"cue",j,value1)
                    values1.append(value1)
                route=0
                for i in range(0,6):
                    if values1[i]==0:
                        route=1
                print(route)
                if route==1:
                    main(cuex,cuey,ballx_set[0],bally_set[0])
                else:
                    main2(cuex,cuey,ballx_set[0],bally_set[0])
                pygame.draw.circle(screen,WHITE,(cuex,cuey),3*radius,2)
                pygame.draw.circle(screen,colors[targetball],(ballx_set[0],bally_set[0]),3*radius,2)
                text()
                pygame.display.update()