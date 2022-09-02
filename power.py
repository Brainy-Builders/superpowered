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
    robot.drive(200, 5)
    time.sleep(3)
    robot.stop()
    main_motor.run_time(-60*16, 2000)
    ev3.speaker.say('trey is cool')
    main_motor.run_time(90*16, 2000)
    robot.stop()
