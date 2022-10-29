from common import *
from gyroturno import gyroturno,gyro_stop
import time
def main():
    forward_distance(400,0,350,.5)
    # robot.stop()
    forward_dist(300,27,500)
    forward_angle(300, -180, -60)
    # ev3.speaker.beep()
    # robot.stop()
    # gyroturno(-20)
    forward_distance(700, 3, 1000, t_prime=1)
    # gyro_stop()
    # robot.drive(700,3)
    # time.sleep(10)
    robot.stop()

