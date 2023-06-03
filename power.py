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
# mission goals
#   collect 3 energy units from the powerplant
#   deliver 5 energy units (3 from powerplant + 2 from left home) to the right home
#   deliver oil truck to the right home

def power_generator():
    get_there_and_dispense()
    get_off_wall()
    get_home()

def get_there_and_dispense():
    # go to powerplant

    forward_distance(speed=400, turn_rate=2, distance=450, t_prime=1) #turn rate to keep on the wall
    robot.drive(speed = 400, turn_rate = 5)
    time.sleep(secs=.8)
    gyro_stop()

    # dispense units

    main_motor.run_time(speed=60*16, time=1700) #motor up
    main_motor.run_time(speed=-90*16, time=1800) #motor down

def get_off_wall():
    # back up and turn off the wall

    forward_distance(speed=-250, turnrate=0, distance=-70)
    gyroturn(angle=35, rate_control=.8, speed=-250)
    robot.reset() #reset to measure distance
    # time.sleep(.1)
    gyroturn(angle=-30, rate_control=1, speed=400, stop=False)

def get_home():

    # go to right home

    dist = robot.distance()
    #forward_dist(speed=300, turn_rate=0, distance=470-dist) old code, saved in case of emergency

    #go around the power plant
    forward_dist(speed=500, turn_rate=0, distance=430-dist)
    gyroturno(angle=30, rate_control=1, speed=400, stop=False)
    ev3.speaker.beep(duration=25)
    # go into home
    gyroturno(angle=0, rate_control=0.35, speed=400, stop=False)
    ev3.speaker.beep(duration=25)
    robot.drive(speed=400, turn_rate=-15)
    time.sleep(secs=0.3)
    gyro_stop()