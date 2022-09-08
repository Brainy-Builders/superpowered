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

<<<<<<< HEAD
def pidline(sensor, distance, speed, Kp=0.2, Ki=0.0006, Kd=0.256, find_cross = False):
=======
def pidline(sensor, distance, speed, Kp=0.2, Ki=0.0006, Kd=0.256, find_cross= False):
>>>>>>> a86b63a4f44befb8a8051a8e965acec55885157b
  Td = distance # target distance
  Tp_pct = speed # Target power - percentage of max power of motor (power is also known as 'duty cycle' ) 
  Tp = Tp_pct * 35/250 # Scale to approximate mm/s units
  lastError = 0 # initialize
  integral = 0  # initialize
  if sensor == 'right':
    follow_sensor = right_colorsensor
    detection_sensor = left_colorsensor
  else:
    follow_sensor = left_colorsensor
    detection_sensor = right_colorsensor
  stop = False 
  target_distance = robot.distance() + Td
  robot.stop()
  while (stop == False):
    error = follow_sensor.reflection()-50 # proportional
    # if (error == 0):
    #   integral = 0
    # else:
    integral = integral + error # maybe limit the integral?
    derivative = error - lastError  

    correction = -(Kp*(error) + Ki*(integral) + Kd*derivative)

    power_left = Tp + correction
    power_right = Tp - correction   

    left_wheel.dc(power_left) 
    right_wheel.dc(power_right) 
      
    lastError = error  
    rd = robot.distance()
    if (rd <= target_distance): 
      stop = False
    else:
      if(not find_cross):
        stop = True
        print("stop without finding cross")
      else:
        # sensed_color = get_color(detection_sensor)
        sensed_color = get_color(detection_sensor)
        if (sensed_color == Color.WHITE): 
          while sensed_color != Color.BLACK:          
            sensed_color = get_color(detection_sensor)
          stop = True
    # print(str(Kp) + ", " + str(Kd) + ", " + str(Ki) + ", error " + str(error) + "; correction " + str(correction)  +"("+ str(-Kp*error)+","+str(-Ki*integral)+","+str(-Kd*derivative)+ ") ; integral " + str(integral)  + "; derivative " + str(derivative)+ "; power_left " + str(power_left) + "; power_right " + str(power_right))   
