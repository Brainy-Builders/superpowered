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

def newstart():
    forward_dist(300, 0, 300, t_prime=0.75)
    forward_angle(300, 45, 30)
    # 
    ev3.speaker.beep()
    # move_motor(speed=600, angle=700, mustWait=False)
    forward_angle(300, -45, -30)
    #gyro_stop()

# def followline_findcross():
#     # move forward and find the line
#     gyro_straight(distance=200, speed=300, t_prime=0.5) # use gyro at beginning 
#     ev3.speaker.beep(duration=25)
#     while(get_color(left_colorsensor) != Color.BLACK):
#         robot.drive(200,0)

#     # follow the line SMART distance
#     dist=robot.distance()
#     gyroturno(30)
#     forward_dist(400, 0, 130, t_prime = 0.5)
#     move_motor(speed=600, angle=700, mustWait=False)
    
#     # continue to the cross
#     dist = robot.distance()
#     #move_motor(speed=600, angle=700, mustWait=False)
#     # linefollow.line_follow(650-dist, speed=125, sensor = "left", side = "right", find_cross = True)
#     ev3.speaker.beep(duration=25) # duration units [ms]
#     gyroturno(0)
#     while(get_color(right_colorsensor) != Color.BLACK):
#         robot.drive(150, 0)
#     # forward_dist(200, 0, 200, t_prime=0.5)
#     robot.stop()

def dump_energy():
    forward_dist(speed=200, turn_rate=0, distance=50)
    gyro_stop()
    main_motor.run_time(speed=1000,time=1000, wait=True) #up
    main_motor.run_time(speed=-1000,time=1500, wait=False) #down
    forward_dist(-100, 0, -15, t_prime=0.3)
    gyro_stop()

def pump_oil():
    # ev3.speaker.beep()
    # move_motor(250, -570, mustWait=False) # down
    gyroturno(-90)
    robot.drive(110, 0)
    time.sleep(1.2)
    forward_dist(speed=-40, turn_rate=0, distance=-10)
    robot.stop()
    for _ in range(2):
        main_motor.run_time(speed=1000,time=1100)  # up
        main_motor.run_time(speed=-1000,time=1100) # down
    main_motor.run_time(speed=1000,time=1100)

def align_to_cart():
    turn_right = False
    max_distance = robot.distance()
    while turn_right == False:
      robot.drive(-60,0)
      if (get_color(right_colorsensor) == Color.BLACK):
        turn_right = True
      if robot.distance() > max_distance+150:
        turn_right = True
    ev3.speaker.beep()
    move_motor(400, -450, mustWait=False)
    forward_dist(-200, 0, -20, t_prime=0.2)
    # while(get_color(right_colorsensor) != Color.BLACK):
    #     robot.drive(-60,0)
    # ev3.speaker.beep()
    # while(get_color(right_colorsensor) != Color.WHITE):
    #     robot.drive(-60,0)
    ev3.speaker.beep()
    gyro_stop()
    #main_motor.run_time(speed=-450,time=1100, wait=False)
    gyroturno(0)
    ev3.speaker.beep()
    #main_motor.run_time(speed=500,time=2000, wait=False)
    robot.straight(40)
    #time.sleep(1)

def hookcart_gohome():
    main_motor.run_time(speed=-1500,time=1500)
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