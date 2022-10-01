from common import *
from gyroturno import gyroturno,gyro_stop
import time
def main():
    forward_distance(400,0,450,.5)
    robot.stop()
    forward_dist(300,35,410)
    robot.stop()
    gyroturno(-20)
    gyro_stop()
    robot.drive(700,3)
    time.sleep(10)
    robot.stop()

