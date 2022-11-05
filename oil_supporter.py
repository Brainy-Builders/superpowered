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

def newstart():
    forward_dist(speed=300, turn_rate=0, distance=200, t_prime=0.75)
    forward_angle(speed=300, turn_rate=30, angle=25)
    ev3.speaker.beep()
    forward_angle(speed=300, turn_rate=-30, angle=-25)
    forward_dist(speed=200, turn_rate=0, distance=60)
    gyro_stop()

def dump_energy():
    main_motor.run_time(speed=1000,time=1000, wait=True) #up
    main_motor.run_time(speed=-1000,time=1500, wait=False) #down

def backup_from_energy():
    turn_left=False
    max_distance = robot.distance()
    while turn_left == False:
      if Button.CENTER == ev3.buttons.pressed:
        raise Exception
      robot.drive(-100,0)
      if (get_color(right_colorsensor) == Color.WHITE):
        turn_left = True
        gyro_stop()
        forward_dist(speed=100, turn_rate=0, distance=30, t_prime=0)
      if robot.distance() < max_distance-80:
        turn_left = True
        gyro_stop()
        forward_dist(speed=100, turn_rate=0, distance=60, t_prime=0)
    

def pump_oil():
    # ev3.speaker.beep()
    # move_motor(250, -570, mustWait=False) # down
    gyroturno(-90)
    robot.drive(110, 0)
    time.sleep(1.2)
    forward_dist(speed=-40, turn_rate=0, distance=-10)
    robot.stop()
    for _ in range(2):
        main_motor.run_time(speed=1000,time=1100, wait=True)  # up
        main_motor.run_time(speed=-1000,time=1100, wait=True) # down
    main_motor.run_time(speed=1000,time=1100, wait=True) # up
    main_motor.run_time(speed=-1000,time=1100, wait=False) # down

def align_to_cart():
    turn_right = False
    max_distance = robot.distance()
    while turn_right == False:
      robot.drive(-60,0)
      if (get_color(right_colorsensor) == Color.BLACK):
        turn_right = True
        forward_dist(speed=-60, turn_rate=0, distance=-20, t_prime=0)
      if robot.distance() > max_distance+150:
        turn_right = True
    main_motor.run_angle(speed=500, rotation_angle=540, wait=False) # up
    gyro_stop()
    gyroturno(0)
    robot.straight(40)

def hookcart_gohome():
    main_motor.run_time(speed=-2000,time=700, wait=True) #down
    robot.drive(-500, 27)
    time.sleep(1.7)
    robot.stop()

def main():
    # get ready
    gyro.reset_angle(angle=0)
    move_motor(speed=1000, angle=-500, mustWait=False) # down
    # go
    newstart()
    #followline_findcross()
    dump_energy()
    try:
        backup_from_energy()
    except:
        ev3.speaker.beep()
        return 0
    pump_oil()
    align_to_cart()
    hookcart_gohome()

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