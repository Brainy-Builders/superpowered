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
# line_follow(followlength=200, followspeed=100, "left")
# followlength=0 goes until an intersection
def pidline(sensor, distance, speed, porportional = 0.6):
   Td = distance # target distance
   Tp = speed # Target power - percentage of max power of motor (power is also known as 'duty cycle' ) 
   
   Kp = porportional #  the Constant 'K' for the 'p' proportional controller
   
   integral = 0 # initialize
   Ki = 0.025 #  the Constant 'K' for the 'i' integral term
   
   derivative = 0 # initialize
   lastError = 0 # initialize
   Kd = 3 #  the Constant 'K' for the 'd' derivative term
   if sensor == 'right':
      follow_sensor = right_colorsensor
   else:
      follow_sensor = left_colorsensor
   while (robot.distance() < Td):
     error = follow_sensor.reflection()-50 # proportional
     if (error == 0):
      integral = 0
     else:
       integral = integral + error 
     derivative = error - lastError  
   
     correction = (Kp*(error) + Ki*(integral) + + Kd*derivative) * -1
   
     power_left = Tp + correction
     power_right = Tp - correction   
     
     left_wheel.dc(power_left) 
     right_wheel.dc(power_right) 
      
     lastError = error  
   
     print("error " + str(error) + "; correction " + str(correction)  + "; integral " + str(integral)  + "; derivative " + str(derivative)+ "; power_left " + str(power_left) + "; power_right " + str(power_right))   
     wait(10)
   
robot.stop()
