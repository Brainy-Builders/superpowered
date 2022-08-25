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
    robot.stop()
def waterfall():
    gyro.reset_angle(0)
    print("gyro: ", gyro.angle())
    ev3.screen.print(gyro.angle())
    drive(.23)
    gyroturno(45)
    drive(2)