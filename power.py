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

def dispense():
    robot.drive(256, 5)
    time.sleep(2.5)
    robot.stop()
    main_motor.run_time(-60*16, 1350)
    main_motor.run_time(90*16, 2000)
    forward_dist(-300,0,-640)
    robot.stop()
    
