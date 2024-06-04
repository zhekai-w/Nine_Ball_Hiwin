import random
import math
import pygame as pg
import pygame
import sys
import time
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
pygame.init()
WIDTH, HEIGHT = 1000,500
WINDOW_SIZE = (WIDTH, HEIGHT)

WHITE=(255,255,255)
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
colorname=["yellow","blue","red","purple","orange","green","brown","black","pink"]

# Distance and vector functions
def distance_and_vector(n1x, n1y, n2x, n2y):
    dx = n1x - n2x
    dy = n1y - n2y
    dist = math.sqrt(dx ** 2 + dy ** 2)
    return round(dist, 2), dx, dy

#
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


# Ball class
class Ball:
    def __init__(self, color, x, y, radius):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# Generate random balls
def generate_balls(ball_count, radius):
    cuex = random.randint(x1 + radius, x1 + width - radius)
    cuey = random.randint(y1 + radius, y1 + height - radius)
    ballx_set = []
    bally_set = []
    for _ in range(ball_count):
        x = random.randint(x1 + radius, x1 + width - radius)
        y = random.randint(y1 + radius, y1 + height - radius)
        ballx_set.append(x)
        bally_set.append(y)
    return cuex, cuey, ballx_set, bally_set, ball_count

# Calculate aim point()
def calculate_aim_point(ball_x, ball_y, target_x, target_y, ball_diameter):
    vector_x = target_x - ball_x
    vector_y = target_y - ball_y
    length = math.sqrt(vector_x ** 2 + vector_y ** 2)
    unit_vector_x = vector_x / length
    unit_vector_y = vector_y / length
    aim_distance = 2 * ball_diameter
    aim_point_x = ball_x - unit_vector_x * aim_distance
    aim_point_y = ball_y - unit_vector_y * aim_distance
    return aim_point_x, aim_point_y

# Calculate distance from point to line segment
def point_to_line_distance(px, py, x1, y1, x2, y2, radius, i, j, value):
    dx = x2 - x1
    dy = y2 - y1
    apx = px - x1
    apy = py - y1
    d_mag_squared = dx ** 2 + dy ** 2
    if d_mag_squared == 0:
        dist = math.sqrt(apx ** 2 + apy ** 2)
        closest_point = (x1, y1)
    else:
        t = (apx * dx + apy * dy) / d_mag_squared
        if t < 0:
            closest_point = (x1, y1)
            dist = math.sqrt((px - x1) ** 2 + (py - y1) ** 2)
        elif t > 1:
            closest_point = (x2, y2)
            dist = math.sqrt((px - x2) ** 2 + (py - y2) ** 2)
        else:
            qx = x1 + t * dx
            qy = y1 + t * dy
            dist = math.sqrt((px - qx) ** 2 + (py - qy) ** 2)
    if dist <= radius:
        value += 1
        return value, px, py
    return value, 0, 0

# Function to find the minimum negative integer in a nested list
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

def perpendicular_points(p_x, p_y, q_x, q_y, distance):
    # 计算向量 pq
    vector_pq_x = q_x - p_x
    vector_pq_y = q_y - p_y
    
    # 计算向量 pq 的垂直向量
    perpendicular_vector_x = -vector_pq_y
    perpendicular_vector_y = vector_pq_x
    
    # 计算垂直向量的模长
    magnitude = math.sqrt(perpendicular_vector_x**2 + perpendicular_vector_y**2)
    
    # 计算单位垂直向量
    unit_vector_x = perpendicular_vector_x / magnitude
    unit_vector_y = perpendicular_vector_y / magnitude
    
    # 计算左侧点位
    left_point_x = p_x + distance * unit_vector_x
    left_point_y = p_y + distance * unit_vector_y
    
    # 计算右侧点位
    right_point_x = p_x - distance * unit_vector_x
    right_point_y = p_y - distance * unit_vector_y
    
    return left_point_x, left_point_y, right_point_x, right_point_y

