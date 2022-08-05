import time 
import math 
from common import *
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font
from gyroturno import *
from pidlinefollow import *
def callum():
    print(robot.settings(600,300,100,100))
    while True:
        robot.straight(500)
        gyroturno.gyro_stop()
        time.sleep(5)
def turntest():
    robot.settings(turn_rate = 100)
    x = 0
    while True:
        robot.turn(-90)
        x += 1
        if x == 4:
            break
def pidtest():
    pidline('right', 1000, 80)
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
def view_color():
    ev3.screen.set_font(med_font)
    while Button.CENTER not in ev3.buttons.pressed():
        ev3.screen.clear()
        r_color = str(right_colorsensor.color())
        l_color = str(left_colorsensor.color())
        ev3.screen.print("left color: {}\nright color: {}".format(l_color, r_color))