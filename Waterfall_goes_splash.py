 #!/usr/bin/env pybricks-micropython
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
from linefollow import line_follow
from common import *
from pidlinefollow import *

def drive(tim, sped = 500, turn = 0):
    robot.drive(sped, turn)
    time.sleep(tim)

def waterfall():
    gyro.reset_angle(0)
    print("gyro: ", gyro.angle())
    ev3.screen.print(gyro.angle())
    drive(.23)
    gyroturno(45)
    drive(2)

def get_there(): # Get there without stopping until at the mission model
    forward_dist(speed = 100, turn_rate = 0, distance = 16)
    forward_dist(speed = 100, turn_rate = 45, distance = 100)
    robot.drive(200,0)
    time.sleep(1.5)
    robot.stop()

def hang_water():
    move_motor(700, -1900)
    robot.settings(200, 400, 180, 180)
    robot.straight(-65)
    move_motor(700, -1000)
    robot.straight(75)
    move_motor(700, 200)



def lift_and_collect():
    robot.straight(-40)
    main_motor.run_time(1000, 4000)

    

def get_home():
    robot.drive(-500, 0)
    time.sleep(2)
    robot.stop()

def test_stuff():
    robot.stop()
    ev3.screen.clear()
    ev3.screen.print("LEFT  => UP")
    ev3.screen.print("RIGHT => DOWN")
    ev3.screen.print("DOWN  => drive back")
    ev3.screen.print("UP    => drive fwd")
    while(not Button.CENTER in ev3.buttons.pressed()):
        if(Button.LEFT in ev3.buttons.pressed()):
            main_motor.run(speed=4000)
        elif(Button.RIGHT in ev3.buttons.pressed()):
            main_motor.run(speed=-4000)
        elif(Button.UP in ev3.buttons.pressed()):
            robot.drive(speed=200, turn_rate=0)
        elif(Button.DOWN in ev3.buttons.pressed()):
            robot.drive(speed=-200, turn_rate=0)
        else:
            robot.stop()
            main_motor.stop()

def waterfall2():
    test_stuff()
    move_motor(700, -4100)
    ev3.speaker.beep()
    time.sleep(2)
    get_there()
    hang_water()
    lift_and_collect()
    get_home()