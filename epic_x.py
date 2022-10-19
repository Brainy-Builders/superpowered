from common import *
from gyroturno import gyroturno,gyro_stop
import time
def main():
    forward_distance(400,0,450,.5)
    robot.stop()
    forward_dist(300,35,450)
    forward_distance(300, 0, 100, 0)
    robot.stop()
    gyroturno(-25)
    gyro_stop()
    robot.drive(700,10)
    time.sleep(10)
    robot.stop()