# Main game logic functions (main1 and main2)
def main1(screen,cuex, cuey, objx, objy, hitpointxs, hitpointys, values1, ballcount, ballx_set, bally_set):
    routenumber=1
    objtoholes = []
    vxs = []
    vys = []
    for i in range(6):
        cuetoobjdis, objtocuex, objtocuey = distance_and_vector(cuex, cuey, hitpointxs[i],hitpointys[i])
        objtohole, _,_= distance_and_vector(objx, objy, vir_hole_positions[i][0], vir_hole_positions[i][1])
        objtoholes.append(objtohole)
        vxs.append(objtocuex) 
        vys.append(objtocuey)

    cue_obj_holeangle = []
    for i in range(6):
        cue_obj_hole1 = vector_angle(cuex, cuey, objx, objy, vir_hole_positions[i][0], vir_hole_positions[i][1])
        if cue_obj_hole1 > 100:
            cue_obj_holeangle.append(-cue_obj_hole1)
        else:
            cue_obj_holeangle.append(cue_obj_hole1)

    main1obstacles = target_hole(hitpointxs, hitpointys, ballcount, ballx_set, bally_set,6)
    way1scores = []
    for i in range(6):
        way1score = cal_score(cuetoobjdis + objtoholes[i], cue_obj_holeangle[i], values1[i], main1obstacles[i])
        way1scores.append(way1score)

    non_positive_scores = [score for score in way1scores if score <= 0]
    if non_positive_scores:
        max_non_positive_score = max(non_positive_scores)
        best_index = way1scores.index(max_non_positive_score)
        best_virholex = vir_hole_positions[best_index][0]
        best_virholey = vir_hole_positions[best_index][1]
        final_hitpointx = hitpointxs[best_index]
        final_hitpointy = hitpointys[best_index]
        bestvx = vxs[best_index]
        bestvy = vys[best_index]
        routeobs = main1obstacles[best_index]
        hitcuepointx, hitcuepointy = calculate_aim_point(cuex, cuey, final_hitpointx, final_hitpointy, radius)
        finalobsx = []
        finalobsy = []
        countobs = 0
        for i in range(1, ballcount):
            countobs, px, py = point_to_line_distance(ballx_set[i], bally_set[i], objx, objy, best_virholex, best_virholey, 2 * radius, i, 1, countobs)
            if px > 0:
                finalobsx.append(px)
                finalobsy.append(py)
        cue_obstacle=edge_detect(hitcuepointx,hitcuepointy)
        final(routenumber,max_non_positive_score, bestvx, bestvy, routeobs, hitcuepointx, hitcuepointy,cue_obstacle)
        #      ballcount,routenumber,hitcuepointx,hitcuepointy,objx,objy,best_virholex,best_virholey,target_hitx,target_hity,reflectionx,reflectiony
        screen(ballcount,routenumber,hitcuepointx,hitcuepointy,objx,objy,best_virholex,best_virholey,final_hitpointx,final_hitpointy,_,_)
        return [max_non_positive_score, bestvx, bestvy, routeobs, hitcuepointx, hitcuepointy]
    else:
        return main2(screen,cuex, cuey, objx, objy, hitpointxs, hitpointys, ballx_set, bally_set, ballcount)

