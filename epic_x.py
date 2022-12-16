

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


def main():
    forward_distance(400,0,350,.5)
    # robot.stop()
    forward_dist(300,27,500)
    forward_angle(250, -180, -50)
    # ev3.speaker.beep()
    # robot.stop()
    # gyroturno(-20)
    gyro_stop()
    time.sleep(.1)
    gyro_straight(distance= 1000, speed=700, GCV= 2.5, t_prime= 1)

    #forward_distance(700, 2, 1000, t_prime=1)
    # gyro_stop()
    # robot.drive(700,3)20
    
    # time.sleep(10)
    robot.stop()

