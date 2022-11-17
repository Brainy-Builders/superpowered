from common import *
import linefollow
from gyroturno import *
from gyrostraight import *
from pidlinefollow import *
import os
def main():
    robot.reset()
    robot.settings(straight_speed=300, straight_acceleration=300, turn_rate=180,  turn_acceleration=180)
    #main_motor.run_time(speed=500,time=800,then=Stop.HOLD,wait=False)
    back_motor.run_time(speed=-500, time=800, wait=False)
    get_to_cross()
    travel2()

def travel2():
    # go a little past the cross and turn
    forward_dist(speed=200,turn_rate=0,distance=70, t_prime=0)
    gyro_stop()
    smart_turn(left_wheel,right_colorsensor)

    # follow the line, then drop the energy harvester
    gyro_stop()
    linefollow.line_follow(length=170,speed=175,sensor="right",side="left")
    gyro_stop()
    back_motor.run_time(speed=700,time=1133,then=Stop.HOLD,wait=False)
    time.sleep(1)

    # keep following the line, get ready to high five
    linefollow.line_follow(length=240,speed=200,sensor="right",side="left")
    gyro_stop()
    #TESTING CHANGE:
    # time.sleep(5000)
    #------------------
    main_motor.run_time(speed=600,time=2000,then=Stop.HOLD,wait=True) # put hand out
    gyro_straight(100,-100)
    main_motor.run_time(speed=-600,time=2000,then=Stop.HOLD,wait=False) # put hand out
    gyro_stop()
    gyroturno(143)
    gyro_straight(distance=350,speed=300, t_prime=1)
    # time.sleep(3)
    # main_motor.run_time(speed=-200,time=700,then=Stop.HOLD,wait=False)
    ev3.speaker.beep()
    forward_angle(speed=300,turn_rate=100,angle=96)
    #forward_angle(speed=200, turn_rate=60, angle = -15)
    ev3.speaker.beep()
    gyro_straight(500, 400)
    robot.drive(500, 0)
    time.sleep(0.75)
    gyro_stop()

def get_to_cross():
    gyro.reset_angle(angle=0)
    # move forward and find the line
    gyro_straight(distance=180, speed=250, t_prime=.6) # use gyro at beginning 
    # main_motor.run_angle(speed=-200,rotation_angle=115,then=Stop.HOLD,wait=False) # put hand out
    ev3.speaker.beep(duration=25)
    while(get_color(left_colorsensor) != Color.BLACK):
        robot.drive(100,0)

    # follow the line SMART distance
    dist=robot.distance()
    forward_angle(speed=150, turn_rate=90, angle=30) # turn but keep moving forward
    linefollow.line_follow(440-30-dist, speed=175, sensor="left", side="right")
    back_motor.run_angle(600,240,then=Stop.HOLD,wait=False) # moving back motor up
    dist=robot.distance()
    linefollow.line_follow(length=650-dist,speed=150,sensor="left",side="right")
    # get to the cross
    ev3.speaker.beep(duration=25) # duration units [ms]
    while(get_color(right_colorsensor) != Color.BLACK):
        robot.drive(75,0)
    back_motor.run_angle(600,-80,then=Stop.HOLD,wait=False)
    ev3.speaker.beep(duration=25)    

