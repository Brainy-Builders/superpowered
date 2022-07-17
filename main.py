#!/usr/bin/env pybricks-micropython
#i commented -trey
import time 
import math 
from common import *
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font
from gyroturno import *
from pidlinefollow import *
def gyrotest():
    gyro.reset_angle(0)
    gyroturno(90)
    gyroturno(180)
    gyroturno(270)
    gyroturno(0)
    robot.stop()
    gyroturno(-90)
    gyroturno(-180)
    gyroturno(-270)
    gyroturno(-0)
    robot.stop()
#gyrotest()
def turntest():
    robot.settings(turn_rate = 100)
    x = 0
    while True:
        robot.turn(-90)
        x += 1
        if x == 4:
            break
pidline('right', 1000, 80)

