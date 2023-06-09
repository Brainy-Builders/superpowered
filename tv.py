# Mission Goals
# - Flip Tv
# - Pump Windmill
# - Launch Hybrid Car
# - Collect Rechargable Unit

from pybricks.media.ev3dev import Font, ImageFile, SoundFile
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import DataLog, StopWatch, wait

from common import *
from gyrostraight import *
from gyroturno import *
from lib import *
from line_a_line import *
from linefollow import *
from pidlinefollow import *

def flip_tv():
    gyro.reset_angle(angle = 0) # reset angle to zero to validate home
    main_motor.run_time(speed=200, time=200, wait=False)
    back_motor.run_time(speed = 200, time=200, wait=False) # make sure UP
    gyro_straight(distance=300, speed=250) # add acceleration
    robot.drive(speed = 170, turn_rate = 0)
    time.sleep(1.2)
    gyro_stop()
    tv_windmill()
    halftesla2_and_rechargable()
    
def tv_windmill(): #go to wind#
    ev3.screen.clear()
    gyro_straight(distance = 35, speed =  -100)
    
    ev3.screen.print(gyroturn(angle = -43))  # gyroturn returns a angle that can be printed to the screen to debug
    forward_dist(speed = 400, turn_rate = 1, distance = 300, t_prime=1) # slight turn right to not miss white line

    foundblack = False
    turn_right = False
    max_distance = robot.distance()
    while turn_right == False: # little loop to look for when to turn right
      robot.drive(speed = 100,turn_rate = 0)
      if right_colorsensor.reflection() < 15:
        turn_right = True
        foundblack = True
      if robot.distance()  > max_distance + 85:
        turn_right = True
                           
    robot.stop()

    if foundblack:
        forward_dist(speed = 50, turn_rate = 0, distance = 20) # go slightly past white
    ev3.screen.print(gyro.angle())
    ev3.screen.print(gyroturn(angle = 45))
    gyro_stop()
    ev3.screen.print(gyro.angle())

    forward_dist(speed = 250, turn_rate = 0, distance = 85)
    
    #collecting the energy units

    for _ in range(3): # repeat to pump 3 times
        robot.drive(speed = 300, turn_rate = 0)
        time.sleep(0.85)
        robot.stop()
        time.sleep(0.2)
        robot.drive(speed = -70, turn_rate = 0)
        time.sleep(0.7)
        robot.stop()
        time.sleep(0.1)
    robot.stop()

def halftesla2_and_rechargable(): #I mean a hybrid car is half a tesla
    # backup into car
    forward_dist(speed=-100, turn_rate=30, distance=-70)
    gyroturn(angle = 128)
    robot.drive(speed=-125,turn_rate=0) 
    time.sleep(1)
    main_motor.run_time(speed = -300, time = 1000, wait=False)
    back_motor.run_time(speed = -200, time=1000, wait=False)  # down
    time.sleep(0.75)
    gyro_stop()
    ev3.speaker.beep()
    acceleration("distance", 50)
    forward_dist(speed=250 + 50, turn_rate=0, distance=120)
    back_motor.run_time(speed = 250, time = 900, wait=False) # up
    forward_dist(250 - 50, 10, 60)
    robot.drive(speed=800, turn_rate=40)
    time.sleep(2)
    gyro_stop()

 # _____  ______ ____  _    _  _____     
 #|  __ \|  ____|  _ \| |  | |/ ____|    
 #| |  | | |__  | |_) | |  | | |  __     
 #| |  | |  __| |  _ <| |  | | | |_ |    
 #| |__| | |____| |_) | |__| | |__| |    
 #|_____/|______|____/ \____/ \_____|  __
 #|  _ \|  ____| |    / __ \ \        / /
 #| |_) | |__  | |   | |  | \ \  /\  / / 
 #|  _ <|  __| | |   | |  | |\ \/  \/ /  
 #| |_) | |____| |___| |__| | \  /\  /   
 #|____/|______|______\____/   \/  \/    
                                        
def find_colors(color, sensor, speed=60):
    if sensor == "right":
        csensor = right_colorsensor
    elif sensor == "left":
        csensor = left_colorsensor

    if color == "white" or "WHITE":
        while get_color(csensor) != Color.WHITE:  
            robot.drive(speed = speed, turn_rate = 0)                              
        robot.stop()
    elif color == "black" or "BLACK":
        while get_color(csensor) != Color.BLACK:  
            robot.drive(speed = speed, turn_rate = 0)                              
        robot.stop()

def test_departure():
    #from hybrid car
    acceleration("distance", 50)
    for myspeed in [100, 200, 300, 400, 500]:
        ev3.speaker.say(str(myspeed))
        for _ in range(10):
            robot.drive(speed=-125,turn_rate=0) 
            time.sleep(1)
            main_motor.run_time(speed = -300, time = 1000, wait=False)
            back_motor.run_time(speed = -200, time=1000, wait=False)  # down
            time.sleep(0.75)
            gyro_stop()
            ev3.speaker.beep()
            acceleration("distance", 50)
            forward_dist(speed=myspeed, turn_rate=0, distance=120)
            back_motor.run_time(speed = 250, time = 900, wait=False) # up
            forward_dist(250 - 50, 10, 60)
            gyro_stop()
            ev3.speaker.beep()
            time.sleep(7)
