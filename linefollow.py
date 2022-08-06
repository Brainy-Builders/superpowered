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
def line_follow(length, speed, sensor, side, find_cross = False, gain_mod=1.0):
    go_distance = robot.distance() + length
    # Calculate the light threshold. Choose values based on your measurements.
    threshold = (BLACK + WHITE) / 2
    ev3.screen.print("WHITE", WHITE)
    ev3.screen.print("BLACK", BLACK)
    DRIVE_SPEED = speed
    # For example, if the light value deviates from the threshold by 10, the robot
    # steers at 10*1.2 = 12 degrees per second.
    if side.lower() == "left":
        PROPORTIONAL_GAIN = 0.35 * gain_mod
    else:
        PROPORTIONAL_GAIN = -0.35 * gain_mod

    if sensor == "right":
        follow_sensor = right_colorsensor
        detection_sensor = left_colorsensor
    else:
        follow_sensor = left_colorsensor 
        detection_sensor = right_colorsensor

    def apply_corrections():
        Td = length # target distance
        Tp = speed # Target power - percentage of max power of motor (power is also known as 'duty cycle' ) 
        
        Kp =  PROPORTIONAL_GAIN#  the Constant 'K' for the 'p' proportional controller
        
            # initialize
        Ki = 0.025 #  the Constanbricks.ev3devices import (
           #Motot 'K' for the 'i' integral term
        integral = Ki
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

    while robot.distance() < go_distance:
      apply_corrections()
    
      if find_cross == True:
        while detection_sensor.reflection() < (WHITE - 10):
            apply_corrections()
            #ev3.screen.print(detection_sensor.reflection())
        ev3.screen.print("found white")
        while detection_sensor.reflection() > (BLACK + 10):
            apply_corrections()
            #ev3.screen.print(detection_sensor.reflection())
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
    
def pidline(sensor, distance, speed, porportional = 0.35, integral = 0, derivitive = 0):
   Td = distance # target distance
   Tp = speed # Target power - percentage of max power of motor (power is also known as 'duty cycle' ) 
   
   Kp = porportional #  the Constant 'K' for the 'p' proportional controller
   
    # initialize
   Ki = 0 #  the Constant 'K' for the 'i' integral term
   
   lastError = 0 # initialize
   Kd = 0 #  the Constant 'K' for the 'd' derivative term
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