def main2(screen,cuex, cuey, objx, objy, hitpointxs, hitpointys, ballx_set, bally_set, ballcount):
    routenumber=2
    cue_obj_diss = []
    cue_objvxs = []
    cue_objvys = []
    obj_tar_diss = []
    obj_tarvxs = []
    obj_tarvys = []
    middlex_nums = []
    middley_nums = []

    for i in range(6):
        cue_obj_dis, cue_obj_vx, cue_obj_vy = distance_and_vector(cuex, cuey, hitpointxs[i], hitpointys[i])
        cue_obj_diss.append(cue_obj_dis)
        cue_objvxs.append(cue_obj_vx)
        cue_objvys.append(cue_obj_vy)
        obj_tar_dis, obj_tar_vx, obj_tar_vy = distance_and_vector(hitpointxs[i], hitpointys[i], objx, objy)
        obj_tar_diss.append(obj_tar_dis)
        obj_tarvxs.append(obj_tar_vx)
        obj_tarvys.append(obj_tar_vy)
        middlex_num = cue_obj_vx / 2
        middley_num = cue_obj_vy / 2
        middlex_nums.append(middlex_num)
        middley_nums.append(middley_num)

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

    main2obstacles1 = []
    for i in range(4):
        values2 = []
        for j in range(6):
            value2 = 0
            for k in range(1, ballcount):
                value2, _, _ = point_to_line_distance(ballx_set[k], bally_set[k], cuex, cuey, pointx_groups[i][j], pointy_groups[i][j], 2 * radius + 2, i + 1, j, value2)
                value2, _, _ = point_to_line_distance(ballx_set[k], bally_set[k], hitpointxs[i], hitpointys[i], pointx_groups[i][j], pointy_groups[i][j], 2 * radius + 2, i + 1, j, value2)
            values2.append(value2)
        main2obstacles1.append(values2)

    all_angle2 = []
    for i in range(4):
        cue_obj_holeangle2 = []
        for j in range(6):
            cue_obj_hole1 = vector_angle(pointx_groups[i][j], pointy_groups[i][j], objx, objy, vir_hole_positions[j][0], vir_hole_positions[j][1])
            if cue_obj_hole1 > 90:
                cue_obj_holeangle2.append(-cue_obj_hole1)
            else:
                cue_obj_holeangle2.append(cue_obj_hole1)
        all_angle2.append(cue_obj_holeangle2)

    main2obstacles2 = target_hole(hitpointxs, hitpointys, ballcount, ballx_set, bally_set,6)
    way2scores2 = []
    for i in range(4):
        way2scores1 = []
        for j in range(6):
            score = cal_score(cue_obj_diss[j] + obj_tar_diss[j], all_angle2[i][j], main2obstacles1[i][j], main2obstacles2[j])
            way2scores1.append(score)
            if score<0:
                print(score)
        way2scores2.append(way2scores1)

    bestscore, best_index1, best_index2 = find_min_negative_integer_in_nested_list(way2scores2)
    vxs2 = []
    vys2 = []
    for i in range(4):
        vxs1 = []
        vys1 = []
        for j in range(6):
            cue_point_dis, vx, vy = distance_and_vector(cuex, cuey, pointx_groups[i][j], pointy_groups[i][j])
            vxs1.append(vx)
            vys1.append(vy)
        vxs2.append(vxs1)
        vys2.append(vys1)

    if bestscore:
        best_virholex = vir_hole_positions[best_index2][0]
        best_virholey = vir_hole_positions[best_index2][1]
        final_hitpointx = hitpointxs[best_index2]
        final_hitpointy = hitpointys[best_index2]
        bestvx = vxs2[best_index1][best_index2]
        bestvy = vys2[best_index1][best_index2]
        reflectionx=pointx_groups[best_index1][best_index2]
        reflectiony=pointy_groups[best_index1][best_index2]
        finalobsx = []
        finalobsy = []
        countobs = 0
        for i in range(1, ballcount):
            countobs, px, py = point_to_line_distance(ballx_set[i], bally_set[i], objx, objy, best_virholex, best_virholey, 2 * radius, i, best_index2 + 1, countobs)
            if px > 0:
                finalobsx.append(px)
                finalobsy.append(py)
        hitcuepointx,hitcuepointy=calculate_aim_point(cuex,cuey,reflectionx,reflectiony,radius)
        cue_obstacle=edge_detect(hitcuepointx,hitcuepointy)
        final(routenumber,bestscore,bestvx,bestvy,countobs,hitcuepointx,hitcuepointy,cue_obstacle)
        # screen(ballcount,routenumber,hitcuepointx,hitcuepointy,objx,objy,best_virholex,best_virholey,target_hitx,target_hity,reflectionx,reflectiony
        screen(ballcount,routenumber,hitcuepointx,hitcuepointy,objx,objy,best_virholex,best_virholey,final_hitpointx,final_hitpointy,reflectionx,reflectiony)
        return [bestscore, bestvx, bestvy, countobs, hitcuepointx,hitcuepointy]
    return main3(screen,cuex, cuey, objx, objy,ballx_set, bally_set, ballcount)

