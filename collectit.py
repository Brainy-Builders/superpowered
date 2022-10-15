from common import *
import linefollow
from gyroturno import *
from gyrostraight import *
from pidlinefollow import *
import os

def coach():
    # go straight with acceleration
    forward_dist(speed=300,  turn_rate=0,  distance=300, t_prime=1.5)
    ev3.speaker.beep(50)
    # turn right then left
    forward_angle(speed=300,  turn_rate=45, angle=30)
    ev3.speaker.beep(50)
    forward_angle(speed=300,  turn_rate=-45, angle=-30)
    ev3.speaker.beep(50)
    # go straight to the end
    robot.drive(50,0)
    time.sleep(3)
    ev3.speaker.beep(50)
    # straight
    # forward_dist(speed=300,  turn_rate=0,  distance=150, t_prime=0)
    gyro_stop()
    time.sleep(5)

def main():
    robot.reset()
    robot.settings(straight_speed=300, straight_acceleration=300, turn_rate=180,  turn_acceleration=180)
    coach()
    main_motor.run_time(speed=500,time=800,then=Stop.HOLD,wait=False)
    get_to_cross()
    travel2()

def travel2():
    # go a little past the cross and turn
    forward_dist(speed=100,turn_rate=0,distance=70, t_prime=0)
    gyro_stop()
    smart_turn(left_wheel,right_colorsensor)

    # follow the line, then drop the energy harvester
    gyro_stop()
    linefollow.line_follow(length=170,speed=150,sensor="right",side="left")
    gyro_stop()
    back_motor.run_time(speed=650,time=1333,then=Stop.HOLD,wait=False)
    time.sleep(1)

    # keep following the line, get ready to high five
    linefollow.line_follow(length=240,speed=150,sensor="right",side="left")
    gyro_stop()
    main_motor.run_time(speed=500,time=1450,then=Stop.HOLD,wait=False) # put hand out
    gyro_straight(100,-70)
    gyro_stop()
    gyroturno(155)
    gyro_straight(distance=400,speed=200)
    gyro_stop()
    main_motor.run_time(speed=-200,time=1500,then=Stop.HOLD,wait=False)
    forward_angle(speed=200,turn_rate=90,angle=90)
    

    robot.drive(300,0)
    time.sleep(5)
    gyro_stop()

def get_to_cross():
    gyro.reset_angle(angle=0)
    # move forward and find the line
    gyro_straight(distance=180, speed=200) # use gyro at beginning 
    main_motor.run_angle(speed=-150,rotation_angle=115,then=Stop.HOLD,wait=False) # put hand out
    ev3.speaker.beep(duration=25)
    while(get_color(left_colorsensor) != Color.BLACK):
        robot.drive(75,0)

    # follow the line SMART distance
    dist=robot.distance()
    forward_angle(speed=150, turn_rate=90, angle=30) # turn but keep moving forward
    linefollow.line_follow(length=650-dist,speed=150,sensor="left",side="right")

    # get to the cross
    ev3.speaker.beep(duration=25) # duration units [ms]
    while(get_color(right_colorsensor) != Color.BLACK):
        robot.drive(100,0)
    ev3.speaker.beep(duration=25)    


