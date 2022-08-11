#
# Want to follow a line? Import this routine and use it!
# line_follow(followlength, followspeed)
#
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
from common import *

# An example of this code is
# line_follow(followlength=200, followspeed=100, "left")
# followlength=0 goes until an intersection
def line_follow(length, speed, sensor, side, find_cross = False):
    Kp = 0.25  #  the Constant 'K' for the 'p' proportional controller
    Kd = 0.2   #  the Constant 'K' for the 'd' derivative term
    Ki = 0.008 #  the Constand 'K' for the 'i' integratl term

    # Work out how far to go first
    go_distance = robot.distance() + length
    # Calculate the light threshold. Choose values based on your measurements.
    ev3.screen.print("WHITE", WHITE)
    ev3.screen.print("BLACK", BLACK)
    threshold = (BLACK + WHITE) / 2

    DRIVE_SPEED = speed*30/200
    
    # Configure side_gain based on side of line to follow
    if side.lower() == "left":
        side_gain = +1
    else:
        side_gain = -1
    
    print(sensor, "r" in sensor.lower())
    
    if "r" in sensor.lower():
        follow_sensor = right_colorsensor
        detection_sensor = left_colorsensor
    else:
        follow_sensor = left_colorsensor 
        detection_sensor = right_colorsensor
    
    integral = [0]  # initialize
    lastError = [0] # initialize
    
    def apply_corrections():
        error = follow_sensor.reflection()-threshold
        # initialize
        Tp = DRIVE_SPEED
        if (error == 0):
            integral[0] = 0
        else:
            integral[0] = integral[0] + error 
        derivative = error - lastError[0]
        
        correction = (Kp*(error) + Ki*(integral[0]) + Kd*derivative) * side_gain
        power_left = Tp + correction
        power_right = Tp - correction   
        left_wheel.dc(power_left) 
        right_wheel.dc(power_right) 
        
        lastError[0] = error  
        # print(str(Kp) + "," + str(Kd) + "," + str(Ki) + "," + "error " + str(error) + "; correction " + str(correction)  + "; integral " + str(integral)  + "; derivative " + str(derivative))   

    while robot.distance() < go_distance:
      apply_corrections()
    
    if find_cross == True:
        while get_color(detection_sensor) != Color.WHITE:
            apply_corrections()
        ev3.screen.print("found white")
        while get_color(detection_sensor) != Color.BLACK:
            apply_corrections()
        ev3.screen.print("found black")        
            
def test1():
    time.sleep(5)
    speed = 400
    gain = .2
    for i in range(10):
        print(gain, speed)
        ev3.screen.print(speed," , ", gain)
        line_follow(600, speed, "right", gain, switch_sensor = True)
        robot.stop()
        gain = gain * 1.5
        time.sleep(5)

def test2():
    new_line_follow(200, 150, sensor="left", side="right", find_cross =  True)
    robot.stop()
    ev3.screen.print("Done!!!!")
    time.sleep(5)
    
