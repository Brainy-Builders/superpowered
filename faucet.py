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
from gyrostraight import *

def coach():
    # def pidline(sensor, distance, speed, Kp=0.2, Ki=0.0006, Kd=0.256, find_cross = False):

    for _ in [0.000, 0.0001, 0.0002, 0.0004, 0.0008, 0.0016, 0.0032]:
        ev3.speaker.say(str(_))
        line_follow(length=350,speed=125,sensor="left",side="right", find_cross="True", Kp=0.15, Ki=0.0008, Kd=0.16)
        gyro_stop()
        time.sleep(2)

def get_to_there():
    # forward_angle(300, 90, 45)
    gyro.reset_angle(0)
    gyroturno(45, speed=200)
    robot.stop()
    # time.sleep(2)
    gyro_straight(250, 200)
    robot.drive(100, 0)
    time.sleep(1)
    robot.drive(-300, 0)
    time.sleep(2)
    robot.stop()


# def waterfall():
#     gyro.reset_angle(0)
#     print("gyro: ", gyro.angle())
#     ev3.screen.print(gyro.angle())
#     drive(.23)
#     gyroturno(45)
#     drive(2)

# def get_there(): # Get there without stopping until at the mission model
#     forward_dist(speed = 100, turn_rate = 0, distance = 19)
#     # forward_dist(speed = 100, turn_rate = 45, distance = 100)
#     forward_angle(100, 45, 45)
#     robot.drive(200,0)
#     time.sleep(1.5)
#     robot.stop()

# def test_stuff():
#     robot.stop()
#     ev3.screen.clear()
#     ev3.screen.print("LEFT  => UP")
#     ev3.screen.print("RIGHT => DOWN")
#     ev3.screen.print("DOWN  => drive back")
#     ev3.screen.print("UP    => drive fwd")
#     while(not Button.CENTER in ev3.buttons.pressed()):
#         if(Button.LEFT in ev3.buttons.pressed()):
#             main_motor.run(speed=4000)
#         elif(Button.RIGHT in ev3.buttons.pressed()):
#             main_motor.run(speed=-4000)
#         elif(Button.UP in ev3.buttons.pressed()):
#             robot.drive(speed=100, turn_rate=0)
#         elif(Button.DOWN in ev3.buttons.pressed()):
#             robot.drive(speed=-100, turn_rate=0)
#         else:
#             robot.stop()
#             main_motor.stop()
