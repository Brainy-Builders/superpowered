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
from common import (
    tiny_font,
    big_font,
    ev3,
    left_wheel,
    right_wheel,
    robot,
    left_colorsensor,
    right_colorsensor,
    WHITE, BLACK
)

# An example of this code is
# pidline(sensor='left', distance=5000, speed=30, Kp=0.25, Ki=0.008, Kd=0.2)
def pidline(sensor, distance, speed, Kp, Ki, Kd):
   Td = distance # target distance
   Tp = speed # Target power - percentage of max power of motor (power is also known as 'duty cycle' ) 
   lastError = 0 # initialize
   integral = 0  # initialize
   if sensor == 'right':
      follow_sensor = right_colorsensor
   else:
      follow_sensor = left_colorsensor
   target_distance = robot.distance() + Td
   while (robot.distance() < target_distance):
     error = follow_sensor.reflection()-50 # proportional
     if (error == 0):
       integral = 0
     else:
       integral = integral + error 
     derivative = error - lastError  
     
     correction = -(Kp*(error) + Ki*(integral) + Kd*derivative)
     power_left = Tp + correction
     power_right = Tp - correction   
     
     left_wheel.dc(power_left) 
     right_wheel.dc(power_right) 
      
     lastError = error  
   
     print(str(Kp) + ", " + str(Kd) + ", " + str(Ki) + ", error " + str(error) + "; correction " + str(correction)  + "; integral " + str(integral)  + "; derivative " + str(derivative)+ "; power_left " + str(power_left) + "; power_right " + str(power_right))   
     wait(10)
   
robot.stop()
