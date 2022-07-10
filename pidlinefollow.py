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
def pidline(sensor, distance, speed, porportional = 3):
   Td = distance # target distance 
   Tp = speed # Target power - percentage of max power of motor (power is also known as 'duty cycle' ) 
   
   Kp = porportional #  the Constant 'K' for the 'p' proportional controller
   if sensor == 'right':
       follow_sensor = right_colorsensor
   else:
       follow_sensor = left_colorsensor
   while (robot.distance() < Td):
      error = follow_sensor.brightness()-50 # proportional
      
      correction = Kp * error * -1   
      
      powerA = Tp + correction
      powerB = Tp - correction   
   
      left_wheel.dc(powerA) 
      right_wheel.dc(powerB) 
      
      print("error " + str(error) + "; correction " + str(correction) + "; powerA " + str(powerA) + "; powerB " + str(powerB))   
      wait(5)
   
   robot.stop()