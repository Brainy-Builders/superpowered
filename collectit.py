from common import *
import linefollow
from gyroturno import *
from gyrostraight import *
from pidlinefollow import *
import os
def main():
        travel()
        
def travel():
    gyro.reset_angle(0)
    main_motor.run_time(-200,1000,Stop.HOLD,False)
    forward_dist(100,0,180)
    ev3.speaker.beep(duration=25)
    while(get_color(left_colorsensor) != Color.BLACK):
        robot.drive(100,0)
    robot.turn(30)
    robot.stop()
    linefollow.line_follow(length=350,speed=125,sensor="left",side="right")
    ev3.speaker.beep(duration=25) # duration units [ms]
    while(get_color(right_colorsensor) != Color.WHITE):
        robot.drive(50,0)
    ev3.speaker.beep()
    while(get_color(right_colorsensor) != Color.BLACK):
        robot.drive(50,0)
    ev3.speaker.beep()
    robot.stop()
    forward_distance(70,0,50,0)
    robot.stop()
    gyroturno(90,.9)
    forward_distance(75,0,150,1)
    ev3.speaker.beep()
    robot.stop()
    ev3.speaker.beep()
    back_motor.run_time(210,3650)
    gyro_straight(140,100)
    robot.stop()
    gyroturno(135)
    gyro_straight(200,200)
    robot.stop()