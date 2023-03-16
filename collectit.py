from common import *
import linefollow
from gyroturno import *
from gyrostraight import *
from pidlinefollow import *
import os


def gyro_test():
    
    robot.heading_control.limits(speed=570010,acceleration=10000000, actuation=100000)
    robot.distance_control.limits(speed=570010,acceleration=10000000, actuation=100000)
    for slay in range(1,30):
        gyro.reset_angle(0)
        old_angle = gyro.angle()
        old_time = time.time()
        right_wheel.run_angle(speed=slay*1000, rotation_angle=90, then=Stop.HOLD, wait=True)
        angle_diff = gyro.angle()-old_angle
        time_diff = time.time()-old_time
        print('speed =', slay*100, 'ANGLE =', angle_diff, 'time =', time_diff)
        right_wheel.run_angle(speed=slay*1000, rotation_angle=-90, then=Stop.HOLD, wait=True)
        

def main():
    robot.reset()
    robot.settings(straight_speed=300, straight_acceleration=300, turn_rate=180,  turn_acceleration=180)
    back_motor.run_time(speed=-500, time=800, wait=False) # put down
    main_motor.run_time(speed=-600, time=2200,wait=False) # retract
    get_to_cross()
    travel2()


def get_to_cross():
    gyro.reset_angle(angle=0)
    # move forward and find the line
    gyro_straight(distance=180, speed=250) # use gyro at beginning 
    while(get_color(left_colorsensor) != Color.BLACK):
        robot.drive(100,0)

    # follow the line SMART distance
    dist=robot.distance()
    forward_angle(speed=150, turn_rate=90, angle=30) # turn but keep moving forward
    linefollow.line_follow(440-30-10-dist, speed=130, sensor="left", side="right")
    back_motor.run_angle(600,240,then=Stop.HOLD,wait=False) # moving back motor up
    dist=robot.distance()
    # linefollow.line_follow(length=550-dist,speed=100,sensor="left",side="right")
    # get to the cross
    # ev3.speaker.beep(duration=25) # duration units [ms]
    gyro_straight(distance=200+10, speed=130, reset_angle=35 - 2.5)
    ev3.speaker.beep()
    while(get_color(right_colorsensor) != Color.BLACK):
        robot.drive(75,0)
    ev3.speaker.beep()
    while(get_color(right_colorsensor) != Color.WHITE):
        robot.drive(75,0)
    ev3.speaker.beep()
    gyro_stop()
    back_motor.run_angle(600,-80,then=Stop.HOLD,wait=False) # miss oil

def travel2():
    # go a little past the cross and turn
    gyro_straight(distance=50, speed=125)
    # forward_dist(speed=150,turn_rate=0,distance=50, t_prime=0)
    gyroturn(90)
    
    #smart_turn(left_wheel,right_colorsensor)

    # follow the line, then drop the energy harvester
    gyro_stop()
    # linefollow.line_follow(length=170+30,speed=60,sensor="right",side="left")
    # gyro_stop()
    back_motor.run_time(speed=1000,time=800,then=Stop.HOLD,wait=True)

    # keep following the line, get ready to high five
    linefollow.line_follow(length=240-30+20,speed=200,sensor="right",side="left", Ki=0.0000)
    gyro_stop()
    #TESTING CHANGE:
    # time.sleep(5000)
    #------------------
    main_motor.run_time(speed=1600,time=2000,then=Stop.HOLD,wait=True) # put hand out
    gyro_straight(distance=100,speed=-200, t_prime=0.5) # MAYBE BACKUP MORE THAN 100?
    gyro_stop()
    main_motor.run_time(speed=-600,time=2000,wait=False) # retract
    
    gyroturn(143+5)
    #CHANGE:
    gyro_straight(distance=350 - 100,speed=300, t_prime=1)
    # time.sleep(3)
    # main_motor.run_time(speed=-200,time=700,then=Stop.HOLD,wait=False)
    ev3.speaker.beep()
    forward_angle(speed=300,turn_rate=100,angle=77)
    #forward_angle(speed=200, turn_rate=60, angle = -15)0
    ev3.speaker.beep()
    gyro_straight(350 - 150, 400)
    gyroturn(270, 1.2, 350, False)
    #forward_angle(300, 100, 45)
    robot.drive(400, 0)
    time.sleep(1.00)
    gyro_stop()
