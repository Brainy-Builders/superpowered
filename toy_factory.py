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
from gyrostraight import *
from gyroturno import *


def toy():
    #Get to toy factory and allign
    gyro_straight(distance=290, speed=400, reset_angle=None, t_prime = 1)
    robot.drive(300, 0)
    time.sleep(.7)
    robot.drive(200,0)
    time.sleep(0.3)
    gyro_stop()
    # wait for units to drop into factory
    time.sleep(.25)
    # get home
    forward_distance(-400, 0, -150, 0)
    forward_angle(-400, -90, -45)
    gyro_stop()

