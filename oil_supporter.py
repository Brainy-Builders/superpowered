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
    gyro_straight(distance=140, speed=250, t_prime=.6)
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
    gyro_straight(distance=85, speed=200, GCV=2.5/2)
    # forward_dist(speed=200, turn_rate=0, distance=200, t_prime=0.75)
    forward_angle(speed=200, turn_rate=19, angle=18)
    gyro_straight(200, 200)
    gyroturn(3, stop=False)
    # gyro_stop()
    # time.sleep(5)
    # forward_angle(speed=200, turn_rate=-20, angle=-20)

    # gyro_stop()
    # ev3.speaker.beep()
    # time.sleep(7)

    linefollow.line_follow(length=150+15,speed=125,sensor="right",side="right", Ki=0.0000,thresh=65)
    # gyro_stop()
    # time.sleep(5)

    gyro_straight(speed=300, reset_angle=7, target_time = 1.5)
 
    # robot.drive(400, 5)
    # time.sleep(1.5)
    # forward_dist(speed=200, turn_rate=0, distance=150)
    gyro_stop()
    
    acceleration("distance", 70)
    acceleration("heading", 70)
    for _ in range(3):
        # forward_dist(speed=-100, turn_rate=0, distance=-30)
        gyro_straight(45, -100)
        # robot.stop()
        # time.sleep(0.2)
        gyro_stop()
        robot.drive(400, 5)
        time.sleep(0.75)
        gyro_stop()
    acceleration("distance", 37)
    acceleration("heading", 30)
def hookcart_gohome():
    #main_motor.run_time(speed=-2000,time=700, wait=True) #down
    # forward_dist(-500, 0, -350, t_prime=1)
    gyro_straight(distance=200, speed=-200)
    robot.drive(-300, 25)
    time.sleep(2)
    robot.stop()

def main():
    gyro.reset_angle(angle=0)
    gotothere()
    hookcart_gohome()


def pumping_oil():
    # forward_dist(300, 0, 30)
    forward_dist(-100, 0, -40)
    for _ in range(3):
        robot.drive(150, 0)
        time.sleep(0.75)
        # forward_dist(-100, 0, -40)
        gyro_straight(-40, -100)
    gyro_stop()

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

def old_oil():
    def newstart():
        forward_dist(speed=300, turn_rate=0, distance=200, t_prime=0.75)
        forward_angle(speed=300, turn_rate=30, angle=25)
        ev3.speaker.beep()
        forward_angle(speed=300, turn_rate=-30, angle=-25)
        forward_dist(speed=200, turn_rate=0, distance=60)
        gyro_stop()

    def dump_energy():
        main_motor.run_time(speed=1500,time=1500, wait=True) #up
        # main_motor.run_time(speed=-300,time=1000, wait=False) #down

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
                main_motor.run_time(speed=-1500,time=2000, wait=True)
                forward_dist(speed=100, turn_rate=0, distance=30, t_prime=0)
            if robot.distance() < max_distance-80:
                turn_left = True
                gyro_stop()
                main_motor.run_time(speed=-1500,time=2000, wait=True)
                forward_dist(speed=100, turn_rate=0, distance=60, t_prime=0)
    def pump_oil():
        # ev3.speaker.beep()
        # move_motor(250, -570, mustWait=False) # down
        gyroturno(-95)
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
            if robot.distance() < max_distance-150:
                turn_right = True
        main_motor.run_angle(speed=500, rotation_angle=540, wait=False) # up
        gyro_stop()
        gyroturno(0)
        robot.drive(70, 0)
        time.sleep(1)
        robot.stop()
        # robot.straight(55)

    def hookcart_gohome():
        main_motor.run_time(speed=-2000,time=700, wait=True) #down
        robot.drive(-500, 27)
        time.sleep(1.7)
        robot.stop()
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