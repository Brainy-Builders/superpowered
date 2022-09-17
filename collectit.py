from common import *
import linefollow
from gyroturno import *
from gyrostraight import *
from pidlinefollow import *
import os
def main():
        robot.reset()
        travel()
        
def travel():
    gyro.reset_angle(0)
    # main_motor.run_time(-200,1000,Stop.HOLD,False)
    forward_dist(100,0,180)
    ev3.speaker.beep(duration=25)
    while(get_color(left_colorsensor) != Color.BLACK):
        robot.drive(100,0)
        dist=robot.distance()
    robot.turn(30)
    robot.stop()
    linefollow.line_follow(length=650-dist,speed=125,sensor="left",side="right")
    ev3.speaker.beep(duration=25) # duration units [ms]
    while(get_color(right_colorsensor) != Color.BLACK):
        robot.drive(50,0)
    ev3.speaker.beep()
    robot.stop()
    forward_distance(70,0,25,0)
    robot.stop()
    gyroturno(90,.9)
    main_motor.run_time(-200,1000,Stop.HOLD,False)
    robot.stop()
    forward_distance(75,-10,150,1)
    ev3.speaker.beep()
    robot.stop()
    ev3.speaker.beep()
    linefollow.line_follow(100,100,"right","left")
    robot.stop()
    forward_dist(-100, 0, -85)
    robot.stop()
    back_motor.run_time(210,3700)
    linefollow.line_follow(100,100,"right","left")
    robot.stop()
    move_motor(100, 180)
    gyroturno(135)
    gyro_straight(200,200)
    robot.stop()