#僅需計路徑上的障礙物來進行路徑選擇
def main3(screen,cuex, cuey, objx, objy, ballx_set, bally_set, ballcount):
    routenumber=3
    left_pointx,left_pointy,right_pointx,right_pointy=perpendicular_points(objx,objy,cuex,cuey,2*radius)
    second_cue_pointx=[]
    second_cue_pointy=[]
    second_cue_pointx.append(left_pointx)
    second_cue_pointy.append(left_pointy)
    second_cue_pointx.append(right_pointx)
    second_cue_pointy.append(right_pointy)
    objtoholes = []
    cue_obj_diss=[]
    cue_obj_vxs=[]
    cue_obj_vys=[]
    for i in range(2):
        cue_objdis,cue_vx,cue_vy=distance_and_vector(cuex,cuey,second_cue_pointx[i],second_cue_pointy[i])
        cue_obj_diss.append(cue_objdis)
        cue_obj_vxs.append(cue_vx)
        cue_obj_vys.append(cue_vy)
    values4=[]
    for j in range(2):
        value4=0
        for i in range(1,ballcount):
            value4,_,_=point_to_line_distance(ballx_set[i],bally_set[i],cuex,cuey,second_cue_pointx[j],second_cue_pointy[j],2*radius,i,j,value4)
        values4.append(value4)
    way3scores = []
    for i in range(2):
        for j in range(6):
            way3score = cal_score(cue_obj_diss[i], 1, values4[i],0)
            way3scores.append(way3score)
    print(way3scores)
    non_positive_scores = [score for score in way3scores if score <= 0]
    if non_positive_scores:
        max_non_positive_score = max(non_positive_scores)
        best_index = way3scores.index(max_non_positive_score)
        final_hitpointx = second_cue_pointx[best_index]
        final_hitpointy = second_cue_pointy[best_index]
        bestvx = cue_obj_vxs[best_index]
        bestvy = cue_obj_vys[best_index]
        routeobs=values4[best_index]
        hitcuepointx, hitcuepointy = calculate_aim_point(cuex, cuey, final_hitpointx, final_hitpointy, radius)
        cue_obstacle=edge_detect(hitcuepointx,hitcuepointy)
        final(routenumber,max_non_positive_score, bestvx, bestvy,routeobs, hitcuepointx, hitcuepointy,cue_obstacle)
        print(values4)
        #ballcount,routenumber,hitcuepointx,hitcuepointy,objx,objy,best_virholex,best_virholey,target_hitx,targethity,reflectionx,reflectiony
        screen(ballcount,routenumber,hitcuepointx,hitcuepointy,objx,objy,objx,objy,final_hitpointx,final_hitpointy,objx,objy)
        return [max_non_positive_score, bestvx, bestvy, cue_obstacle, hitcuepointx, hitcuepointy]
    else:
        routenumber=4
        routeobs=values4[1]
        final_hitpointx=second_cue_pointx[1]
        final_hitpointy=second_cue_pointy[1]
        hitcuepointx, hitcuepointy = calculate_aim_point(cuex, cuey, final_hitpointx, final_hitpointy, radius)
        cue_obstacle=edge_detect(hitcuepointx,hitcuepointy)
        final(routenumber,way3scores[1],cue_obj_vxs[1],cue_obj_vys[1],"x", hitcuepointx, hitcuepointy,cue_obstacle)
        #ballcount,routenumber,hitcuepointx,hitcuepointy,objx,objy,best_virholex,best_virholey,target_hitx,targethity,reflectionx,reflectiony
        print(values4)
        screen(ballcount,routenumber,hitcuepointx,hitcuepointy,objx,objy,objx,objy,second_cue_pointx[1],second_cue_pointy[1],objx,objy)
        return [way3scores[1],cue_obj_vxs[1],cue_obj_vys,values4[1],cue_obstacle,hitcuepointx,hitcuepointy]

    
    
def vector_angle(n1x, n1y, n2x, n2y, n3x, n3y):
    vx1, vy1 = n2x - n1x, n2y - n1y
    vx2, vy2 = n3x - n2x, n3y - n2y
    dotproduct = vx1 * vx2 + vy1 * vy2
    magnitude1 = math.sqrt(vx1 ** 2 + vy1 ** 2)
    magnitude2 = math.sqrt(vx2 ** 2 + vy2 ** 2)
    cos = dotproduct / (magnitude1 * magnitude2)
    cos = max(-1, min(1, cos))
    rad = math.acos(cos)
    deg = math.degrees(rad)
    return deg

def cal_score(distance, angle, cue_objobs, obj_holeobs):
    score = ((angle * -22) + (distance * -1) + (obj_holeobs * -4000))
    if angle < 0:
        score = abs(score)
    elif cue_objobs > 0:
        score = abs(score)
    return score

def text(screen):
    font = pygame.font.SysFont("Arial", 20)
    balltext=font.render("the ball exist:",True,BLACK)
    screen.blit(balltext,(450,50))
    for i in range(0,3):
        holenumbertop=font.render(str(i),True,BLACK)
        screen.blit(holenumbertop,(virholex[i],virholey[i]-50))
    for i in range(3,6):
        holenumberdown=font.render(str(i),True,BLACK)
        screen.blit(holenumberdown,(virholex[i],virholey[i]+50))
    # for i in range(0,ballcount):
    #     txtexistball = font.render(str(ballnumber[i]), True, BLACK)
    #     screen.blit(txtexistball, (550+10*i, 50))
    for i in range(0,9):
        txtexistball = font.render((colorname[i]), True, BLACK)
        screen.blit(txtexistball, (900, 50+20*i))  

def edge_detect(hitcuepointx,hitcuepointy):
    cue_obstacle=0
    if hitcuepointx - radius < x1 or hitcuepointx + radius > x1 + width or hitcuepointy - radius < y1 or hitcuepointy + radius > y1 + height:
        return True
    for i in range(1,ballcount):
        cue_obstacle,_,_=point_to_line_distance(ballx_set[i],bally_set[i],hitcuepointx,hitcuepointy,cuex,cuey,2*radius,i,1,cue_obstacle)
        return True
    return False

