import time 
import math 
from common import *
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font
from gyroturno import *
from pidlinefollow import *
from linefollow import *
from line_a_line import *
def cs_data(truth):
    i = 0
    cs_data = open(r"cs_data_trey", "w")
    cs_data.write("sensor,red,green,blue,reflectivity,ambient,classification,truth\n")
    time.sleep(2)
    ev3.speaker.beep()
    while not Button.LEFT in ev3.buttons.pressed():
        ev3.screen.print(i)
        i += 1
        xyzabc = left_colorsensor.rgb()
        color = str(left_colorsensor.color()).rpartition('.')[2] # What the color senor thinks
        my_data = ("LEFT", xyzabc[0], xyzabc[1], xyzabc[2], left_colorsensor.reflection(), left_colorsensor.ambient(), color, truth, "\n")
        my_line = ",".join(map(str ,my_data,  ))
        cs_data.write(my_line)
        cbazyx = right_colorsensor.rgb()
        color = str(right_colorsensor.color()).rpartition('.')[2] # What the color senor thinks
        my_data = ("RIGHT", cbazyx[0], cbazyx[1], cbazyx[2], right_colorsensor.reflection(), right_colorsensor.ambient(), color, truth, "\n")
        my_line = ",".join(map(str ,my_data,  ))
        cs_data.write(my_line)
    cs_data.close()
def callum():
    print(robot.settings(600,300,100,100))
    #while True:
        #robot.straight(500)
        #forward_dist(speed = 300, turn_rate = 0, distance = 500)
        #gyro_stop()
        #time.sleep(5)
    #line_follow(0, 100, "left", "right", find_cross=True)
    #gyro_stop()
    line_a_line(speed=50, speed_approach = 200)
def turntest():
    robot.settings(turn_rate = 100)
    x = 0
    while True:
        robot.turn(-90)
        x += 1
        if x == 4:
            break
def pidtest():
    pidline('right', 1000000000000000, 80)
def gyrotest():
    gyro.reset_angle(0)
    gyroturno(90)
    gyroturno(180)
    gyroturno(270)
    gyroturno(0)
    robot.stop()
    gyroturno(-90)
    gyroturno(-180)
    gyroturno(-270)
    gyroturno(-0)
    robot.stop()