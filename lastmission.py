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

def mission():
    gyro_straight(500, 400, t_prime=1)
    robot.drive(400, 60)
    time.sleep(1)
    robot.stop()
    robot.drive(-100, -60)
    time.sleep(2)
    robot.stop()
    gyro_straight(100000, 1000, t_prime=1)