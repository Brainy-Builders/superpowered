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
    gyro_straight(distance=300, speed=250) # add acceleration
    robot.drive(170, 0)
    time.sleep(2.75 - 1.75)
    gyro_stop()
    # ev3.speaker.beep()
    # time.sleep(3)

    windthing()
    halftesla2()
    
def windthing(): #go to wind#
    gyro_straight(125, -100)
    gyroturno(-45+5-2)
    forward_dist(speed = 400, turn_rate = 1, distance = 300, t_prime=1) # slight turn right to not miss white line
    # ev3.speaker.beep(25)
    foundblack = False
    turn_right = False
    max_distance = robot.distance()
    while turn_right == False:
      robot.drive(100,0)
      if right_colorsensor.reflection() < 15:
        turn_right = True
        foundblack = True
      if robot.distance() > max_distance+125:
        turn_right = True
    # while get_color(right_colorsensor) != Color.WHITE:  
    #     robot.drive(50, 0)                              
    robot.stop()
    # ev3.speaker.beep(25) 
    # while get_color(right_colorsensor) != Color.WHITE:
    #     robot.drive(50, 0)
    # robot.stop()
    # ev3.speaker.beep(25) 
    if foundblack:
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
        time.sleep(0.1)
    robot.stop()

def halftesla2():
    # backup into car
    forward_dist(speed=-225, turn_rate=30, distance=-150, t_prime = 0.5)
    gyroturno(130)
    # ev3.speaker.beep()
    # time.sleep(3)
    robot.drive(speed=-125,turn_rate=0) 
    time.sleep(1)
    # forward_dist(70, 0, 15)
    # gyro_stop()
    # ev3.speaker.beep()
    back_motor.run_time(speed = -200, time=1000, wait=False)  # down
    time.sleep(0.75)
    gyro_stop()
    ev3.speaker.beep()
    # time.sleep(3)
    # Let car down
    forward_dist(speed=200, turn_rate=0, distance=140)
    # gyro_stop()
    back_motor.run_time(speed = 250, time = 900, wait=False) # up
    forward_dist(200, 0, 100)
    # push the car away, then run into Toy Factory
    forward_angle(speed=-100, turn_rate=90, angle=90)
    gyro_stop()
    # time.sleep(3)
    forward_dist(speed=200, turn_rate=0, distance=200, t_prime=0.5)
    robot.drive(speed=200, turn_rate=0)
    time.sleep(0.5)
    gyro_stop()
    # backup, turn, go home
    forward_dist(speed=-100, turn_rate=0, distance=-25)
    # gyroturno(angle=-225, rate_control=1.0, speed=50)
    gyroturno(angle=-225, rate_control=0.75, speed=0)
    forward_dist(speed=600, turn_rate=5, distance=500, t_prime=1.0)
    robot.drive(speed=800, turn_rate=0)
    time.sleep(0.75)
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

def test_departure():
    #from hybrid car
    for myspeed in [200, 250, 300, 350, 400, 450, 500]:
        back_motor.run_time(speed = -200, time=1000, wait=True)
        ev3.speaker.say(str(myspeed))
        forward_dist(speed=myspeed, turn_rate=0, distance=200)
        gyro_stop()
        back_motor.run_time(speed = 500, time = 900, wait=False)
        forward_dist(200, 0, 60)
        robot.stop()
        time.sleep(5)