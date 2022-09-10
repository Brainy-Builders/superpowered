from common import *
import linefollow
from gyroturno import *
from gyrostraight import *
def main():
        gyro.reset_angle(0)
        gyro_straight(400, 200)
        linefollow.line_follow(length=350,speed=150,sensor="left",side="left",find_cross=True)
        forward_dist(200, 0, 200)
        gyroturno(90)
        forward_dist(100, 0, 50)
        move_motor(300, 700)
        # linefollow.line_follow(length=450,speed=150,sensor="right",side="left")
        linefollow.line_follow(200, 200, "right", "left")
        robot.stop()
        robot.turn(90)
        