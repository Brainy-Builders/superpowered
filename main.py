#!/usr/bin/env pybricks-micropython
import time 
import math 
from common import *
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font
from gyroturno import *

def gyrotest():
    gyro.reset_angle(360)
    gyroturno(90)
    gyro.reset_angle(-720)
    gyroturno(-90)
    gyro.reset_angle(405)
    gyroturno(90)
    robot.stop()
gyrotest()
