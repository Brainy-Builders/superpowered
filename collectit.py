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
    linefollow.line_follow(440-30-30-dist, speed=130, sensor="left", side="right")
    back_motor.run_angle(600,240,then=Stop.HOLD,wait=False) # moving back motor up
    dist=robot.distance()
    # get to the cross
    gyro_straight(distance=200+10, speed=130, reset_angle=35 - 2.5)
    ev3.speaker.beep()
    dist = robot.distance()
    pastdistance = False 
    maxdistance = int(dist+120)
    while pastdistance==False:
        robot.drive(75,0)
        if (get_color(right_colorsensor) == Color.BLACK):
            ev3.speaker.beep()
            forward_distance(75, 0, 75)
            pastdistance = True
        if robot.distance() >= maxdistance:
            pastdistance = True
    gyro_stop()
    back_motor.run_angle(600,-80,then=Stop.HOLD,wait=False) # miss oil

def travel2():
    # go a little past the cross and turn
    gyroturn(90)
    # follow the line, then drop the energy harvester
    gyro_stop()
    back_motor.run_time(speed=1000,time=800,then=Stop.HOLD,wait=True)

    # keep following the line, get ready to high five
    linefollow.line_follow(length=240-30+20,speed=200,sensor="right",side="left", Ki=0.0000)
    gyro_stop()
    main_motor.run_time(speed=1600,time=2000,then=Stop.HOLD,wait=True) # put hand out
    gyro_straight(distance=83,speed=-200) # MAYBE BACKUP MORE THAN 100?
    gyro_stop()
    main_motor.run_time(speed=-600,time=2000,wait=False) # retract
    acceleration("heading", 20)
    gyroturn(143+5)
    acceleration("heading", 30)
    #CHANGE:
    # Turning around water and heading home
    gyro_straight(distance=350 - 100,speed=300, t_prime=1)
    ev3.speaker.beep()
    forward_angle(speed=300,turn_rate=90,angle=77)
    ev3.speaker.beep()
    gyro_straight(distance=350 - 250, speed=400)
    gyroturn(angle=270, rate_control=1.2, speed=350, stop=False)
    robot.drive(400, 0)
    time.sleep(1.00)
    gyro_stop()