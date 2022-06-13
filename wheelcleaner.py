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

def wheelcleaner():
    ev3.screen.print("wheel cleaner program started")
    right_wheel.run_angle(300, (360 * 3))
    ev3.speaker.beep()
    time.sleep(2)
    left_wheel.run_angle(300, (360 * 3))
    ev3.speaker.beep()
    ev3.screen.print("wheel cleaner program done") 