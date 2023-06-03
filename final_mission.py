#!/usr/bin/env pybricks-micropython
#import functions from pybrics, a python service for lego technic
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
#import basic functions and tools that help with all movements
import time
import math
#import motor names and ports, etc.
from common import *
#import the teams custom functions that allow for more accurate movement
from linefollow import line_follow
from pidlinefollow import *
from gyrostraight import *
from gyroturno import *

#     Mission Goals:
#        -->move forward and curve to the power to x area
#        -->quickly turn to toss the innovation project and units into the oval area
#        -->drive to the west home area to deliver the dinosaur with rechargeable unit

def main():
    #move  straight forward out of the east home area
    forward_distance(speed = 400, turn_rate = 0, distance = 350, t_prime = .5)
    #move forward and turn to avoid power plant
    forward_dist(speed = 300, turn_rate = 24, distance = 390)
    #move forward and turn back with a steep angle to toss out the innovation and energy units
    forward_angle(speed = 250, turn_rate =  -80, angle = -50)
    #use gyro sensor to go to the west home area 
    gyro_straight(distance= 1000, speed=700, GCV= 2.5)
    #stop the robot
    robot.stop()

