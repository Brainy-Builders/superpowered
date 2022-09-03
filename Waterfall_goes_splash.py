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
from linefollow import line_follow
from common import *
from pidlinefollow import *

def drive(tim, sped = 500, turn = 0):
    robot.drive(sped, turn)
    time.sleep(tim)

def waterfall():
    gyro.reset_angle(0)
    print("gyro: ", gyro.angle())
    ev3.screen.print(gyro.angle())
    drive(.23)
    gyroturno(45)
    drive(2)

def get_there(): # Get there without stopping until at the mission model
    main_motor.run_time(300, 2000, wait = False)
    robot.drive(230,0)
    time.sleep(0.225)
    robot.drive(200,90)
    time.sleep(0.5)
    robot.drive(300,0)
    time.sleep(1.0)
    robot.stop()

def hang_water():
    main_motor.run_until_stalled(-1000)
    move_motor(1000, 500)
    robot.drive(-200, 0) 
    time.sleep(0.2)
    robot.stop()


def lift_and_collect():
    move_motor(400, -80, mustWait = False)
    robot.drive(-300, 0)
    time.sleep(.5)
    robot.drive(300, 0)
    time.sleep(.5)
    robot.stop()
    main_motor.run_time(300, 2000)

    

def get_home():
    robot.drive(-500, 0)
    time.sleep(2)
    robot.stop()

def waterfall2():
    #get_there()
    hang_water()
    # lift_ando_collect()
    # get_home()