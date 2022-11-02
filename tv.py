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
    # ev3.speaker.beep()
    back_motor.run_time(speed = 200, time=200, wait=False) # make sure UP
    gyro_straight(distance=270, speed=250) # add acceleration
    robot.drive(170, 0)
    time.sleep(2.75 - 1.75)
    gyro_stop()
    # ev3.speaker.beep()
    # time.sleep(3)

    windthing()
    halftesla2()
    
def windthing(): #go to wind#
    gyro_straight(150, -100)
    gyroturno(-45+5-2)
    forward_dist(speed = 400, turn_rate = 1, distance = 300, t_prime=1) # slight turn right to not miss white line
    # ev3.speaker.beep(25)
    turn_right = False
    max_distance = robot.distance()
    while turn_right == False:
      robot.drive(100,0)
      if right_colorsensor.reflection() < 25:
        turn_right = True
      if robot.distance() > max_distance+100:
        turn_right = True
    # while get_color(right_colorsensor) != Color.WHITE:  
    #     robot.drive(50, 0)                              
    robot.stop()
    # ev3.speaker.beep(25) 
    # while get_color(right_colorsensor) != Color.WHITE:
    #     robot.drive(50, 0)
    # robot.stop()
    # ev3.speaker.beep(25) 
    forward_dist(speed = 50, turn_rate = 0, distance = 50) # go slightly past white
    gyroturno(45)
    forward_dist(speed = 250, turn_rate = 0, distance = 85)
    
    #collecting the energy units#

    for _ in range(3):
        robot.drive(300, 0)
        time.sleep(0.85)
        robot.stop()
        time.sleep(0.2)
        robot.drive(-100, 0)
        time.sleep(0.75)
        robot.stop()
        time.sleep(0.2)
    robot.stop()

def halftesla():
    # back_motor.run_until_stalled(speed=100, then=Stop.HOLD, duty_limit=None)
    gyro.reset_angle(45)
    # forward_dist(-200, 0, -140)
    gyro_straight(distance=130, speed=-200)
    gyroturno(137)
    # robot.stop()
    robot.drive(-200,-5) # slight angle into the car model
    time.sleep(1.5)
    robot.stop()
    # gyro.reset_angle(135)  # uncomment if/when reliably aligned
    # forward_dist(-200, 0, -300)
    back_motor.run_time(speed = -200, time=800)  # down
    forward_dist(speed=375, turn_rate=0, distance=100)
    forward_dist(speed=375, turn_rate=0, distance=50) # extra distance to allow car to fall
    gyro_stop()
    time.sleep(0.5)
    back_motor.run_time(speed = 200, time = 700, wait=False) # up
    gyroturno(135+82, rate_control=0.5)
    robot.stop()
    forward_dist(100, 0, 140)

    gyroturno(-225, rate_control=0.7)  # move forward here
    gyro_straight(700, 500)
    # robot.turn(-70)       # most of the turn
    # robot.drive(200,-100) # rest of the turn while moving forward to keep energy unit
    # time.sleep(0.5)
    # robot.drive(300,0)    # get the rest of the way home

    # time.sleep(2)
    robot.stop()
    # Try this: 
    # back_motor.run_until_stalled(speed=100, then=Stop.HOLD, duty_limit=None)
    # back_motor.run_until_stalled(100, stop_type=Stop.HOLD)

def halftesla2():
    # backup into car
    forward_dist(speed=-250, turn_rate=0, distance=-120, t_prime = 0.5)
    gyroturno(120)
    # ev3.speaker.beep()
    # time.sleep(3)
    robot.drive(speed=-250,turn_rate=0) 
    time.sleep(0.75)
    back_motor.run_time(speed = -200, time=800, wait=False)  # down
    time.sleep(0.75)
    gyro_stop()
    ev3.speaker.beep()
    # time.sleep(3)
    # Let car down
    forward_dist(speed=200, turn_rate=0, distance=230, t_prime=0.5)
    gyro_stop()
    back_motor.run_time(speed = 400, time = 1000, wait=False) # up
    # ev3.speaker.beep()
    # time.sleep(3)
    # push the car away, then run into Toy Factory
    forward_angle(speed=-150, turn_rate=90, angle=90)
    gyro_stop()
    ev3.speaker.beep()
    # time.sleep(3)
    forward_dist(speed=200, turn_rate=4, distance=250, t_prime=0.5)
    robot.drive(speed=200, turn_rate=0)
    time.sleep(0.5)
    gyro_stop()
    ev3.speaker.beep()
    # time.sleep(3)
    
    # backup, turn, go home
    forward_dist(speed=-100, turn_rate=0, distance=-25)
    gyroturno(angle=-225, rate_control=1.0, speed=50)  # move forward here
    forward_dist(speed=600, turn_rate=5, distance=500, t_prime=1.0)
    robot.drive(speed=800, turn_rate=0)
    time.sleep(1)
    gyro_stop()

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