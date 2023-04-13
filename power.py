from common import *
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font
from gyroturno import *
from pidlinefollow import *
from linefollow import *
from line_a_line import *
from gyrostraight import *
from lib import *

def power_generator():
    get_there_and_dispense()
    get_off_wall()
    get_home()

def get_there_and_dispense():
    forward_distance(400, 2, 450, 1)
    robot.drive(speed = 400, turn_rate = 5)
    time.sleep(.8)
    gyro_stop()
    #dispense units
    main_motor.run_time(speed=60*16, time=1700)
    main_motor.run_time(speed=-90*16, time=1800)

def get_off_wall():
    forward_distance(-250, 0, -70)
    gyroturn(angle=35, rate_control=.8, speed=-250)
    robot.reset()
    # time.sleep(.1)
    gyroturn(angle=-30, rate_control=1, speed=400, stop=False)

def get_home():
    dist = robot.distance()
    #forward_dist(speed=300, turn_rate=0, distance=470-dist) old code, saved in case of emergency
    forward_dist(speed=500, turn_rate=0, distance=430-dist)
    gyroturno(angle=30, rate_control=1, speed=400, stop=False)
    ev3.speaker.beep(duration=25)
    gyroturno(angle=0, rate_control=0.35, speed=400, stop=False)
    ev3.speaker.beep(duration=25)
    # forward_angle(speed=500, turn_rate=70, angle= 50)
    # ev3.speaker.beep()
    # forward_angle(speed=500, turn_rate=-30, angle=-45)
    # ev3.speaker.beep()
    # forward_distance(speed=500, turn_rate=-5, distance=300)
    #robot.drive(speed=350, turn_rate=-5) old code, saved in case of emergency
    robot.drive(speed=400, turn_rate=-15)
    time.sleep(0.3)
    gyro_stop()