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

# def newstart():
#     forward_dist(speed=300, turn_rate=0, distance=200, t_prime=0.75)
#     forward_angle(speed=300, turn_rate=30, angle=25)
#     ev3.speaker.beep()
#     forward_angle(speed=300, turn_rate=-30, angle=-25)
#     forward_dist(speed=200, turn_rate=0, distance=60)
#     gyro_stop()
def gototherewline():
    gyro.reset_angle(angle=0)
    gyro_straight(distance=180, speed=250, t_prime=.6)
    while(get_color(left_colorsensor) != Color.BLACK):
        robot.drive(100,0)
    dist=robot.distance()
    forward_angle(speed=150, turn_rate=90, angle=30)
    linefollow.line_follow(440-30-dist, speed=175-50, sensor="left", side="right")
    dist=robot.distance()
    linefollow.line_follow(length=650-dist,speed=150,sensor="left",side="right")
    while(get_color(right_colorsensor) != Color.BLACK):
        robot.drive(75,0)
    gyro_straight(distance=100, speed=200)

def gotothere():
    gyro.reset_angle(0)
    gyro_straight(distance=125, speed=200, t_prime=1.0)
    # forward_dist(speed=200, turn_rate=0, distance=200, t_prime=0.75)
    forward_angle(speed=200, turn_rate=20, angle=20)
    
    forward_angle(speed=200, turn_rate=-20, angle=-20)
    turn=None
    if get_color(right_colorsensor)==Color.BLACK:
        turn=10
        ev3.light.on(Color.ORANGE)
    elif get_color(left_colorsensor)==Color.WHITE:
        turn=-10
        ev3.light.on(Color.RED)
    else:
        ev3.light.on(Color.GREEN)
    gyro_straight(distance=100, speed=200, t_prime=0.0,reset_angle=turn)
    ev3.speaker.beep()
    robot.drive(200, 0)
    time.sleep(1.0)
    # forward_dist(speed=200, turn_rate=0, distance=150)
    robot.stop()
    ev3.speaker.beep()
    for _ in range(4):
        forward_dist(speed=-100, turn_rate=0, distance=-40)
        robot.drive(300, 10)
        time.sleep(0.75)
    gyro_stop()
    ev3.light.off()
def gototheregyro():
    gyro.reset_angle(0)
    gyro_straight(700, 200, t_prime=1)
    ev3.speaker.beep()
    robot.drive(100, 0)
    time.sleep(1.0)
    for _ in range(4):
        forward_dist(speed=-100, turn_rate=0, distance=-40)
        robot.drive(200, 0)
        time.sleep(0.75)
    gyro_stop()

def pumping_oil():
    # forward_dist(300, 0, 30)
    forward_dist(-100, 0, -40)
    for _ in range(3):
        robot.drive(150, 0)
        time.sleep(0.75)
        forward_dist(-100, 0, -40)
    gyro_stop()

def main():
    # get ready
    gyro.reset_angle(angle=0)
    gotothere()
    # newstart()
    # pumping_oil()
    #move_motor(speed=1000, angle=-500, mustWait=False) # down
    # go
    #followline_findcross()
    #dump_energy()
    #try:
    #    backup_from_energy()
    #except:
    #    ev3.speaker.beep()
    #    return 0
    #pump_oil()
    #align_to_cart()
    hookcart_gohome()


# def dump_energy():
#     main_motor.run_time(speed=1000,time=1000, wait=True) #up
#     main_motor.run_time(speed=-1000,time=1500, wait=False) #down

# def backup_from_energy():
#     turn_left=False
#     max_distance = robot.distance()
#     while turn_left == False:
#       if Button.CENTER == ev3.buttons.pressed:
#         raise Exception
#       robot.drive(-100,0)
#       if (get_color(right_colorsensor) == Color.WHITE):
#         turn_left = True
#         gyro_stop()
#         forward_dist(speed=100, turn_rate=0, distance=30, t_prime=0)
#       if robot.distance() < max_distance-80:
#         turn_left = True
#         gyro_stop()
#         forward_dist(speed=100, turn_rate=0, distance=60, t_prime=0)
    

# def pump_oil():
#     # ev3.speaker.beep()
#     # move_motor(250, -570, mustWait=False) # down
#     gyroturno(-90)
#     robot.drive(110, 0)
#     time.sleep(1.2)
#     forward_dist(speed=-40, turn_rate=0, distance=-10)
#     robot.stop()
#     for _ in range(2):
#         main_motor.run_time(speed=1000,time=1100, wait=True)  # up
#         main_motor.run_time(speed=-1000,time=1100, wait=True) # down
#     main_motor.run_time(speed=1000,time=1100, wait=True) # up
#     main_motor.run_time(speed=-1000,time=1100, wait=False) # down

# def align_to_cart():
#     turn_right = False
#     max_distance = robot.distance()
#     while turn_right == False:
#       robot.drive(-60,0)
#       if (get_color(right_colorsensor) == Color.BLACK):
#         turn_right = True
#         forward_dist(speed=-60, turn_rate=0, distance=-20, t_prime=0)
#       if robot.distance() > max_distance+150:
#         turn_right = True
#     main_motor.run_angle(speed=500, rotation_angle=540, wait=False) # up
#     gyro_stop()
#     gyroturno(0)
#     robot.straight(40)

def hookcart_gohome():
    #main_motor.run_time(speed=-2000,time=700, wait=True) #down
    # forward_dist(-500, 0, -350, t_prime=1)
    gyro_straight(distance=350, speed=-225, t_prime=1)
    robot.drive(-500, 35)
    time.sleep(1)
    robot.stop()

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