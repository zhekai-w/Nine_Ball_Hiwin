import cv2
import yaml
import numpy as np
from time import sleep
from math import pi, sin, cos, atan2, atan, asin, acos, sqrt

import time
import rclpy
from enum import Enum
from rclpy.node import Node
from rclpy.task import Future
from geometry_msgs.msg import Twist
from hiwin_interfaces.srv import RobotCommand

from cv2 import aruco
from threading import Thread
import pyrealsense2 as rs
from scipy.spatial.transform import Rotation as R
import configparser
import os

WIDTH = 1920
HEIGHT = 1080
TEST_VIEW = False
CAM_ROTATE_XAXIS = False
LOCK_TAG = 2
CONFIG_FILE = 'arm.yaml'

class State:
    BLIND_SEARCH = 0
    MEASURE_HEIGHT = 1
    LOCATE_CAMVIEW = 2
    LOCATE_2NDTAG = 3
    MOVE_HOME = 4
    CALIBRATED = 5
    TEST = 6

if TEST_VIEW:
    CAM_INIT_POS = [0.0, 377.0, 320.0]
    CAM_INIT_ORI = [0.0, 0.0, 0.0]
    INIT_STATE = State.TEST
else:
    CAM_INIT_POS = [0.0, 377.0, 320.0]
    CAM_INIT_ORI = [0.0, 0.0, -45.0]
    INIT_STATE = State.BLIND_SEARCH

TAG_DIST = 263      # distance between the camera and the target tag during measuring height in millimeter.
TAG_WIDTH = 50
EXPECT_TAG_AREA = 67000 # 260mm height
MIN_TAG_AREA = 17560
# limit operation ranges of robot arm in millimeter.
ARM_ZLIMIT_LOW = 0
ARM_ZLIMIT_HIGH = 1400
ARM_XLIMIT_LOW = -1200
ARM_XLIMIT_HIGH = 1200
ARM_YLIMIT_LOW = -500
ARM_YLIMIT_HIGH = 1200
MARGIN = 0.15       # the vertical and horizontal margin have to be reserved.
#TABLE_LENGTH = 680
#TABLE_WIDTH = 350

class Frame:
    NEXT = 0
    DONE = 1

