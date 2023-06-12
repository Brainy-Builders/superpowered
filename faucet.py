 #!/usr/bin/env pybricks-micropython
import math
import time

from pybricks.ev3devices import (ColorSensor, GyroSensor, InfraredSensor,
                                 Motor, TouchSensor, UltrasonicSensor)
from pybricks.hubs import EV3Brick
from pybricks.media.ev3dev import Font, ImageFile, SoundFile
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import DataLog, StopWatch, wait

from common import *
from gyrostraight import *
from linefollow import line_follow
from pidlinefollow import *

#
# Mission goals:
#   -> Drop one water unit into the water reservoir
#   -> Hang two units on the red hooks above the water reservoir
#   -> Collect energy unit from the hydroelectric dam
#

#
# This is the simple version if hanging the units becomes unreliable or something goes wrong:
# Drops three water units in the reservoir
# Grabs energy unit
#
def simple_water():
    gyro.reset_angle(angle=0)
    # Drives into the hydroelctric dam triggering the attachment to drop three units into the reservoir
    gyro_straight(distance=250, speed=450, t_prime=0.5)
    robot.drive(speed=300, turn_rate=0)
    time.sleep(seconds=1)
    # Drives back home and grabs the energy unit with rubber bands
    robot.drive(speed=-300, turn_rate=0)
    time.sleep(seconds=2)
    robot.stop()

#
# This is the advanced version to hang the units to get the maximum amount of points:
# Hangs two water units on red hooks
# Drop one water unit in the reservoir
# Grabs energy unit
#
def advance_water():
    gyro.reset_angle(angle=0)
    # Drives into the hydro electric dam triggering the attachment to drop one unit into the reservoir
    gyro_straight(distance=250, speed=450, t_prime=0.5)
    robot.drive(speed=300, turn_rate=0)
    time.sleep(1)
    gyro_stop()

    # Lowers the water units and positions them to be hanged
    main_motor.run_time(speed=-600, time=500, then=Stop.COAST, wait=True)
    main_motor.run_until_stalled(speed=-600, then=Stop.COAST, duty_limit=30)
    main_motor.reset_angle(angle=0)

    # Drives back a bit to hang the water units
    robot.drive(speed=-100, turn_rate=0)
    time.sleep(1.5)

    # Lifts the attachment back up and out of the way
    main_motor.run_target(speed=400, target_angle=360, then=Stop.HOLD, wait=False)

    # Drives home and grabs the energy unit with rubber bands
    robot.drive(speed=-400, turn_rate=0)
    time.sleep(1.2)
    robot.stop()