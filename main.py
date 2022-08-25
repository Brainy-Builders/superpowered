#!/usr/bin/env pybricks-micropython
#i commented -trey
import time 
import math 
import os
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font
from gyroturno import *
from pidlinefollow import *
import common
gyro.reset_angle(0)
ev3.screen.draw_image(x = 0, y = 0, source = "splash.png", transparent=None)
<<<<<<< HEAD
#os.popen("""beep -f 617 -l 300 -n -f 824 -l $((300 * 3/2)) -n -f 980 -l $((300/2)) -n -f 873 -l 300 -n -f 824 -l $((300 * 2)) -n -f 1234 -l 300 -n -f 1100 -l $((300*5/2)) -n -f 925 -l $((300*5/2)) -n -f 824 -l $((300*3/2)) -n -f 980 -l $((300/2)) -n -f 873 -l 300 -n -f 777 -l $((300*2)) -n -f 873 -l 300 -n -f 617 -l $((300*5/2))""")
#time.sleep(5)
=======
# os.popen("""beep -f 617 -l 300 -n -f 824 -l $((300 * 3/2)) -n -f 980 -l $((300/2)) -n -f 873 -l 300 -n -f 824 -l $((300 * 2)) -n -f 1234 -l 300 -n -f 1100 -l $((300*5/2)) -n -f 925 -l $((300*5/2)) -n -f 824 -l $((300*3/2)) -n -f 980 -l $((300/2)) -n -f 873 -l 300 -n -f 777 -l $((300*2)) -n -f 873 -l 300 -n -f 617 -l $((300*5/2))""")
# time.sleep(5)
>>>>>>> 72d053e7b8e12480a5aa449b0b348c20692e9cf5
import menu

#gyrotest()

#IF YOU FOUND THIS YOU ARE smart
#😎












