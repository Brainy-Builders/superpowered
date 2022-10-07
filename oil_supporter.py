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
import linefollow
from gyroturno import *
from gyrostraight import *
from pidlinefollow import *
import os
#def findline():
    #gyro.reset_angle(0)
    #move_motor(1000, 500, mustWait=False)
    #forward_dist(100,0,180)
    #ev3.speaker.beep(duration=25)
    #while(get_color(left_colorsensor) != Color.BLACK):
    #    robot.drive(100,0)
    #robot.turn(30)
    #robot.stop()


def followline_findcross():
    back_motor.run_time(-1000, 1000, wait=False)
    # move forward and find the line
    gyro_straight(distance=180, speed=300, t_prime=0.5) # use gyro at beginning 
    ev3.speaker.beep(duration=25)
    while(get_color(left_colorsensor) != Color.BLACK):
        robot.drive(75,0)

    # follow the line SMART distance
    dist=robot.distance()
    # forward_angle(speed=150, turn_rate=90, angle=30) # turn but keep moving forward
    smart_turn(left_wheel, left_colorsensor)
    linefollow.line_follow(length=440-dist,speed=200,sensor="left",side="right", find_cross=False)
    back_motor.run_time(800, 800, wait=False)
    dist = robot.distance()
    move_motor(1000, 900, mustWait=False)
    #main_motor.run_time(speed=1000,time=1200, wait=False)
    linefollow.line_follow(650-dist, speed=200, sensor = "left", side = "right", find_cross = True)
    # get to the cross
    ev3.speaker.beep(duration=25) # duration units [ms]
    while(get_color(right_colorsensor) != Color.BLACK):
        robot.drive(100,0)
    ev3.speaker.beep(duration=25)


def pump_oil():
    robot.straight(100)
    main_motor.run_time(speed=5000,time=2000)
    main_motor.run_time(speed=-7000,time=2500, wait=False)
    ev3.speaker.beep()
    robot.straight(-20)
    # move_motor(250, -570, mustWait=False) # down
    gyroturno(-90)
    robot.stop()
    ev3.speaker.beep()
    robot.drive(100, 0)
    time.sleep(1)
    forward_dist(speed=-50, turn_rate=0, distance=-10)
    robot.stop()
    for _ in range(2):
        main_motor.run_time(speed=1000,time=1100)  # up
        main_motor.run_time(speed=-1000,time=1100) # down
    main_motor.run_time(speed=1000,time=1100)
    #main_motor.run_time(speed=500,time=2000, wait=False) # up

def align_to_cart():
    while(get_color(right_colorsensor) != Color.BLACK):
        robot.drive(-60,0)
    ev3.speaker.beep()
    while(get_color(right_colorsensor) != Color.WHITE):
        robot.drive(-60,0)
    ev3.speaker.beep()
    gyro_stop()
    #move_motor(200, 500, mustWait=False)
    gyroturno(0)
    ev3.speaker.beep()
    #main_motor.run_time(speed=500,time=2000, wait=False)
    robot.straight(30)
    #time.sleep(1)

def hookcart_gohome():
    main_motor.run_time(speed=-1000,time=1100)
    robot.drive(-500, 28)
    time.sleep(1.5)
    robot.stop()

def main():
    # get ready
    gyro.reset_angle(angle=0)
    move_motor(speed=1000, angle=-1000, mustWait=False) # down
    # go
    followline_findcross()
    pump_oil()
    align_to_cart()
    hookcart_gohome()
    #for _ in range(10):
        #main_motor(speed=500, time=2200)
        #main_motor(speed=-500, time=2200)
        #time.sleep(5)

def oiltruck():
    gyro.reset_angle(0)
    #gyro_straight(distance=300, speed=200)
    #robot.stop()
    robot.settings(straight_speed=300, straight_acceleration=300, turn_rate=180,  turn_acceleration=180)
    #robot.straight(400)
    gyro_straight(distance=390, speed=230, reset_angle=None, GCV=2.5, t_prime = 1)
    #robot.drive(speed=200, turn_rate=0) 
    #time.sleep(0.3)
    robot.stop() 
    time.sleep(0.6)
    #goback
    gyro_straight(distance=420, speed=-340, reset_angle=None, GCV=2.5, t_prime = 1)
    #robot.drive(speed=-450, turn_rate=0)
    #time.sleep(0.7)
    robot.stop()