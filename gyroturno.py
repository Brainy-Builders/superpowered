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
# Import other external modules that you usee
import time
import math
from common import *

# when making a Right turn, input angle should be positive
# when making a left turn, input angle should be negative
def gyrotest(loop, gyro1):
    #gyro.reset_angle(360)
    ev3.speaker.beep()
    for i in range(loop):
        print("in loop", i)
        gyroturno(-45 * i)
        ev3.speaker.beep()
        time.sleep(1)

def gyro_stop():
    robot.stop()
    left_wheel.brake()
    right_wheel.brake()
    left_wheel.brake()
    right_wheel.brake()


def gyroturno2(angle, rate_control=1, speed=0): 
    t_angle = angle
    # robot.stop()
    #t_angle is the target angle
    gyromod_360 = (-1 * gyro.angle()) % 360
    right_angle = (t_angle - gyromod_360) % 360 #0.24965278
    left_angle = (gyromod_360 - t_angle) % 360 
    previous_speed = 10
    if left_angle > right_angle:
        #right turn
        angle = gyro.angle() - right_angle
        print("right turn: left angle = ", left_angle," right angle = ", right_angle, " gyro angle ", gyro.angle(), " angle = ", angle)
        while gyro.angle() > angle:      
            difference=min(abs(3*(angle - gyro.angle())* rate_control), previous_speed)
            previous_speed += 1
            robot.drive(speed, (max(difference, 9)))
            #robot.drive(speed, max((angle - (gyro.angle())*(-1)) * 3 * rate_control, 9))
        # gyro_stop()

    elif right_angle > left_angle:
        #left turn
        angle = gyro.angle() + left_angle
        print("left turn: left angle = ", left_angle," right angle = ", right_angle, " gyro angle ", gyro.angle(), " angle = ", angle)
        while gyro.angle() < angle:
            difference=min(abs(3*(angle - gyro.angle())* rate_control), previous_speed)
            previous_speed += 1
            robot.drive(speed, (-1 * max(difference, 9)))
            #robot.drive(speed, min((angle - gyro.angle()) * 3 * rate_control, -9))
        # gyro_stop()

    return angle



def gyroturno(angle, rate_control=1, speed=0):
    previous_speed = 10
    gyroangle = gyro.angle()
    
    if gyroangle >= 180:
        while gyroangle >= 180:
            gyroangle -= 360

    elif gyroangle <= -180:
        while gyroangle <= -180:
            gyroangle += 360

    gyro.reset_angle(gyroangle)

    if gyroangle < angle:
        #right turn
        while gyro.angle() < angle:
            difference = min(abs(3*(angle - gyro.angle())* rate_control), previous_speed)
            previous_speed += 1
            robot.drive(speed, (max(difference, 9)))
    
    elif gyroangle > angle:
        #left turn
        while gyro.angle() > angle:
            difference=min(abs(3*(angle - gyro.angle())* rate_control), previous_speed)
            previous_speed += 1
            robot.drive(speed, (-1 * max(difference, 9)))  
    return gyro.angle()