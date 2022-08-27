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
    robot.settings(straight_acceleration = 250, straight_speed = 300)
    robot.straight(270)
    #forward_dist(300, 0, 270)
    #robot.settings(straight_acc = )
    robot.drive(200, 0)
    time.sleep(2)
    robot.stop()
    
    windthing()
    halftesla()
    

def windthing():
    # gyro.reset_angle(0)

    #go to wind#

    forward_dist(-100, 0, -150)
    gyroturno(-40)
    forward_dist(200, 0, 330)
    # find_colors(WHITE, "right", 70)
    # ev3.speaker.beep()
    # find_colors(BLACK, "right", 50)
    # ev3.speaker.beep()
    # find_colors(WHITE, "right", 50)
    # ev3.speaker.beep()
    while get_color(right_colorsensor) != Color.WHITE:  #
        robot.drive(70, 0)                              # Maybe these 3 lines should be a function with color as the argument
    robot.stop()          
    ev3.speaker.beep(25)                              #
    while get_color(right_colorsensor) != Color.BLACK:
        robot.drive(50, 0)
    robot.stop()
    ev3.speaker.beep(25) 
    while get_color(right_colorsensor) != Color.WHITE:
        robot.drive(50, 0)
    robot.stop()
    ev3.speaker.beep(25) 
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
        time.sleep(0.75)
        robot.stop()
        time.sleep(0.4)

    robot.stop()

def halftesla():
    # back_motor.run_until_stalled(speed=100, then=Stop.HOLD, duty_limit=None)
    gyro.reset_angle(45)
    forward_dist(-200, 0, -180)
    gyroturno(135)
    robot.stop()
    robot.drive(-200, 0)
    time.sleep(2)
    robot.stop()
    gyro.reset_angle(135)
    # forward_dist(-200, 0, -300)
    back_motor.run_time(speed = -200, time=700)
    forward_dist(300, 0, 100)
    robot.stop()
    back_motor.run_time(speed = 200, time = 700)
    gyroturno(135+90)
    robot.stop()
    forward_dist(100, 0, 80)
    gyroturno(-225)
    robot.drive(300, 0)
    time.sleep(4)
    robot.stop()
    # Try this: 
    # back_motor.run_until_stalled(speed=100, then=Stop.HOLD, duty_limit=None)
    # back_motor.run_until_stalled(100, stop_type=Stop.HOLD)
def find_colors(color, sensor, speed=60):
    if sensor == "right":
        csensor = right_colorsensor
    elif sensor == "left":
        csensor = left_colorsensor

    if color == "white" or "WHITE":
        while get_color(csensor) != Color.WHITE:  
            robot.drive(speed, 0)                              
        robot.stop()
    elif color == "black" or "BLACK":
        while get_color(csensor) != Color.BLACK:  
            robot.drive(speed, 0)                              
        robot.stop()
    # else:
    #     while get_color(right_colorsensor) != Color.WHITE:  
    #         robot.drive(speed, 0)                              
    #     robot.stop()