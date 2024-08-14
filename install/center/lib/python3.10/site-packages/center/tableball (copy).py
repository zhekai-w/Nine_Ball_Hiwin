
from matplotlib.patches import Polygon as MatplotlibPolygon
import random
import math
import pygame as pg,random,math,time
import sys
import pygame
tableheight =1920
tablewidth  =932
actualwidth =62.7
actualheight=30.4
# radius of balls (30.4cm: 1.6cm = 932pixels : 97.5pixels)
# R = 1.6/actualheight*tableheight
# r = round(R) #97
# #radius of holes (62.6cm : 1920pixels = 2cm : 60pixels)
# hole = tablewidth/actualwidth*2
# rb = round(hole)
radius=10
holeradius=15
#background
#代碼開始部分設定了一些基本的參數，如桌子的尺寸和球的半徑。此外，初始化 Pygame 並設定遊戲視窗的大小和標題。
pygame.init()
WIDTH, HEIGHT = 1000,500
WINDOW_SIZE = (WIDTH, HEIGHT)
screen = pygame.display .set_mode(WINDOW_SIZE)
pygame.display.set_caption("table tennis")
width=300 # 桌面的寬度
height=200 # 桌面的高度
value=0
#用不到
def color():
    #color noused
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
#孔洞的座標則根據桌面的四角和中點     
holex=[x1,x1+width/2,x1+width,x1,x1+width/2,x1+width]
holey=[y1,y1,y1,y1+height,y1+height,y1+height]
virholex=[x1+radius,x1+width/2,x1+width-radius,x1+radius,x1+width/2,x1+width-radius]
virholey=[y1+radius,y1+radius,y1+radius,y1+height-radius,y1+height-radius,y1+height-radius]
#distance to two ball

#計算兩個點之間的距離和向量
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
#類別用於創建和管理球的屬性，如顏色、位置、半徑和數字。
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

def cal_score(distance,angle,obstancle):
    print(distance,angle,obstancle)
    angles=[]
    distances=[]
    obstancles=[]
    score = (-obstancle * 5) + (-angle * 2) + (-distance * 1)
    return score
        # 
        
            #calculate angle distance
            #append in to list
            #calculate the score 
            #print score
        # for i in range(0,obstancle):
        #     score=(-angle[i]*1273 + 2000) + (- distance[i] + 2000) + (-obstancle[i]*1000 + 2000)
        #     sum+=score
        # print(sum,obstancle)
        # return sum
        
    # elif n == 1:
    #     n1ton2 = math.sqrt(abs(n1ton2[0])**2+abs(n1ton2[1])**2)
    #     n2tohole = math.sqrt(abs(toholevector[0])**2+abs(toholevector[1])**2)
    #     angle0 = math.acos((cueton1[0]*n1ton2[0]+cueton1[1]*n1ton2[1])/(cueton1*n1ton2))
    #     angle1 = math.acos((n1ton2[0]*toholevector[0]+n1ton2[1]*toholevector[1])/(n2tohole*n1ton2))      
    #     score = (-angle0*1273 + 2000)/2 + (-angle1*1273 + 2000)/2 + (- (cueton1+n1ton2+n2tohole) + 2000)  + (-n*1000 + 2000)

    # elif n == 2:
    #     cuefinalvector = [cueton1[0]-n1ton2[0],cueton1[1]-n1ton2[1]]
    #     cuetoiL = math.sqrt(abs(cueton1[0])**2+abs(cueton1[1])**2)
    #     itok2L = math.sqrt(abs(n1ton2[0])**2+abs(n1ton2[1])**2)
    #     k2tok1L = math.sqrt(abs(k2tok1vector[0])**2+abs(k2tok1vector[1])**2)
    #     k1toholeL = math.sqrt(abs(toholevector[0])**2+abs(toholevector[1])**2)
    #     angle0 = math.acos((cueton1[0]*n1ton2[0]+cueton1[1]*n1ton2[1])/(cuetoiL*itok2L))
    #     angle1 = math.acos((n1ton2[0]*k2tok1vector[0]+n1ton2[1]*k2tok1vector[1])/(k2tok1L*itok2L))
    #     angle2 = math.acos((k2tok1vector[0]*toholevector[0]+k2tok1vector[1]*toholevector[1])/(k1toholeL*k2tok1L))
    #     score = (-angle0*1273 + 2000)/3 + (-angle1*1273 + 2000)/3 + (-angle2*1273 + 2000)/3 + (- (cuetoiL+itok2L+k2tok1L+k1toholeL) + 2000) + (-n*1000 + 2000)
    
    # return score,cuefinalvector,cue,cueton1, n1, n1ton2, n2 ,toholevector,n
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
#在桌上隨機位置創建一個球。
def oneball(objcolor):
    x = random.randint(x1+radius,x1+width-radius)
    y = random.randint(y1+radius,y1+height-radius)
    pygame.draw.circle(screen,objcolor,(x,y),radius,width=radius)
    return objcolor,x,y
