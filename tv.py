from common import *
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font
from gyroturno import *
from pidlinefollow import *
from linefollow import *
from line_a_line import *
import gyrostraight
def flip_tv():
    ev3.speaker.beep()
    forward_dist(300, 0, 370)
    #robot.settings(straight_acc = )
    robot.drive(200, 0)
    time.sleep(2)
    robot.stop()

def windthing():
    gyro.reset_angle(0)
    