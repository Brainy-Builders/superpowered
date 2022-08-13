from common import *
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font
from gyroturno import *
from pidlinefollow import *
from linefollow import *
from line_a_line import *
from gyrostraight import *
from lib import *
def flip_tv():
    gyro.reset_angle(0)
    ev3.speaker.beep()
    forward_dist(300, 0, 370)
    #robot.settings(straight_acc = )
    robot.drive(200, 0)
    time.sleep(2)
    robot.stop()
    
    windthing()
    

def windthing():
    #gyro.reset_angle(0)

    #go to wind#

    forward_dist(-100, 0, -100)
    gyroturno(-40)
    forward_dist(200, 0, 280)
    while get_color(right_colorsensor) != Color.WHITE:  #
        robot.drive(70, 0)                              # Maybe these 3 lines should be a function with color as the argument
    robot.stop()                                        #
    while get_color(right_colorsensor) != Color.BLACK:
        robot.drive(50, 0)
    robot.stop()
    while get_color(right_colorsensor) != Color.WHITE:
        robot.drive(50, 0)
    robot.stop()
    forward_dist(50, 0, 20)
    gyroturno(43)
    forward_dist(100, 0, 85)

    #collecting the energy units#


    xyz = 0                  #
    while xyz  < 3:          # Replace these three lines with "while _ in range(3):"
        xyz += 1             #
        robot.drive(200, 0)
        time.sleep(0.8)
        robot.drive(-100, 0)
        time.sleep(0.5)
        robot.stop()
        time.sleep(0.3)

    robot.stop()

def halftesla():
    # gyro.reset_angle(45)
    # forward_dist(-300, 0, -200)
    # gyroturno(135)
    # robot.stop()
    # robot.drive(-200, 0)
    # time.sleep(4)
    # robot.stop()
    #forward_dist(-200, 0, -300)
    # Try this: back_motor.run_until_stalled(speed=100, then=Stop.HOLD, duty_limit=None)
    back_motor.run_until_stalled(100, stop_type=Stop.HOLD)