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
    # gyro.reset_angle(0)
    # forward_distance(400, 0, 26, 1)
    # time.sleep(1)
    # gyroturno(-62)
    # forward_distance(400, 0, 250, 1)
    # robot.drive(200, 0)
    # time.sleep(1.5)
    # robot.stop()
    # move_motor(400, 900)
    # time.sleep(.5)
    # forward_distance(-800, 0, -80, 1)
    # robot.drive(-800, 80)
    # time.sleep(1)
    # robot.stop()
    toy_alternative()
    

def toy_alternative():
    gyro_straight(distance=290, speed=400, reset_angle=None, t_prime = 1)
    ev3.speaker.beep()
    robot.drive(300, 0)
    time.sleep(.7)
    robot.drive(200,0)
    time.sleep(0.3)
    gyro_stop()
    time.sleep(.25)
    forward_distance(-400, 0, -150, 0)
    robot.drive(-400, 0)
    time.sleep(1)
    robot.stop()