#檢查兩球是否重疊。
def checkball(x1,y1,x2,y2,radius,firstname,secondname):
    disx=x2-x1
    disy=y2-y1
    dis=math.sqrt(abs(disx)**2+abs(disy)**2)
    if dis<=radius:
        print("cover",firstname,secondname)
#在兩點間畫線。      
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
    # 计算方向向量 d
    dx = x2 - x1
    dy = y2 - y1
    # 计算向量 AP
    apx = px - x1
    apy = py - y1
    # 计算向量 d 的模长的平方
    d_mag_squared = dx**2 + dy**2
    # 防止除以零
    if d_mag_squared == 0:
        dist = math.sqrt(apx**2 + apy**2)
        closest_point = (x1, y1)
    else:
        # 计算投影长度 t
        t = (apx * dx + apy * dy) / d_mag_squared
        if t < 0:
            closest_point = (x1, y1)
            dist = math.sqrt((px - x1)**2 + (py - y1)**2)
        elif t > 1:
            closest_point = (x2, y2)
            dist = math.sqrt((px - x2)**2 + (py - y2)**2)
        else:
            # 计算投影点 Q
            qx = x1 + t * dx
            qy = y1 + t * dy
            closest_point = (qx, qy)
            dist = math.sqrt((px - qx)**2 + (py - qy)**2)
    #pygame.draw.line(screen,BLACK,closest_point,(px,py),3)
    # 判断是否碰撞
    if dist <= radius:
        value+=1
    #print(i,ballnumber[j])
    return value
def text():
    font = pygame.font.SysFont("Arial", 20)
    balltext=font.render("the ball exist:",True,BLACK)
    screen.blit(balltext,(450,50))
    for i in range(0,3):
        holenumbertop=font.render(str(holenumber[i]),True,BLACK)
        screen.blit(holenumbertop,(holex[i],holey[i]-50))
    for i in range(3,6):
        holenumberdown=font.render(str(holenumber[i]),True,BLACK)
        screen.blit(holenumberdown,(holex[i],holey[i]+50))
    for i in range(0,ballcount):
        txtexistball = font.render(str(ballnumber[i]), True, BLACK)
        screen.blit(txtexistball, (550+10*i, 50))
    for i in range(0,9):
        txtexistball = font.render((colorname[i]), True, BLACK)
        screen.blit(txtexistball, (700, 50+20*i))  
#def method1(cuex,cuey,obhname,objx,objy): 
# 計算打球的瞄准點
def calculate_aim_point(ball_x, ball_y, target_x, target_y, ball_diameter):
    # 计算向量
    vector_x = target_x - ball_x
    vector_y = target_y - ball_y
    # 计算向量长度
    length = math.sqrt(vector_x**2 + vector_y**2)
    # 标准化向量
    unit_vector_x = vector_x / length
    unit_vector_y = vector_y / length
    # 计算瞄准点
    aim_distance = 2 * ball_diameter
    aim_point_x = ball_x - unit_vector_x * aim_distance
    aim_point_y = ball_y - unit_vector_y * aim_distance
    return aim_point_x, aim_point_y

def main(cuex,cuey,objx,objy,):
    distoholes=[]
    vxs=[]
    vys=[]
    cuetoobjdis,objtocuex,objtocuey=disandvec(cuex,cuey,objx,objy)
    line(WHITE,cuex,cuey,objx,objy,3)
    for i in range(0,6):
        target_hole_lines=[]
        # target_hole_lines.append(line(colors[targetball],objx,objy,holex[i],holey[i],3))
        distohole,vx,vy=disandvec(objx,objy,holex[i],holey[i])
        distoholes.append(distohole)
        vxs.append(vx)
        vys.append(vy)  
    cue_obj_holeangle=[]
    print("obj ball",objx,objy)
    for i in range(0,6):
        cue_obj_hole1=vector_angle(cuex,cuey,objx,objy,holex[i],holey[i])
        cue_obj_holeangle.append(cue_obj_hole1)
    for i in range(0,6):
        if cue_obj_holeangle[i]>120:
            print(i+1,f"error")
        else:
            print("dis  ",i+1,distoholes[i])
            print("angle",i+1,cue_obj_holeangle[i])
            line(BLACK,objx,objy,holex[i],holey[i],3)
    main1obstacles=[]
    main1obstacles=target_hole(hitpointxs,hitpointys,main1obstacles)
    way1scores=[]
    for i in range(0,6):
        way1score=cal_score(cuetoobjdis+distoholes[i],cue_obj_holeangle[i],main1obstacles[i])
        way1scores.append(way1score)
    max_score = max(way1scores)
    best_index = way1scores.index(max_score)
    best_holex=holex[best_index]
    best_holey=holey[best_index]
    line(WHITE,objx,objy,best_holex,best_holey,3)
    print("score",way1scores)
    print("best",max_score)
    
    
