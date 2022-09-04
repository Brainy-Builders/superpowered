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
    back_motor.run_time(speed = 200, time=200, wait=False) # make sure UP
    gyro_straight(200, 250)
    # robot.settings(straight_acceleration = 200, straight_speed = 300)
    # robot.straight(270)
    #forward_dist(300, 0, 270)
    #robot.settings(straight_acc = )
    robot.drive(200, 0)
    time.sleep(1.75)
    robot.stop()
    
    windthing()
    halftesla()
    

def windthing(): #go to wind#
    gyro_straight(150, -100)
    gyroturno(-45)
    forward_dist(speed = 200, turn_rate = 2, distance = 330) # slight turn right to not miss white line
    ev3.speaker.beep(25)
    while get_color(right_colorsensor) != Color.WHITE:  
        robot.drive(50, 0)                              
    # robot.stop()          
    # ev3.speaker.beep(25)                              #
    # while get_color(right_colorsensor) != Color.BLACK:
    #     robot.drive(50, 0)
    robot.stop()
    ev3.speaker.beep(25) 
    # while get_color(right_colorsensor) != Color.WHITE:
    #     robot.drive(50, 0)
    # robot.stop()
    # ev3.speaker.beep(25) 
    forward_dist(speed = 50, turn_rate = 0, distance = 25) # distance from white to black 
    forward_dist(speed = 50, turn_rate = 0, distance = 50) # rest of the distance 
    gyroturno(45)
    forward_dist(speed = 100, turn_rate = 0, distance = 85)
    
    #collecting the energy units#

    for _ in range(4):          # one extra for luck?
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
    # forward_dist(-200, 0, -140)
    gyro_straight(distance=140, speed=-200)
    gyroturno(135)
    # robot.stop()
    robot.drive(-100,-5) # slight angle into the car model
    time.sleep(2.5)
    robot.stop()
    # gyro.reset_angle(135)  # uncomment if/when reliably aligned
    # forward_dist(-200, 0, -300)
    back_motor.run_time(speed = -200, time=700)  # down
    forward_dist(speed=375, turn_rate=0, distance=100)
    forward_dist(speed=375, turn_rate=0, distance=50) # extra distance to allow car to fall
    gyro_stop()
    back_motor.run_time(speed = 200, time = 700, wait=False) # up
    gyroturno(135+90)
    robot.stop()
    forward_dist(100, 0, 120)

    # gyroturno(-225, rate_control=0.7)  # move forward here
    # gyro_straight(600, 500)
    robot.turn(-70)       # most of the turn
    robot.drive(200,-100) # rest of the turn while moving forward to keep energy unit
    time.sleep(0.5)
    robot.drive(300,0)    # get the rest of the way home

    time.sleep(2)
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