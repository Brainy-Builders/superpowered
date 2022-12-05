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
from gyroturno import *
# An example of this code is
# pidline(sensor='left', distance=600, speed=200, Kp=0.2, Ki=0.0006, Kd=0.256, find_cross = False)

# def pidline(sensor, distance, speed, Kp=0.2, Ki=0.0006, Kd=0.256, find_cross = False):
def pidlinefollow(length,  speed, sensor, side, find_cross = False, Kp=0, Ki=0, Kd=0):
  """length in mm, speed in mm/sec, sensor is which sensor is following, side is which side of the line your on, and find cross is weather to continue until cross is found"""
  # Kp, Ki, Kd = 0.2, 0.0006, 0.256  # original from Sophia
  
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
  stop = False 
  while (stop == False):
    error = follow_sensor.reflection()-50 # proportional
    if (abs(error) < 1):
      integral = 0
    else:
      integral = integral + error 

    correction = -(Kp*(error) + Ki*(integral)) * side_mod
    print("er ", error, ", cor ", correction,"\n")
    robot.drive(speed, correction)
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

def pidtest():
  for _ in [0.05,0.1, 0.2, 0.4, 0.8, 1.6, 3.2, 6.4, 12.8, 15, 30]:
    ev3.speaker.say(str(_))
    # pidlinefollow(length=1000,  speed=_, sensor='right', side='left', find_cross = False, Kp=0.2, Ki=0.0004, Kd=0)
    pidlinefollow(length=500, speed=100, sensor='left', side='right', find_cross = True, Kp=_, Ki=0, Kd=0)
    robot.stop()
    time.sleep(2)