def main2(cuex,cuey,objx,objy):
    cue_obj_diss=[]
    cue_objvxs=[]
    cue_objvys=[]
    obj_tar_diss=[]
    obj_tarvxs=[]
    obj_tarvys=[]
    cue_obj_dis,vx,vy=disandvec(cuex,cuey,objx,objy)
    middlex_num=vx/2
    middley_num=vy/2
    pointx=[cuex-middlex_num,cuex-middlex_num,x1+300,x1]
    pointy=[y1+200,y1,cuey-middley_num,cuey-middley_num]
    for i in range(0,4):
        cue_obj_dis1,cue_objvx,cue_objvy=disandvec(cuex,cuey,pointx[i],pointy[i])
        obj_tar_dis,obj_tarvx,obj_tarvy=disandvec(objx,objy,pointx[i],pointy[i])
    values3=[]
    values4=[]
    for j in range(0,4):
        value3=0
        value4=0
        for i in range(1,ballcount):
            value3=point_to_line_distance(ballx_set[i],bally_set[i],cuex,cuey,pointx[j],pointy[j],2*radius,i,j,value3)
            value4=point_to_line_distance(ballx_set[i],bally_set[i],objx,objy,pointx[j],pointy[j],2*radius,i,j,value4)
        values3.append(value3)  
        values4.append(value4)
        if value3==0 and value4==0:
            line(PINK,cuex,cuey,pointx[j],pointy[j],3)
            line(PINK,ballx_set[0],bally_set[0],pointx[j],pointy[j],3)
    main2obstacles=[]
    main2obstacles=target_hole(hitpointxs,hitpointys,main2obstacles)
    print(middlex_num,middley_num)
# def main3(cuex,cuey,objx,objy):
        
        # values7=[]
        # for i in range(0,6):
        #     value7=0
        #     for j in range(1,ballcount):
        #         value7=point_to_line_distance(ballx_set[j],bally_set[j],objx,objy,holex[i],holey[i],2*radius,i+1,j,value7)
        #     values7.append(value7)
        #     if value7==0:
        #         line(PINK,objx,objy,holex[i],holey[i],3) 
        # print("target_hole",values7)
        # return 0
def target_hole(hitx,hity,obstacle):
    obstacles = []
    for i in range(0,6):
        count = 0 
        for j in range(1, ballcount):
            count = point_to_line_distance(ballx_set[j], bally_set[j], hitpointxs[i], hitpointys[i], holex[i], holey[i], 2*radius, i+1, j, count)
        obstacles.append(count)
    print("count",obstacles)
    return obstacles
        
def final():
    print("route",)
    print("score")
    print("vx,vy")
    print("is the have obstacle on the route")
    print("is the have obstacle at hitpoint")
    print("x,y")
    
    
    
        
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
                rect1=pygame.draw.rect(screen, DARK_GREEN, [x1, y1, width, height], 400)
                leftwall=pygame.draw.line(screen,BLACK,(x1,y1),(x1,y1+200),5)
                rightwall=pygame.draw.line(screen,BLACK,(x1+300,y1),(x1+300,y1+200),5)
                topwall=pygame.draw.line(screen,BLACK,(x1,y1),(x1+300,y1),5)
                downwall=pygame.draw.line(screen,BLACK,(x1,y1+200),(x1+300,y1+200),5)
                #hole(畫布, 顏色, (x坐標, y坐標), 半徑, 線寬)
                for i in range(0,6):
                    circle(holex[i],holey[i])
                    #circle(virholex[i],virholey[i])
                #balls:all the ball  
                balls=[]
                #generate the ball 
                ballcount = random.randint(2,8)
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
                    hitpointx,hitpointy=calculate_aim_point(ballx_set[0],bally_set[0],holex[i],holey[i],radius)
                    hitpointys.append(hitpointy)
                    hitpointxs.append(hitpointx)
                distonine=[]
                distohole=[]
                distoelse=[]
                value1=0
                cue_boj_route=[]
                for i in range(0,6):
                    for j in range(1,ballcount):
                        value1=point_to_line_distance(ballx_set[j], bally_set[j], cuex,cuey,hitpointxs[i],hitpointys[i], 2*radius,"cue",j,value1)
                        if value1==0:
                            main(cuex,cuey,ballx_set[0],bally_set[0])
                            break
                        else:
                            main2(cuex,cuey,ballx_set[0],bally_set[0])
                            
                pygame.draw.circle(screen,WHITE,(cuex,cuey),3*radius,2)
                pygame.draw.circle(screen,colors[targetball],(ballx_set[0],bally_set[0]),3*radius,2)
                text()
                pygame.display.update()
