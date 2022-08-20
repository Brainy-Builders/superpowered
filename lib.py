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
    # pidline(sensor='left', distance=1000, speed=30, Kp=0.45, Ki=0.9, Kd=1.1)
    ev3.speaker.beep()
    ev3.speaker.set_speech_options(voice='f2')
    # pidline(sensor='left', distance=400, speed=20, Kp=0.25, Ki=0.008, Kd=0.4, find_cross = True)
    for _ in range(5):
        ev3.speaker.say(str(_))
        # pidline(sensor='left', distance=600, speed=_, Kp=0.3, Ki=0.001, Kd=1.0, find_cross = True)
        forward_dist(100,0,180)
        ev3.speaker.beep(duration=25)
        while(get_color(left_colorsensor) != Color.BLACK):
            robot.drive(100,0)
        robot.turn(30)
        robot.stop()
        ev3.speaker.beep(duration=25)
        pidline(sensor='left', distance=350, speed=200, Kp=0.2, Ki=0.001, Kd=0.3, find_cross = False)
        ev3.speaker.beep(duration=25) # duration units [ms]
        while(get_color(right_colorsensor) != Color.WHITE):
            robot.drive(50,0)
        while(get_color(right_colorsensor) != Color.BLACK):
            robot.drive(50,0)
        gyro_stop()
    

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
    while Button.LEFT not in ev3.buttons.pressed():
        time.sleep(.5)
        ev3.screen.clear()
        r_color = get_color(right_colorsensor)
        l_color = get_color(left_colorsensor)
        ev3.screen.print("press LEFT to end")
        ev3.screen.print("ml:\n")
        ev3.screen.print("L clr: {}".format(l_color))
        ev3.screen.print("R clr: {}".format(r_color))
        ev3.screen.print("\npybricks:\n")
        ev3.screen.print("L clr: {}".format(left_colorsensor.color()))
        ev3.screen.print("R clr: {}".format(right_colorsensor.color()))

def test_follow():
    [ev3.speaker.beep() for i in range(3)]
    line_follow(1000,200,"left" , "right", True)
    robot.stop()
    left_wheel.brake()
    right_wheel.brake() 
def motor_test():
    