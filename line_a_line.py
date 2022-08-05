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
from gyroturno import gyro_stop

AVG = load_avg()
def test_a_line():
    gyro = GyroSensor(Port.S3, direction=Direction.CLOCKWISE)
    gyro.reset_angle(0)
    ev3.screen.clear()
    time.sleep(1)
    while Button.CENTER not in ev3.buttons.pressed():
        ev3.screen.print(gyro.angle())
        time.sleep(0.25)
    if gyro.angle() < 0:
        while  left_colorsensor.reflection() > 10:
            robot.drive(70, 0)
        robot.stop()
        right_wheel.reset_angle(0)
        while right_colorsensor.reflection() > 10:
            right_wheel.run(50)
        robot.stop()
        ev3.screen.print("right wheel angle (record)", right_wheel.angle())
        left_wheel.reset_angle(0)
        while Button.CENTER not in ev3.buttons.pressed():
            time.sleep(0.1)
        ev3.screen.print("left wheel angle (record)", left_wheel.angle())
        time.sleep(30)
    elif gyro.angle() > 0:
        while  right_colorsensor.reflection() > 10:
            robot.drive(70, 0)
        robot.stop()
        left_wheel.reset_angle(0)
        while left_colorsensor.reflection() > 10:
            left_wheel.run(50)
        robot.stop()
        ev3.screen.print("left wheel angle (record)", left_wheel.angle())
        right_wheel.reset_angle(0)
        while Button.CENTER not in ev3.buttons.pressed():
            time.sleep(0.1)
        ev3.screen.print("right wheel angle (record)", right_wheel.angle())
        time.sleep(30)

def line_a_line(speed=70, speed_approach = 200,white=True):
    fraction = -45/75
    
    if(white):
        #while (right_colorsensor.reflection() <= (WHITE - 10)) and (left_colorsensor.reflection() <= (WHITE - 10)) and (right_colorsensor.rgb()[0] < AVG and left_colorsensor.rgb()[0] < AVG):
        while ((right_colorsensor.reflection() <= (WHITE - 10)) and (left_colorsensor.reflection() <= (WHITE - 10))):
            robot.drive(speed_approach, 0)
    
        # Don't overshoot the white
        robot.stop()
        left_wheel.hold()
        right_wheel.hold()
        time.sleep(0.25)

        # Now go find black
        robot.drive(speed, 0)
    else:
        robot.drive(speed_approach,0)

    while True:
        if (right_colorsensor.reflection() <= (BLACK + 10)) or (
            left_colorsensor.reflection() <= (BLACK + 10)):
            gyro_stop()
            break
    time.sleep(0.25)
    
    if right_colorsensor.reflection() <= (BLACK + 10):
        left_wheel.reset_angle(0)
        left_wheel.run(speed)
        while True:
            if left_colorsensor.reflection() <= (BLACK + 10):
                robot.stop()
                break
        leftrotation = left_wheel.angle()
        correctionr = fraction*leftrotation
        right_wheel.run_angle(speed, correctionr, wait=True)
    elif left_colorsensor.reflection() <= (BLACK + 10):
        right_wheel.reset_angle(0)
        right_wheel.run(speed)
        while True:
            if right_colorsensor.reflection() <= (BLACK + 10):
                robot.stop()
                break
            
        rightrotation = right_wheel.angle()
        correctionl = fraction*rightrotation
        left_wheel.run_angle(speed, correctionl, wait=True)
    gyro_stop()

def colorbeep(side="left", backwards=1):
    ev3.screen.print("cb2 w=", white)
    ev3.screen.print("cb2 b=", black)
    cb_sensor = right_colorsensor
    if side == "left":
        cb_sensor = left_colorsensor
    speed = 70 * backwards
    while cb_sensor.reflection() < (white-25):
        robot.drive(speed, 0)
    while cb_sensor.reflection() > (black+5):
        robot.drive(speed, 0)
    robot.stop()
