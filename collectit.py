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
    # go a little past the cross and turn
    forward_dist(speed=100,turn_rate=0,distance=70, t_prime=0)
    robot.stop()
    smart_turn(left_wheel,right_colorsensor)

    # follow the line, then drop the energy harvester
    gyro_stop()
    linefollow.line_follow(length=170,speed=150,sensor="right",side="left")
    gyro_stop()
    back_motor.run_time(speed=600,time=1333,then=Stop.HOLD,wait=False)

    # forward_dist(speed=-100, turn_rate=0, distance=-150, t_prime=0)
    ev3.speaker.say("ready to collect")
    time.sleep(3)

    # keep following the line, get ready to high five
    linefollow.line_follow(length=200,speed=150,sensor="right",side="left")
    gyro_stop()
    ev3.speaker.say("ready to high five")
    main_motor.run_time(speed=300,time=1000,then=Stop.HOLD,wait=False) # put hand out

    time.sleep(3)
    
    gyroturno(135)
    gyro_straight(distance=200,speed=200)
    robot.stop()

def get_to_cross():
    gyro.reset_angle(angle=0)
    # move forward and find the line
    gyro_straight(distance=180, speed=200) # use gyro at beginning 
    main_motor.run_time(speed=150,time=1000,then=Stop.HOLD,wait=False) # put hand out
    ev3.speaker.beep(duration=25)
    while(get_color(left_colorsensor) != Color.BLACK):
        robot.drive(100,0)

    # follow the line SMART distance
    dist=robot.distance()
    forward_angle(speed=150, turn_rate=90, angle=30) # turn but keep moving forward
    linefollow.line_follow(length=650-dist,speed=150,sensor="left",side="right")

    # get to the cross
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
    while sensor.reflection() < 80:
    # while get_color(sensor) != Color.WHITE:
        wheel.dc(20)
        opp.dc(-20)
    wheel.hold()