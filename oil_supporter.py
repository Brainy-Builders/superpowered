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
from linefollow import line_follow
from common import *
from pidlinefollow import *

def findline():
    gyro.reset_angle(0)
    move_motor(1000, 500, mustWait=False)
    forward_dist(100,0,180)
    ev3.speaker.beep(duration=25)
    while(get_color(left_colorsensor) != Color.BLACK):
        robot.drive(100,0)
    robot.turn(30)
    robot.stop()

def followline_findcross():
    ev3.speaker.beep(duration=25)
    pidline(sensor='left', distance=320, speed=200, Kp=0.2, Ki=0.001, Kd=0.3, find_cross = False)
    ev3.speaker.beep(duration=25) # duration units [ms]
    while(get_color(right_colorsensor) != Color.WHITE):
        robot.drive(50,0)
    ev3.speaker.beep()
    while(get_color(right_colorsensor) != Color.BLACK):
        robot.drive(50,0)
    ev3.speaker.beep()
    gyro_stop()

def pump_oil():
    robot.straight(70)
    ev3.speaker.beep()
    move_motor(200, -570, mustWait=False)
    gyroturno(-90)
    robot.stop()
    ev3.speaker.beep()
    time.sleep(1)
    robot.drive(100, 0)
    time.sleep(0.6)
    robot.stop()
    for _ in range(3):
        move_motor(1000, 600)
        move_motor(1000, -600)
    #move_motor(1000, 600)
    #move_motor(1000, -600)
    #move_motor(1000, 600)
    #move_motor(1000, -600)

def align_to_cart():
    gyro.reset_angle(-90)
    while(get_color(right_colorsensor) != Color.BLACK):
        robot.drive(-60,0)
    ev3.speaker.beep()
    while(get_color(right_colorsensor) != Color.WHITE):
        robot.drive(-60,0)
    ev3.speaker.beep()
    gyro_stop()
    move_motor(200, 500, mustWait=True)
    gyroturno(0)
    ev3.speaker.beep()
    robot.straight(30)

def hook_cart():
    move_motor(300, -370)

def main():
    findline()
    followline_findcross()
    pump_oil()
    align_to_cart()
    hook_cart()