def target_hole(hitpointxs, hitpointys, ballcount, ballx_set, bally_set,hitpoint_count):
    obstacles = []
    for i in range(hitpoint_count):
        count = 0
        for j in range(1, ballcount):
            count, _, _ = point_to_line_distance(ballx_set[j], bally_set[j], hitpointxs[i], hitpointys[i], vir_hole_positions[i][0], vir_hole_positions[i][1], 2 * radius, i + 1, j, count)
        obstacles.append(count)
    return obstacles

#the final data need to publish
def final(routenumber,bestscore,bestvx,bestvy,obstacle,bestx,besty,cue_obstacle):
    print("---------------------------------------------")
    print("routenumber",routenumber)
    print("Score:", bestscore)
    print("vx, vy:", bestvx, bestvy)
    print("Obstacles on the route:", obstacle)
    print("x, y:", bestx, besty)
    print("there have obstacle around cue",cue_obstacle)
    # return ballx_set,bally_set,ballcount,cu
    # ex,cuey,bestscore, bestvx, bestvy, countobs, final_hitpointx, final_hitpointy,x,y

def screen(ballcount,routenumber,hitcuepointx,hitcuepointy,objx,objy,best_virholex,best_virholey,target_hitx,target_hity,reflectionx,reflectiony):
    screen = pygame.display.set_mode(WINDOW_SIZE)
    colors=[YELLOW,BLUE,RED,PURPLE,ORANGE,GREEN,BROWN,BLACK,PINK]
    pygame.display.set_caption("table tennis")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            screen.fill(WHITE)
            #hole(畫布, 顏色, (x坐標, y坐標), 半徑, 線寬)
            table_inside=pygame.draw.rect(screen,DARK_GREEN, [x1, y1, width, height], 400)
            tablewall=pygame.draw.rect(screen,BLACK,(x1,y1,width,height),5)
            pygame.draw.rect(screen, BLACK, (x1, y1, width, height), 5)
            for i in range(0,6):
                pygame.draw.circle(screen,BLACK,(holex[i],holey[i]),holeradius,holeradius)
                pygame.draw.circle(screen,BLACK,(virholex[i],virholey[i]),holeradius,3)
            pygame.draw.circle(screen,WHITE,(cuex,cuey),radius,radius)
            for i in range (ballcount):
                pygame.draw.circle(screen,colors[i],(ballx_set[i],bally_set[i]),radius,radius)
            pygame.draw.circle(screen,RED,(hitcuepointx,hitcuepointy),3,3)
            if routenumber==1 :
                pygame.draw.line(screen,WHITE,(cuex,cuey),(target_hitx,target_hity),3)
                pygame.draw.line(screen,WHITE,(objx,objy),(best_virholex,best_virholey),3)
            elif routenumber==2 :
                pygame.draw.line(screen,RED,(cuex,cuey),(reflectionx,reflectiony),3)
                pygame.draw.line(screen,RED,(reflectionx,reflectiony),(target_hitx,target_hity),3)
                pygame.draw.line(screen,RED,(objx,objy),(best_virholex,best_virholey),3)
            elif routenumber==3 or routenumber==4:
                pygame.draw.line(screen,BLUE,(cuex,cuey),(target_hitx,target_hity),3)
            pygame.display.update()
        
def main(ballx_set,bally_set,ballcount,cuex,cuey):
    while True:                    
        hitpointxs = []
        hitpointys = []
        for i in range(6):
            hitpointx, hitpointy = calculate_aim_point(ballx_set[0], bally_set[0], vir_hole_positions[i][0], vir_hole_positions[i][1], radius)
            hitpointys.append(hitpointy)
            hitpointxs.append(hitpointx)
        #cue_target ball obstacle count
        values1 = []
        for i in range(6):
            value1 = 0
            for j in range(1, ballcount):
                value1, _, _ = point_to_line_distance(ballx_set[j], bally_set[j], cuex, cuey, hitpointxs[i], hitpointys[i], 2 * radius, "cue", j, value1)
            values1.append(value1)
        route = any(v == 0 for v in values1)
        if route:
            return main1(screen,cuex, cuey, ballx_set[0], bally_set[0], hitpointxs, hitpointys, values1, ballcount, ballx_set, bally_set)
        else:
            return main2(screen,cuex, cuey, ballx_set[0], bally_set[0], hitpointxs, hitpointys, ballx_set, bally_set, ballcount,)
while True:
    balls=[]
    ballcount=8
    #def generate the ball
    cuex, cuey, ballx_set, bally_set, ball_count=generate_balls(ballcount,radius)
    print(ballx_set)
    print(bally_set)
    print("ballcount",ballcount)
    main(ballx_set,bally_set,ballcount,cuex,cuey)