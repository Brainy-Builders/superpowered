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

# Miles -> Break this up into at least three sub-functions
#       -> Also the forward_angle isn't working reliably getting off the wall.abs(x)
#       -> Think of how to make sure the target angles are achieved even when "skidding" 
#       -> against the wall. I fixed it with gyroturno.

def power_generator():
    get_there_and_dispense()
    get_off_wall()
    get_home()

def get_there_and_dispense():
    forward_distance(400, 5, 450, 1)
    robot.drive(speed = 400, turn_rate = 5)
    time.sleep(.8)
    gyro_stop()
    #dispense units
    main_motor.run_time(-60*16, 1350)
    main_motor.run_time(90*16, 2000)

def get_off_wall():
    gyroturno(35, .8, -200)
    time.sleep(.1)
    gyroturno(-30, 1, 300)



def get_home():
    forward_dist(500, 0, 200, t_prime=1)
    forward_angle(speed=500, turn_rate=70, angle= 50)
    ev3.speaker.beep()
    forward_angle(speed=500, turn_rate=-30, angle=-45)
    ev3.speaker.beep()
    forward_distance(speed=900, turn_rate=0, distance=300)
    robot.stop()