class pid:
    def __init__(self, move_arm, capture_img, tf=None, frame_wait=False):
        self.move_arm = move_arm
        self.capture_img = capture_img
        self.frame_wait = frame_wait
        self.output_transform = tf

        # rz:-45, +45; rx: -30, -90
        self.pos = CAM_INIT_POS
        self.ori = CAM_INIT_ORI
        self.state = INIT_STATE
        self.scandir = 0        # 0: rotate z axis in counterclockwise; 1: rotate z axis in clockwise
        self.bestpos = (-1, -1, -1, -1, -1, -1)
        self.bestval = 1000000

        self.lock_tag = LOCK_TAG
        self.config = dict()

        self.aruco_dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_50)
        self.aruco_parameters = cv2.aruco.DetectorParameters()
        self.aruco_detector = cv2.aruco.ArucoDetector(self.aruco_dictionary, self.aruco_parameters)

    def calibrate(self):
        self.move_arm(self.pos, self.ori)

        if self.state == State.BLIND_SEARCH:
            print(f"===== BLIND SEARCH =====")
        elif self.state == State.MEASURE_HEIGHT:
            print(f"===== MEASURE HEIGHT {self.cnt} =====")
        elif self.state == State.LOCATE_CAMVIEW:
            print(f"===== LOCATE CAMVIEW {self.cnt} =====")
        elif self.state == State.LOCATE_2NDTAG:
            print(f"===== LOCATE 2ND TAG {self.cnt} =====")
        elif self.state == State.MOVE_HOME:
            print(f"===== MOVE HOME =====")

        print(f"camview ===> ", end='')
        for i in self.pos + self.ori:
            print(f"{i:.5f} ", end='')
        print()

        img = self.capture_img()
        (corners, ids, rejected) = self.aruco_detector.detectMarkers(img)
        print("corners = ", len(corners))

        #print(f"ids = {ids}, corners = {corners}")
        ids = [] if ids is None else ids.flatten()
        corners = [i.reshape((4, 2)) for i in corners]
        #print(f"===> ids = {ids}, corners = {corners}")
        idmap = {elmt:i for i, elmt in enumerate(ids)}

        #idxidmap = {j: i for i, j in idmap.items()}
        for i, elmt in enumerate(corners):
            (cx, cy) = self.center(elmt)
            print(f"{ids[i]}: ({cx:.2f}, {cy:.2f})")

        if self.state == State.BLIND_SEARCH:
            ret = self.blind_search(idmap, corners)
            if ret == Frame.DONE:
                self.blind_search_done()
                self.state = State.MEASURE_HEIGHT
                self.measure_height_init()
        elif self.state == State.MEASURE_HEIGHT:
            for (marker_corner, marker_id) in zip(corners, ids):
                (cx, cy) = self.center(marker_corner)
                cv2.circle(img, (cx, cy), 4, (0, 0, 255), -1)

            ret = self.measure_height(idmap, corners)
            if ret == Frame.DONE:
                self.measure_height_done()
                self.state = State.LOCATE_CAMVIEW
                self.locate_camview_init()
        elif self.state == State.LOCATE_CAMVIEW:
            ret = self.locate_camview(idmap, corners)
            if ret == Frame.DONE:
                self.locate_camview_done(idmap, corners)
                self.state = State.LOCATE_2NDTAG
                self.locate_2ndtag_init()
        elif self.state == State.LOCATE_2NDTAG:
            ret = self.locate_2ndtag(idmap, corners)
            if ret == Frame.DONE:
                self.locate_2ndtag_done()
                self.state = State.MOVE_HOME
        elif self.state == State.MOVE_HOME:
            self.move_home(idmap, corners)
            self.state = State.CALIBRATED
        elif self.state == State.CALIBRATED:
            return Frame.DONE
        elif self.state == State.TEST:
            sleep(1)
        else:
            print("Unknown state")
            return Frame.DONE

        cv2.imshow('Output', cv2.resize(img, (1280, 720)))
        cv2.waitKey(1)
        if self.frame_wait and (self.state == State.MEASURE_HEIGHT or self.state == State.LOCATE_CAMVIEW):
            sleep(0.1)
        return Frame.NEXT

    def blind_search(self, idmap, corners):
        if self.lock_tag in idmap:
            (cx, cy) = self.center(corners[idmap[self.lock_tag]])
            print(f"==> ({cx}, {cy})")
            e = abs(cx - WIDTH/2) + abs(cy - HEIGHT/2)
            if e < self.bestval:
                self.bestval = e
                self.bestpos = (*self.pos, *self.ori)
            if abs(cx - WIDTH/2) < WIDTH/4 and abs(cy - HEIGHT/2) < HEIGHT/4:
                return Frame.DONE

        # (x, y, z) fixed
        # rz:-45, +45; rx: 0, 60
        if self.scandir == 0:
            self.ori[2] += 15
            if self.ori[2] > 60:
                self.scandir = 1
                self.ori[0] += 10
                self.ori[2] = 60
                if self.ori[0] > 21:
                    return Frame.DONE
        else:
            self.ori[2] -= 15
            if self.ori[2] < -60:
                self.scandir = 0
                self.ori[0] += 10
                self.ori[2] = -60
                if self.ori[0] > 21:
                    return Frame.DONE

        return Frame.NEXT

    def blind_search_done(self):
        if self.bestval != 1000000:
            self.pos = list(self.bestpos[:3])
            self.ori = list(self.bestpos[3:])
        print(f"orientation = ({self.ori[0]}, {self.ori[1]})")
        print(f"bastval = {self.bestval}")

    def measure_height_init(self):
        self.Kp = 0.2         # parameters for centering the tag
        self.Ki = 0.1
        self.target = (WIDTH/2, HEIGHT/2)
        self.Kp2 = 0.06         # parameters for tag orientation
        self.Ki2 = 0.008
        self.Kp3 = 0.09         # parameters for adjusting camera's X axis
        self.Ki3 = 0.01
        self.Kp4 = 0.0005      # parameters for moving camera's Z axis
        self.Ki4 = 0.00001
        self.acclist = []
        self.acclist2 = []
        self.acclist3 = []
        self.acclist4 = []
        self.cnt = 0

    def measure_height(self, idmap, corners):
        # find the target tag and then approach it.
        if self.lock_tag not in idmap:
            return Frame.NEXT

        npos, nori = self.pos[:], self.ori[:]
        print(f"tag{self.lock_tag} = {corners[idmap[self.lock_tag]]}")
        tagcorner = corners[idmap[self.lock_tag]]
        cx, cy = self.center(tagcorner)
        ex = cx - self.target[0]
        ey = self.target[1] - cy
        ex, ey = self.rotate(ex, ey, nori[2])
        print(f'(x, y) = ({cx:.5f}, {cy:.5f}), (ex, ey) = ({ex:02}, {ey:02})')

        npos[0] += self.Kp * ex + self.Ki * self.integ2(self.acclist)[0]
        npos[0] = np.clip(npos[0], ARM_XLIMIT_LOW, ARM_XLIMIT_HIGH)
        npos[1] += self.Kp * ey + self.Ki * self.integ2(self.acclist)[1]
        npos[1] = np.clip(npos[1], ARM_YLIMIT_LOW, ARM_YLIMIT_HIGH)
        self.add(self.acclist, (ex, ey))
        print(f"==> {self.pos}")

        # rotate around Z axis (yaw)
        (tl, tr, br, bl) = tagcorner
        eo = atan((bl[1] - br[1])/(br[0] - bl[0])) * 180 / pi
        nori[2] += self.Kp2 * eo + self.Ki2 * self.integ(self.acclist2)
        self.add(self.acclist2, eo)

        # rotate around X axis
        # ep = -90 - self.ori[0]     # for lens view +Y
        ep = -self.ori[0]
        if abs(ex) < 200 and abs(ey) < 200:
            nori[0] += self.Kp3 * ep + self.Ki3 * self.integ(self.acclist3)
            self.add(self.acclist3, ep)

        # move along Z axis
        print("AREA : ", self.area(*tagcorner))
        ea = self.area(*tagcorner) - EXPECT_TAG_AREA
        if abs(ep) < 15:
            npos[2] += self.Kp4 * ea + self.Ki4 * self.integ(self.acclist4)
            npos[2] = np.clip(npos[2], ARM_ZLIMIT_LOW, ARM_ZLIMIT_HIGH)
            self.add(self.acclist4, ea)

        print(f"ex = {ex:.5f}, ey = {ey:.5f}")
        print(f"eo = {eo:.5f}, ep = {ep:.5f}, ea = {ea:.5f}")
        if abs(ex) < 2 and abs(ey) < 2 and abs(eo) < 1 and abs(ep) < 1 and abs(ea) < 100:
            return Frame.DONE

        self.cnt += 1
        self.pos, self.ori = npos[:], nori[:]
        return Frame.NEXT

    def measure_height_done(self):
        self.cnt = 0
        self.tag = [*self.pos, *self.ori]
        self.tag[2] -= TAG_DIST
        print(f"===> tag{self.lock_tag} = {self.tag}")

    def locate_camview_init(self):
        # goal
        # x axis(optional): 30
        # tag0: (w/32, h/16), ...
        # move back to make tag2/tag3 captured.
        # move higher to make tag1/tag2 captured
        self.target = [WIDTH/32, HEIGHT/16]
        if self.lock_tag == 1 or self.lock_tag == 2:
            self.target[0] = WIDTH - self.target[0]
        if self.lock_tag == 2 or self.lock_tag == 3:
            self.target[1] = HEIGHT - self.target[1]

        self.Kp = 0.01
        self.Ki = 0.002
        self.Kp2 = 0.06
        self.Ki2 = 0.02
        self.Kp3 = 0.00037
        self.Ki3 = 0.000004
        self.Kp4 = 0.05
        self.Ki4 = 0.03
        self.Kp5 = 0.05
        self.Ki5 = 0.02
        self.Kp6 = 0.03
        self.Ki6 = 0.01
        self.acclist = []
        self.acclist2 = []
        self.acclist3 = []
        self.acclist4 = []
        self.acclist5 = []
        self.acclist6 = []

    def locate_camview(self, idmap, corners):
        idset = set(idmap)

        if self.lock_tag not in idset:
            print(f"*************** TAG{self.lock_tag} UNTRACKED ****************")
            return Frame.NEXT

        npos, nori = self.pos[:], self.ori[:]
        if idset == {0, 1, 2, 3}:
            sx = sy = 0
            for  elmt in corners:
                (cx, cy) = self.center(elmt)
                sx += cx
                sy += cy
            ex = sx / 4 - WIDTH/2
            ey = HEIGHT/2 - sy / 4
            ex, ey = self.rotate(ex, ey, nori[2])
            npos[0] += self.Kp4 * ex + self.Ki4 * self.integ2(self.acclist4)[0]
            npos[0] = np.clip(npos[0], ARM_XLIMIT_LOW, ARM_XLIMIT_HIGH)
            npos[1] += self.Kp4 * ey + self.Ki4 * self.integ2(self.acclist4)[1]
            npos[1] = np.clip(npos[1], ARM_YLIMIT_LOW, ARM_YLIMIT_HIGH)
            self.add(self.acclist4, (ex, ey))

            # rotate around Z axis (yaw)
            bl = self.center(corners[idmap[3]])
            br = self.center(corners[idmap[2]])
            eo = atan((bl[1] - br[1])/(br[0] - bl[0])) * 180 / pi
            nori[2] += self.Kp5 * eo + self.Ki5 * self.integ(self.acclist5)
            self.add(self.acclist5, eo)

            # adjust height
            if abs(ex) < 20 and abs(ey) < 20:
                emx = WIDTH * MARGIN / 2 - bl[0]
                emy = bl[1] - (HEIGHT - MARGIN * HEIGHT / 2)
                em = emx if abs(emx) < abs(emy) else emy
                npos[2] += self.Kp6 * em + self.Ki6 * self.integ(self.acclist6)
                self.add(self.acclist6, em)
                print(f"em = {em:.5f}, emx = {emx:.5f}, emy = {emy:.5f}")

            print(f"(ex, ey) = ({ex:.5f}, {ey:.5f}), eo = {eo:.5f}")
            if abs(ex) < 9 and abs(ey) < 9 and abs(eo) < 0.5 and abs(em) < 9:
                return Frame.DONE

        else:
            cx, cy = self.center(corners[idmap[self.lock_tag]])
            ex = cx - self.target[0]
            ey = self.target[1] - cy
            ex, ey = self.rotate(ex, ey, nori[2])
            npos[0] += self.Kp * ex + self.Ki * self.integ2(self.acclist)[0]
            npos[0] = np.clip(npos[0], ARM_XLIMIT_LOW, ARM_XLIMIT_HIGH)
            npos[1] += self.Kp * ey + self.Ki * self.integ2(self.acclist)[1]
            npos[1] = np.clip(npos[1], ARM_YLIMIT_LOW, ARM_YLIMIT_HIGH)
            self.add(self.acclist, (ex, ey))

            if CAM_ROTATE_XAXIS:
                # rotate around X axis
                # ep = -60 - self.nori[0]    # for lens view +Y
                ep = 30 - self.nori[0]
                if abs(ey) < 100:
                    nori[0] += self.Kp2 * ep + self.Ki2 * self.integ(self.acclist2)
                    self.add(self.acclist2, ep)
                    print(f"-----> ep = {ep:.5f}")

            # move higher along Z axis
            ea = self.area(*corners[idmap[self.lock_tag]]) - MIN_TAG_AREA
            npos[2] += self.Kp3 * ea + self.Ki3 * self.integ(self.acclist3)
            npos[2] = np.clip(npos[2], ARM_ZLIMIT_LOW, ARM_ZLIMIT_HIGH)   # limit max. height
            self.add(self.acclist3, ea)

            print(f'(x, y) = ({cx:.5f}, {cy:.5f}), (ex, ey) = ({ex:.5f}, {ey:.5f}), area = {self.area(*corners[idmap[self.lock_tag]])}, ea = {ea:.2f}')

        self.cnt += 1
        self.pos, self.ori = npos[:], nori[:]

        return Frame.NEXT

    def locate_camview_done(self, idmap, corners):
        self.campos, self.camori = self.pos[:], self.ori[:]
        self.tagimgpos = self.center(corners[idmap[self.lock_tag]])

        self.config['img_pot0'] = np.array(corners[idmap[0]][0]).tolist()
        self.config['img_pot1'] = np.array(corners[idmap[1]][1]).tolist()
        self.config['img_pot2'] = np.array(corners[idmap[2]][2]).tolist()
        self.config['img_pot3'] = np.array(corners[idmap[3]][3]).tolist()

    def locate_2ndtag_init(self):
        self.tag2nd = (self.lock_tag + 2) % 4
        self.target = (WIDTH/2, HEIGHT/2)
        self.Kp = 0.04
        self.Ki = 0.002
        self.Kp2 = 0.0005
        self.Ki2 = 0.0000002

        self.acclist = []
        self.acclist2 = []
        self.cnt = 0

    def locate_2ndtag(self, idmap, corners):
        if self.tag2nd not in idmap:
            return Frame.NEXT

        npos, nori = self.pos[:], self.ori[:]
        print(f"tag{self.tag2nd} = {corners[idmap[self.tag2nd]]}")
        tagcorner = corners[idmap[self.tag2nd]]
        cx, cy = self.center(tagcorner)
        ex = cx - self.target[0]
        ey = self.target[1] - cy
        ex, ey = self.rotate(ex, ey, nori[2])
        print(f'(x, y) = ({cx:.5f}, {cy:.5f}), (ex, ey) = ({ex:02}, {ey:02})')

        npos[0] += self.Kp * ex + self.Ki * self.integ2(self.acclist)[0]
        npos[0] = np.clip(npos[0], ARM_XLIMIT_LOW, ARM_XLIMIT_HIGH)
        npos[1] += self.Kp * ey + self.Ki * self.integ2(self.acclist)[1]
        npos[1] = np.clip(npos[1], ARM_YLIMIT_LOW, ARM_YLIMIT_HIGH)
        self.add(self.acclist, (ex, ey))
        print(f"==> {self.pos}")

        # move along Z axis
        ea = self.area(*tagcorner) - EXPECT_TAG_AREA
        print("abs(ex): ", abs(ex), " abs(ey): ", abs(ey), " abs(ea): ", abs(ea))
        if abs(ex) < WIDTH/2 and abs(ey) < HEIGHT/2:
            print("AREA : ", self.area(*tagcorner))
            npos[2] += self.Kp2 * ea + self.Ki2 * self.integ(self.acclist2)
            npos[2] = np.clip(npos[2], ARM_ZLIMIT_LOW, ARM_ZLIMIT_HIGH)
            self.add(self.acclist2, ea)

        print(f"ex = {ex:.5f}, ey = {ey:.5f}, ea = {ea:.5f}")
        if abs(ex) < 3 and abs(ey) < 3 and abs(ea) < 2000:
            return Frame.DONE

        self.cnt += 1
        self.pos, self.ori = npos[:], nori[:]
        return Frame.NEXT

    def locate_2ndtag_done(self):
        self.pos2ndtag = self.pos[:]
        print(f"2ndtag_done: pos = {self.pos}, ori = {self.ori}")
        self.pos, self.ori = self.campos[:], self.camori[:]

    def move_home(self, idmap, corners):
        pass

    def calc_potpos(self, tagid, x, y):
        theta = self.camori[2] * pi / 180
        potoff = sqrt(2 * (TAG_WIDTH/2)**2)
        p = potoff * complex(cos(theta), sin(theta))

        if tagid == 0:
            r = p * (-1 + 1j)/sqrt(2)
            return x + r.real, y + r.imag
        elif tagid == 1:
            r = p * (1 + 1j)/sqrt(2)
            return  x + r.real, y + r.imag
        elif tagid == 2:
            r = p * (1 - 1j)/sqrt(2)
            return x + r.real, y + r.imag
        elif tagid == 3:
            r = p * (-1 - 1j)/sqrt(2)
            return x + r.real, y + r.imag

    def calibrated(self):
        print(f"======== Result of Calibration========")
        tx, ty, tz, ta, tb, tc = self.tag
        tx2, ty2, tz2 = self.pos2ndtag
        camx, camy, camz, camox, camoy, camoz = self.campos + self.camori
        print(f"tag{self.lock_tag} = ({tx:.5f}, {ty:.5f}, {tz:.5f}, {ta:.5f}, {tb:.5f}, {tc:.5f})")
        print(f"tag{self.tag2nd} = ({tx2:.5f}, {ty2:.5f}, {tz2:.5f})")
        theta = camoz * pi / 180
        zcos, zsin = cos(theta), sin(theta)
        tx, ty = self.calc_potpos(self.lock_tag, tx, ty)
        tx2, ty2 = self.calc_potpos(self.tag2nd, tx2, ty2)
        alpha = atan((ty2 - ty)/(tx2 - tx))
        diag = sqrt((tx-tx2)**2 + (ty-ty2)**2)
        table_width = abs(diag * sin(theta - alpha))
        table_length = abs(diag * cos(theta - alpha))
        print(f"(tx, ty) = {tx:.5f}, {ty:.5f}")
        print(f"(tx2, ty2) = {tx2:.5f}, {ty2:.5f}")
        print(f"table (w, h) = ({table_width:.5f}, {table_length:.5f})")
        if self.lock_tag == 0:
            x0, y0 = tx, ty
            x2, y2 = tx2, ty2
            x1, y1 = x0 + table_length * zcos, y0 + table_length * zsin
            x3, y3 = x0 + table_width * zsin, y0 - table_width * zcos
        elif self.lock_tag == 1:
            x1, y1 = tx, ty
            x3, y3 = tx2, ty2
            x0, y0 = x1 - table_length * zcos, y1 - table_length * zsin
            x2, y2 = x1 + table_width * zsin, y1 - table_width * zcos
        elif self.lock_tag == 2:
            x2, y2 = tx, ty
            x0, y0 = tx2, ty2
            x1, y1 = x2 - table_width * zsin, y2 + table_width * zcos
            x3, y3 = x2 - table_length * zcos, y2 - table_length * zsin
        elif self.lock_tag == 3:
            x3, y3 = tx, ty
            x1, y1 = tx2, ty2
            x0, y0 = x3 - table_width * zsin, y3 + table_width * zcos
            x2, y2 = x3 + table_length * zcos, y3 + table_length * zsin

        print(f"pot0 = ({x0:.5f}, {y0:.5f})\npot1 = ({x1:.5f}, {y1:.5f})\npot2 = ({x2:.5f}, {y2:.5f})\npot3 = ({x3:.5f}, {y3:.5f})")
        print(f"camview ===> {camx:.5f}, {camy:.5f}, {camz:.5f}, {camox:.5f}, {camoy:.5f}, {camoz:.5f}")

        cenx, ceny = (x0 + x2) / 2, (y0 + y2) / 2
        print(f"center = ({cenx:.5f}, {ceny:.5f})")

        tagpos = np.array(self.tag[:3])
        print(f"tagpos = {tagpos}")
        w = -theta
        T = np.array([[1, 0, 0, -camx], [0, 1, 0, -camy], [0, 0, 1, -camz], [0, 0, 0, 1]])
        R = np.array([[cos(w), -sin(w), 0, 0], [sin(w), cos(w), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        Mext = R.dot(T)
        print(f"Mext = {Mext}")
        xc, yc, zc, _  = Mext.dot(np.r_[tagpos, 1])
        print(f"xc = {xc:.5f}, yc = {yc:.5f}, zc = {zc:.5f}")
        u, v = self.tagimgpos
        cx, cy = WIDTH/2, HEIGHT/2
        fx = (u - cx) * zc / xc
        fy = (v - cy) * zc / yc
        Mint = np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]]) / zc
        print(f"Mint = {Mint}")

        self.config['zoff'] = np.array(abs(camz - tz)).tolist()
        self.config['pot0'] = np.array([x0, y0, tz]).tolist()
        self.config['pot1'] = np.array([x1, y1, tz]).tolist()
        self.config['pot2'] = np.array([x2, y2, tz]).tolist()
        self.config['pot3'] = np.array([x3, y3, tz]).tolist()
        self.config['campos'] = np.array([*self.campos, *self.camori]).tolist()

        if self.output_transform != None:
            armpos, armori = self.output_transform(self.campos, self.camori)
            self.config['armpos'] = np.array([*armpos, *armori]).tolist()

        self.config['Mint'] = Mint.tolist()
        self.config['Mext'] = Mext.tolist()
        with open(CONFIG_FILE, 'w') as file:
            yaml.dump(self.config, file, default_flow_style=False, sort_keys=False)

    def add(self, acclist, elmt):
        acclist.append(elmt)
        if len(self.acclist) > 10:   # keep at most 10 elements.
            acclist.pop(0)

    def integ(self, acclist):
        if len(acclist) == 0:
            return 0
        return sum(acclist) / len(acclist)

    def integ2(self, acclist):
        if len(acclist) == 0:
            return (0, 0)
        ax = sum([i for (i, j) in acclist]) / len(acclist)
        ay = sum([j for (i, j) in acclist]) / len(acclist)
        return (ax, ay)

    def area(self, tl, tr, br, bl):
        pos = tl[0]*tr[1] + tr[0]*br[1] + br[0]*bl[1] + bl[0]*tl[1]
        neg = tl[1]*tr[0] + tr[1]*br[0] + br[1]*bl[0] + bl[1]*tl[0]
        return abs(pos - neg) / 2

    def rotate(self, x, y, w):
        w = w * pi / 180
        A = np.array([[cos(w), -sin(w)], [sin(w), cos(w)]])
        X = np.array([x, y])
        return A.dot(X)

    def center(self, corner):
        (top_left, top_right, bottom_right, bottom_left) = corner
        cx = int((top_left[0] + bottom_right[0])/2)
        cy = int((top_left[1] + bottom_right[1])/2)
        return (cx, cy)


