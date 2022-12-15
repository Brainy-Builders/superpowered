import time 
import math 
from common import *
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font
from gyroturno import *
from gyrostraight import *
from pidlinefollow import *
from linefollow import *
from line_a_line import *
import threading
import logging

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
    ev3.speaker.say("starting test")
    for _ in [0.00001,0.00002,0.00004,0.00008,0.00016, 0.00032]:
        ev3.speaker.say(str(_))
        line_follow(700,125,"left","right",Kp=0.6,Ki=_,Kd=0)
        gyro_stop()

def gyrotest():
    gyro.reset_angle(0)

    # test_gyro_turno=False
    # if (test_gyro_turno):
    gyroturno(90)
    time.sleep(2)
    ev3.speaker.beep()
    gyroturno(180)
    ev3.speaker.beep()
    time.sleep(2)
    gyroturno(270)
    ev3.speaker.beep()
    time.sleep(2)
    gyroturno(0)
    ev3.speaker.beep()
    time.sleep(2)
    robot.stop()

    gyroturno(-90)
    ev3.speaker.beep()
    time.sleep(2)
    gyroturno(-180)
    ev3.speaker.beep()
    time.sleep(2)
    gyroturno(-270)
    ev3.speaker.beep()
    time.sleep(2)
    gyroturno(-0)
    robot.stop()
    # else:

    #     gyro_straight(distance=1000, speed=-100, reset_angle=45)
    #     ev3.speaker.beep()
    #     robot.stop()
def view_color():
    ev3.screen.set_font(med_font)
    while Button.LEFT not in ev3.buttons.pressed():
        time.sleep(.5)
        ev3.screen.clear()
        r_color = get_color(right_colorsensor)
        l_color = get_color(left_colorsensor)
        r_raw = get_color(right_colorsensor, raw=True)
        l_raw = get_color(left_colorsensor, raw=True)
        ev3.screen.print("press LEFT to end")
        ev3.screen.print("ml:")
        ev3.screen.print("L clr: {}".format(l_color))
        ev3.screen.print(" raw:", l_raw)
        ev3.screen.print("R clr: {}".format(r_color))
        ev3.screen.print(" raw:", r_raw)
        ev3.screen.print("pb L clr: {}".format(left_colorsensor.color()))
        ev3.screen.print("pb R clr: {}".format(right_colorsensor.color()))
        time.sleep(1)
def test_follow():
    
    line_follow(1000,200,"left" , "right", True)

def motor_test():
    
    time.sleep(5)
    def log():
        
        t=time.time()
        print(t,t+7)
        while time.time() < t+10.00001:
            print(str(time.time()-t)+", "+str(left_wheel.speed()))
        
    x=threading.Thread(target=log)
    x.start()
    left_wheel.run(650)
    time.sleep(1)
    left_wheel.stop()
    time.sleep(.5)
    left_wheel.run(650)
    time.sleep(1)
    left_wheel.brake()
    time.sleep(.5)
    left_wheel.run(650)
    time.sleep(1)
    left_wheel.hold()
    time.sleep(.5)
    ev3.speaker.beep(1000,900)
