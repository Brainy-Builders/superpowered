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
def gyro_adjust(func):
    def wrap(*args, **kwargs):
        _=gyro.angle()
        result = func(*args, **kwargs)
        _=gyro.angle()
        return result
    return wrap
# when making a Right turn, input angle should be positive
# when making a left turn, input angle should be negative
def gyrotest(loop, gyro1):
    #gyro.reset_angle(360)
    ev3.speaker.beep()
    for i in range(loop):
        print("in loop", i)
        gyroturno2(45 * 1)
        ev3.speaker.beep()
        time.sleep(5)

def gyro_stop():
    robot.stop()
    left_wheel.brake()
    right_wheel.brake()
    # Again since sometimes one motor keeps running!
    left_wheel.brake()
    right_wheel.brake()
    time.sleep(0.1)

def gyroturno(angle, rate_control=1.2, speed=0, stop=True): 
    gyromod_360 = (1 * gyro.angle()) % 360
    right_angle = (angle - gyromod_360) % 360 #0.24965278
    left_angle = (gyromod_360 - angle) % 360    

    previous_speed = 10
    if left_angle > right_angle:
        #right turn
        #t_angle is the target angle
        t_angle = gyro.angle() + right_angle 
        # print("right turn: left angle = ", left_angle," right angle = ", right_angle, " gyro angle ", gyro.angle(), " t_angle = ", t_angle)
        while gyro.angle() <= t_angle:      
            difference=min(abs(3*(t_angle - gyro.angle())* rate_control), previous_speed)
            previous_speed += 1
            robot.drive(speed, (max(difference, 9)))

    elif right_angle > left_angle:
        #left turn
        #t_angle is the target angle
        t_angle = gyro.angle() - left_angle
        # print("left turn: left angle = ", left_angle," right angle = ", right_angle, " gyro angle ", gyro.angle(), " t_angle = ", t_angle)
        while gyro.angle() >= t_angle:
            difference=min(abs(3*(t_angle - gyro.angle())* rate_control), previous_speed)
            previous_speed += 1
            robot.drive(speed, (-1 * max(difference, 9)))
    if stop:
        gyro_stop()
    return gyro.angle()
@gyro_adjust
def gyroturn(angle, rate_control=1.2, speed=0, stop=True):
    DEBUG = False
    _ = gyro.angle() # leave to regulate gyro input
    gyromod_360 = (1 * gyro.angle()) % 360
    right_angle = (angle - gyromod_360) % 360 
    left_angle = (gyromod_360 - angle) % 360    

    # Quickly return if already pointed in the right direction
    if(min(right_angle, left_angle) <=1):
        return 

    old_angle = gyro.angle()
    old_time = time.time()
    old_speed = gyro.speed()

    if left_angle > right_angle:
        turn_direction = 'right'
        t_angle = old_angle + right_angle 
        direction_multiplier = 1
    else:
        turn_direction = 'left'  
        direction_multiplier = -1  
        t_angle = old_angle - left_angle

    while (turn_direction == 'right' and old_angle <= (t_angle)) or (turn_direction == "left" and old_angle >= (t_angle)):
        new_speed = gyro.speed()
        current_time = time.time()
        time_diff = current_time - old_time
        angel = old_angle + time_diff*((new_speed+old_speed)/2)

        difference=abs(3*(t_angle - angel)* rate_control)
        target_rate = (direction_multiplier * min(300,max(difference, 25)))
        robot.drive(speed, target_rate)
            
        old_angle = angel
        old_time = current_time
        old_speed = new_speed
            
    if stop:
        gyro_stop()

    # For some reason, two rest_angle() calls are needed! Please keep!
    gyro.reset_angle(old_angle)  # keep
    time.sleep(0.01)            # also keep
    gyro.reset_angle(old_angle)  # keep me too!

    if(DEBUG):
        for point in range(10):
            print("  (tail of gyro)",point,"gyro_angle:", gyro.angle())
            time.sleep(0.01)
        gyro.reset_angle(old_angle)
        for point in range(10):
            print("   2 (tail of gyro)",point,"gyro_angle:", gyro.angle())
            time.sleep(0.01)
    return old_angle