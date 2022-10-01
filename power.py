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
    forward_distance(400, 5, 450, 1)
    robot.drive(speed = 400, turn_rate = 5)
    time.sleep(.8)
    robot.stop()
    main_motor.run_time(-60*16, 1350)
    main_motor.run_time(90*16, 2000)
    forward_angle(speed=-200, turn_rate=40, angle=45)
    forward_angle(speed=200, turn_rate= -70, angle=-70)
    ev3.speaker.beep()
    forward_angle(speed=300, turn_rate=50, angle= 90)
    ev3.speaker.beep()
    forward_angle(speed=300, turn_rate=-20, angle=-20)
    ev3.speaker.beep()
    forward_distance(speed=300, turn_rate=0, distance=300)
    gyro_stop()
    time.sleep(1000000)

    #forward_dist(speed = -300, turn_rate = 20, distance = -200, t_prime=1)
    forward_dist(speed = 100, turn_rate = -70, distance = 100, t_prime=1)
    forward_dist(speed= 100, turn_rate= 0, distance=90)
    ev3.speaker.beep()
    forward_distance(speed=100, turn_rate=25, distance=150, t_prime=0)
    #ev3.speaker.beep()
    forward_distance(speed=100, turn_rate= 0, distance=250, t_prime=0)
    #Get home
    forward_distance(speed=100, turn_rate=25, distance=150, t_prime=0)
    forward_distance(speed=100, turn_rate= 0, distance=10, t_prime=0)
    ev3.speaker.beep()
    forward_dist(speed = 100, turn_rate = -20, distance = 50, t_prime=0)
    ev3.speaker.beep()
    forward_dist(speed=100, turn_rate=0, distance=200)

    robot.stop()

