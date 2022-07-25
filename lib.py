import time 
import math 
from common import *
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font
from gyroturno import *
from pidlinefollow import *
from linefollow import *
from line_a_line import *
def callum():
    print(robot.settings(600,300,100,100))
    #while True:
        #robot.straight(500)
        #forward_dist(speed = 300, turn_rate = 0, distance = 500)
        #gyro_stop()
        #time.sleep(5)
    #line_follow(0, 100, "left", "right", find_cross=True)
    #gyro_stop()
    line_a_line(speed=50, speed_approach = 200)
def turntest():
    robot.settings(turn_rate = 100)
    x = 0
    while True:
        robot.turn(-90)
        x += 1
        if x == 4:
            break
def pidtest():
    pidline('right', 1000000000000000, 80)
def gyrotest():
    gyro.reset_angle(0)
    gyroturno(90)
    gyroturno(180)
    gyroturno(270)
    gyroturno(0)
    robot.stop()
    gyroturno(-90)
    gyroturno(-180)
    gyroturno(-270)
    gyroturno(-0)
    robot.stop()