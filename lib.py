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
def get_color(reflectivity,green):
    if reflectivity <= 14.00:
            color = Color.BLACK
    if reflectivity >  14.00:
        if green <= 78.50:
                color = "Other"
        if green >  78.50:
                color = Color.WHITE
    return color
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
        my_data = ["LEFT", xyzabc[0], xyzabc[1], xyzabc[2], left_colorsensor.reflection(), left_colorsensor.ambient(), str(left_colorsensor.color()).split('.')[-1], truth, "\n"]
        my_line=[str(i) for i in my_data]
        my_line = ",".join(my_line)
        cs_data.write(my_line)
        cbazyx = right_colorsensor.rgb()
        my_data = ["RIGHT", cbazyx[0], cbazyx[1], cbazyx[2], right_colorsensor.reflection(), right_colorsensor.ambient(), str(right_colorsensor.color()).split('.')[-1], truth, "\n"]
        my_line=[str(i) for i in my_data]
        my_line = ",".join(my_line)
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
    pidline('left', 1000000000000000, 30, 0.45, 0.9, 1.1)
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
def view_color():
    ev3.screen.set_font(med_font)
    while Button.CENTER not in ev3.buttons.pressed():
        time.sleep(.5)
        ev3.screen.clear()
        r_color = get_color(right_colorsensor.reflection(),right_colorsensor.rgb()[2])
        l_color = get_color(left_colorsensor.reflection(),left_colorsensor.rgb()[2])
        ev3.screen.print("ml\n")
        ev3.screen.print("left color: {} right color: {}".format(l_color, r_color))
        ev3.screen.print("pybricks\n")
        ev3.screen.print("left color: {} right color: {}".format(left_colorsensor.color(),right_colorsensor.color()))
