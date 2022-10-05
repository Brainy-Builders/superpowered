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

def line_follow(length, speed, sensor, side, find_cross = False, Kp=0.15, Ki=0.0032, Kd=0.512):
  """length in mm, speed in mm/sec, sensor is which sensor is following, side is which side of the line your on, and find cross is weather to continue until cross is found"""
  # Kp, Ki, Kd = 0.2, 0.0006, 0.256  # original from Sophia
  Tp = speed * 35/250 # Target power - percentage of max power of motor (power is also known as 'duty cycle' ) 
  
  if sensor == 'right':
    follow_sensor = right_colorsensor
    detection_sensor = left_colorsensor
  else:
    follow_sensor = left_colorsensor
    detection_sensor = right_colorsensor

  if side.lower() == "left":
    side_mod = -1
  else:
    side_mod = 1

  target_distance = robot.distance() + length
  lastError = 0 # initialize
  integral = 0  # initialize
  robot.stop()  # deactivate DriveBase before powering wheels individually 
  stop = False 
  while (stop == False):
    error = follow_sensor.reflection()-50 # proportional
    if (abs(error) < 10):
      integral = 0
    else:
      integral = integral + error 
    derivative = error - lastError  

    correction = -(Kp*(error) + Ki*(integral) + Kd*derivative) * side_mod

    power_left = Tp + correction
    power_right = Tp - correction   
    left_wheel.dc(power_left) 
    right_wheel.dc(power_right) 
      
    lastError = error  
    if (robot.distance() <= target_distance): 
      stop = False
    else:
      if(not find_cross):
        stop = True
      else:
        if(detection_sensor.reflection()>80):
        # sensed_color = get_color(detection_sensor)
        # if (sensed_color == Color.WHITE): 
          # while sensed_color != Color.BLACK:          
          #   sensed_color = get_color(detection_sensor)
          stop = True
          
def old_line_follow(length, speed, sensor, side, find_cross = False, gain_mod=1.0):
    """length in mm, speed in mm/sec, sensor is which sensor is following, side is which side of the line your on, and find cross is weather to continue until cross is found"""
    Kp=  0.2
    Ki = 0.0006
    Kd = 0.256
    go_distance = robot.distance() + length
    # Calculate the light threshold. Choose values based on your measurements.
    threshold = (BLACK + WHITE) / 2
    ev3.screen.print("WHITE", WHITE)
    ev3.screen.print("BLACK", BLACK)
    DRIVE_SPEED = speed
    # For example, if the light value deviates from the threshold by 10, the robot
    # steers at 10*1.2 = 12 degrees per second.
    if side.lower() == "left":
        side_mod = -1
    else:
        side_mod = 1
    print(sensor, "r" in sensor.lower())
    if "r" in sensor.lower():
        follow_sensor = right_colorsensor
        detection_sensor = left_colorsensor
    else:
        follow_sensor = left_colorsensor 
        detection_sensor = right_colorsensor
    integral = [Ki]
    lastError = [0] # initialize
    def apply_corrections():

        error = follow_sensor.reflection()-50 # proportional
        # initialize
        if error == 0:
            integral[0] = 0
        else:
            integral[0] = integral[0] + error 
        derivative = error - lastError[0]

        correction = (Kp*(error) + Ki*(integral[0]) + Kd*derivative) * side_mod
        robot.drive(speed, correction*-1) 
        lastError[0] = error

    while robot.distance() < go_distance:
      apply_corrections()
    
    if find_cross == True:
        # while get_color(detection_sensor) != Color.WHITE:
        while detection_sensor.reflection() < 80:
          apply_corrections()
        # while get_color(detection_sensor) != Color.BLACK:
        #     apply_corrections()

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
    
