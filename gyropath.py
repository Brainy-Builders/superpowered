#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (
    Motor,
    TouchSensor,
    ColorSensor,
    InfraredSensor,
    UltrasonicSensor,
    GyroSensor,
)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font
import time
import math
import os
from common import *
import os
f="""0 ,  0
13 ,  0
13 ,  0
13 ,  0
13 ,  0
13 ,  0
13 ,  0
24 ,  -2
38 ,  -2
51 ,  -3
63 ,  -5
74 ,  -10
87 ,  -14
100 ,  -17
115 ,  -18
129 ,  -19
143 ,  -20
157 ,  -20
172 ,  -21
187 ,  -22
202 ,  -23
216 ,  -25
230 ,  -28
243 ,  -32
260 ,  -36
277 ,  -36
294 ,  -37
310 ,  -39
325 ,  -39
339 ,  -38
357 ,  -33
371 ,  -29
387 ,  -24
404 ,  -21
420 ,  -20
436 ,  -18
450 ,  -14
461 ,  -12
465 ,  -11
476 ,  -9
487 ,  -3
497 ,  -2
506 ,  -1
514 ,  2
523 ,  7
535 ,  8
546 ,  10
557 ,  14
572 ,  19
579 ,  23
586 ,  25
598 ,  27
611 ,  33
624 ,  37
641 ,  42
658 ,  46
674 ,  44
691 ,  43
708 ,  46
722 ,  49
737 ,  48
751 ,  45
763 ,  40
775 ,  37
787 ,  35
800 ,  35
812 ,  34
818 ,  34
821 ,  37
825 ,  39
842 ,  43
857 ,  50
878 ,  51
897 ,  53
915 ,  55
932 ,  57
943 ,  60
960 ,  62
976 ,  68
988 ,  73
1006 ,  76
1018 ,  84
1030 ,  82
1046 ,  80
1062 ,  78
1072 ,  79
1081 ,  80
1089 ,  82
1104 ,  82
1118 ,  82
1133 ,  82
1145 ,  83
1157 ,  83
1171 ,  84
1183 ,  86
1196 ,  87
1211 ,  88
1222 ,  90
1233 ,  91
1247 ,  92
1261 ,  91
1278 ,  93
1296 ,  94
1314 ,  93
1332 ,  92
1343 ,  93
1355 ,  95
1368 ,  95
1381 ,  95
1395 ,  96
1413 ,  95
1429 ,  94
1443 ,  93
1452 ,  93
1456 ,  93
1456 ,  92
1456 ,  92
1456 ,  92
1456 ,  92
1456 ,  92
1456 ,  92
1456 ,  92"""

def record():
    robot.reset()
    gyro.reset_angle(0)
    while True:
        c=robot.distance()
        b=gyro.angle()
        ev3.screen.print(c,", ",b)
        print(c,", ",b)
        time.sleep(0.3)
def run(load=f, speed=200, t_prime=0.5):
    load=load.split("\n")
    d={}
    for i in load:
        x=i.replace(" ", "").split(",")
        d[int(x[0])]=int(x[1])
    t=t_prime
    t_prime=time.time()+t_prime
    cur_time=time.time()
    cur_speed=robot.state()[1]
    speed_calc=speed-cur_speed
    bm=robot.distance()+list(d.keys())[-1]
    heading = gyro.angle()
    x=0
    while robot.distance()<bm:
        search_key=robot.distance()
        angle=d.get(search_key) or d[min(d.keys(), key = lambda key: abs(key-search_key))]
        correction = (angle-gyro.angle()) * 2.
        if time.time() < t_prime:
            speed=(speed_calc)/t*(time.time()-cur_time)
        robot.drive(speed, correction)
        x+=1
    robot.stop()
    ev3.screen.print("sdr ",x)
    time.sleep(10)