# the relative pose between the end effector and the camera.
# the relative position between the end effector and the lens is measured when the orientation of the end effector is set to (0, 0, 0).
# the view direction of the camera lens is defined as -Z.
END2CAM = [77.5046, -36.715, 68.49, 180.0, 0.0, 90.0]

DEFAULT_VELOCITY = 50
DEFAULT_ACCELERATION = 10

class States(Enum):
    INIT = 0
    FINISH = 1
    MOVE_TO_PHOTO_POSE = 2
    YOLO_DETECT = 3
    MOVE_TO_OPJECT_TOP = 4
    PICK_OBJECT = 5
    MOVE_TO_PLACE_POSE = 6
    CHECK_POSE = 7
    CLOSE_ROBOT = 8

class ArmCali(Node):
    def __init__(self):
        super().__init__('ArmCalibration')
        self.hiwin_client = self.create_client(RobotCommand, 'hiwinmodbus_service')

        # Read camera_calibration.ini
        current_dir = os.getcwd()
        print("Current dir", current_dir)
        filepath = current_dir + '/camera_calibration.ini'
        self.camera_matrix, self.dist_coeffs = self.read_camera_config(filepath)
        print("Camera matrix: ", self.camera_matrix)

        self.pipeline = rs.pipeline()
        config = rs.config()
        config.enable_stream(rs.stream.color, 1920, 1080, rs.format.bgr8, 30)
        # Start streaming
        self.pipeline.start(config)

        self.pid = pid(self.move_arm, self.capture_img, tf=self.cam2arm)


    def start(self):
        thread = Thread(target=self.calibrate)
        thread.daemon = True
        thread.start()

    def calibrate(self):
        while True:
            ret = self.pid.calibrate()
            if ret == Frame.DONE:
                self.pid.calibrated()
                break
        self.pipeline.stop()
        self.destroy_node()

    def move_arm(self, pos, ori):
        pos, ori = self.cam2arm(pos, ori)
        pose = Twist()
        [pose.linear.x, pose.linear.y, pose.linear.z] = pos
        [pose.angular.x, pose.angular.y, pose.angular.z] = ori

        req = self.generate_robot_request(
                holding=True,
                cmd_mode=RobotCommand.Request.PTP,
                pose=pose)
        res = self.call_hiwin(req)

    def capture_img(self):
        frame = self.pipeline.wait_for_frames()
        color_frame = frame.get_color_frame()
        frame = np.asanyarray(color_frame.get_data())
        undistort = self.undistort_image(frame, self.camera_matrix, self.dist_coeffs)
        return undistort

    def cam2arm(self, pos, ori):
        end2cam_rot = R.from_euler('xyz', END2CAM[3:], degrees=True)
        cam_rot = R.from_euler('xyz', ori, degrees=True)
        A = cam_rot * end2cam_rot
        relpos = A.apply(END2CAM[:3])
        armpos = pos - relpos
        armori = A.as_euler('xyz', degrees=True)
        return armpos, armori
    
    def read_camera_config(self, filepath):
        camera_matrix = None
        dist_coeffs = None
        config = configparser.ConfigParser()
        config.read(filepath)
        try:
            # Read camera matrix
            cm = config['Intrinsic']
            camera_matrix = np.array([
                [float(cm['0_0']), float(cm['0_1']), float(cm['0_2'])],
                [float(cm['1_0']), float(cm['1_1']), float(cm['1_2'])],
                [0, 0, 1]
            ])

            # Read distortion coefficient
            dc = config['Distortion']
            dist_coeffs = np.array(
                [float(dc['k1']), float(dc['k2']), float(dc['t1']), float(dc['t2']), float(dc['k3'])]
            )
        except configparser.Error as e:
            print(e)
        return camera_matrix, dist_coeffs

    def undistort_image(self, image, camera_matrix, dist_coeffs):
        """
        Undistort an image using camera calibration parameters
        param image: Input image
        param camera_matrix: Camera matrix
        param dist_coeffs: Distortion ceofficients
        return: Undistorted image
        """
        h, w = image.shape[:2]

        new_camera_matrix,  roi = cv2.getOptimalNewCameraMatrix(camera_matrix, dist_coeffs, (w, h), 1, (w, h))
        undistorted = cv2.undistort(image, camera_matrix, dist_coeffs, None, new_camera_matrix)
        return undistorted

    def generate_robot_request(
            self,
            holding=True,
            cmd_mode=RobotCommand.Request.PTP,
            cmd_type=RobotCommand.Request.POSE_CMD,
            velocity=DEFAULT_VELOCITY,
            acceleration=DEFAULT_ACCELERATION,
            tool=1,
            base=0,
            digital_input_pin=0,
            digital_output_pin=0,
            digital_output_cmd=RobotCommand.Request.DIGITAL_OFF,
            pose=Twist(),
            joints=[float('inf')]*6,
            circ_s=[],
            circ_end=[],
            jog_joint=6,
            jog_dir=0
            ):
        request = RobotCommand.Request()
        request.digital_input_pin = digital_input_pin
        request.digital_output_pin = digital_output_pin
        request.digital_output_cmd = digital_output_cmd
        request.acceleration = acceleration
        request.jog_joint = jog_joint
        request.velocity = velocity
        request.tool = tool
        request.base = base
        request.cmd_mode = cmd_mode
        request.cmd_type = cmd_type
        request.circ_end = circ_end
        request.jog_dir = jog_dir
        request.holding = holding
        request.joints = joints
        request.circ_s = circ_s
        request.pose = pose
        return request

    def _wait_for_future_done(self, future: Future, timeout=-1):
        time_start = time.time()
        while not future.done():
            time.sleep(0.01)
            if timeout > 0 and time.time() - time_start > timeout:
                return False
        return True

    def call_hiwin(self, req):
        while not self.hiwin_client.wait_for_service(timeout_sec=2.0):
            print('in function while loop')
        future = self.hiwin_client.call_async(req)
        if self._wait_for_future_done(future):
            res = future.result()
        else:
            res = None
        return res

def main(args=None):
    rclpy.init(args=args)

    stratery = ArmCali()
    stratery.start()

    rclpy.spin(stratery)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
