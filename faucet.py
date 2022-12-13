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

# Chloe - please also try the "get_there()" routine below to compare.
def get_to_there():
    # forward_angle(300, 90, 45)
    gyro.reset_angle(0)
    # gyroturno(50, speed=150) 
    # gyro_stop()
    # time.sleep(2.5)
    gyro_straight(250, 450, t_prime=0.5)
    robot.drive(300, 0)
    time.sleep(1)
    robot.drive(-300, 0)
    time.sleep(2)
    robot.stop()

def hang_water_units():
    gyro.reset_angle(0)
    gyro_straight(250, 450, t_prime=0.5)
    robot.drive(300, 0)
    time.sleep(1)
    gyro_stop()
    main_motor.run_until_stalled(-600, then=Stop.COAST, duty_limit=30)
    robot.drive(-100, 0)
    time.sleep(1.5)
    main_motor.run_target(400, 360, then=Stop.HOLD, wait=False)
    robot.drive(-400, 0)
    time.sleep(1.2)
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
