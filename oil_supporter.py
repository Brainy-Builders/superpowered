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

def followline():
    print("in")
    robot.stop()
    robot.settings(straight_acceleration=200, straight_speed=200, turn_acceleration=150, turn_rate=90)#don't know what to do for tunr rate.
    pidline(sensor='left', distance=400, speed = 200, Kp=0.3, Ki=0, Kd=1.0, find_cross = True)
    robot.stop()
    ev3.speaker.beep()
    time.sleep(2)
    robot.turn(90)
    ev3.speaker.beep()
    robot.straight(50)
    ev3.speaker.beep()
    move_motor(300, 720)