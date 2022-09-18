from common import *
import linefollow
from gyroturno import *
from gyrostraight import *
from pidlinefollow import *
import os
def main():
    robot.reset()
    robot.settings(straight_speed=300, straight_acceleration=300, turn_rate=180,  turn_acceleration=180)
    main_motor.run_time(speed=-300,time=800,then=Stop.HOLD,wait=False)
    get_to_cross()
    travel2()    

def travel2():
    forward_dist(speed=100,turn_rate=0,distance=70, t_prime=0)
    robot.stop()
    smart_turn(left_wheel,right_colorsensor)
    gyro_stop()
    linefollow.line_follow(length=170,speed=150,sensor="right",side="left")
    gyro_stop()
    back_motor.run_time(speed=600,time=1333,then=Stop.HOLD,wait=False)
    # forward_dist(speed=-100, turn_rate=0, distance=-150, t_prime=0)
    gyro_stop()
    ev3.speaker.say("ready to collect")
    time.sleep(3)

    linefollow.line_follow(length=300,speed=150,sensor="right",side="left")
    gyro_stop()
    main_motor.run_time(speed=300,time=600,then=Stop.HOLD,wait=False) # put hand out

    time.sleep(3)
    
    linefollow.line_follow(length=140,speed=100,sensor="right",side="left")
    robot.stop()
    gyroturno(135)
    gyro_straight(distance=200,speed=200)
    robot.stop()

def get_to_cross():
    gyro.reset_angle(angle=0)
    forward_dist(speed=200,turn_rate=0,distance=180, t_prime=0.75)
    main_motor.run_time(speed=300,time=600,then=Stop.HOLD,wait=False) # put hand out
    ev3.speaker.beep(duration=25)
    while(get_color(left_colorsensor) != Color.BLACK):
        robot.drive(100,0)
    dist=robot.distance()
    forward_angle(speed=200, turn_rate=90, angle=30) # turn but keep moving forward
    linefollow.line_follow(length=650-dist,speed=150,sensor="left",side="right")

    ev3.speaker.beep(duration=25) # duration units [ms]
    while(get_color(right_colorsensor) != Color.BLACK):
        robot.drive(100,0)
    ev3.speaker.beep(duration=25)    

def travel():
    forward_dist(speed=100,turn_rate=0,distance=25, t_prime=0)
    robot.stop()
    gyroturno(90,.9)
    robot.stop()
    forward_dist(speed=75,turn_rate=10,distance=150, t_prime=1)
    ev3.speaker.beep()
    robot.stop()
    ev3.speaker.beep()
    back_motor.run_time(speed=210,time=3650)
    linefollow.line_follow(length=140,speed=100,sensor="right",side="left")
    robot.stop()
    gyroturno(135)
    gyro_straight(distance=200,speed=200)
    robot.stop()

def smart_turn(wheel,sensor):
    if wheel==left_wheel:
        opp=right_wheel
    else:
        opp=left_wheel
    while get_color(sensor) != Color.WHITE:
        wheel.dc(20)
        opp.dc(-20)
    wheel.hold()