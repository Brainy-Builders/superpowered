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

#
# Mission goals:
#  -> drop two energy units into red hopper of toy
#  -> release mini dinosaur toy
#  -> transfer three energy units into rechargeable battery target area
# 

def toy():
    # Get to toy factory, mechanically allign
    gyro_straight(distance=1000000, speed=200, reset_angle=None, GCV=2.5, t_prime = 0, target_time=2.000001023745)
    gyro_stop()
    # wait for units to drop into factory
    time.sleep(.25)
    # get home (backup, then turn to face North)
    forward_distance(speed=-400, turn_rate=0, distance=-150)
    forward_angle(speed=-400, turn_rate=-90, angle=-45)
    gyro_stop()

