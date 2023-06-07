import math
import os
import time

from pybricks.ev3devices import (ColorSensor, GyroSensor, InfraredSensor,
                                 Motor, TouchSensor, UltrasonicSensor)
from pybricks.hubs import EV3Brick
from pybricks.media.ev3dev import Font, ImageFile, SoundFile
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import DataLog, StopWatch, wait

import linefollow
from common import *
from gyrostraight import *
from gyroturno import *
from pidlinefollow import *

#
# Mission goals:
#   -> Mechanically allign between oil plant and energy storage
#   -> Pump oil three times
#   -> Hook oil truck and drive home
#

def main():
    get_to_oil()
    pump_oil()
    hookcart_gohome()


def get_to_oil():
    #set acceleration
    acceleration("distance", 20)
    acceleration("heading", 20)

    #reset gyro against wall
    gyro.reset_angle(angle=0)

    #get behind oil
    gyro_straight(distance=200, reset_angle=30, speed=200, GCV=2.5/2)
    gyro_straight(distance=300, reset_angle=0, speed=200, GCV=2.5/2)

    #mechanically allign between oil plant and energy storage. (push into oil)
    gyro_straight(speed=300, reset_angle=0, target_time = 2.0)
     


def pump_oil():
    #faster acceleration
    acceleration("distance", 100)
    acceleration("heading", 100)

    #pump oil 3 times
    for _ in range(3):
        #back out of oil
        gyro_straight(distance=45, reset_angle=0, speed=-100)
        gyro_stop()

        #slight turn towards oil
        robot.turn(5)

        #push into oil and wait
        robot.drive(speed=400, turn_rate=0)
        time.sleep(0.75)
        gyro_stop()

def hookcart_gohome():
    #slower acceleration
    acceleration("distance", 37)
    acceleration("heading", 30)

    #back up and go home
    gyro_straight(distance=200, speed=-200)
    robot.drive(speed=-300, turn_rate=25)
    time.sleep(2)
    robot.stop()
    gyro_stop()
