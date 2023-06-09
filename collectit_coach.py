from common import *
import linefollow
from gyroturno import *
from gyrostraight import *
from pidlinefollow import *
import os

#
# Mission goals:
#   -> Collect all looped water units
#   -> Collect three energy units from solar farm
#   -> Raise smart grid
#
def main():
    position_attachments()
    get_to_energy_storage()
    get_energy()
    push_hand_go_back()
    go_home()

#
# Put down front attachment (to get looped water unit)
# Put up back attachment all the way
#
def position_attachments():
    robot.reset()
    robot.settings(straight_speed=300, straight_acceleration=300, turn_rate=180,  turn_acceleration=180)
    back_motor.run_time(speed=-500, time=800, wait=False) # put down front
    main_motor.run_time(speed=-600, time=2200,wait=False) # put up back

# 
# Follow the line past hydro
# Use gyro straight to east/west line
#
def get_to_energy_storage():
    # Find the black part of the line
    gyro.reset_angle(angle=0)
    gyro_straight(distance=180, speed=250) 
    while(get_color(left_colorsensor) != Color.BLACK):
        robot.drive(100,0)

    # turn and catch the line
    # follow the line SMART distance
    dist=robot.distance()
    forward_angle(speed=150, turn_rate=90, angle=30) # turn but keep moving forward
    linefollow.line_follow(length=380-dist, speed=130, sensor="left", side="right")
    back_motor.run_angle(speed=600,rotation_angle=240,then=Stop.HOLD,wait=False) # lift up water unit

    # get to the east/west line
    gyro_straight(distance=210, speed=130, reset_angle=32.5)
    ev3.speaker.beep()
    dist = robot.distance()
    pastdistance = False 
    maxdistance = int(dist+120)
    while pastdistance==False:
        robot.drive(speed=75,turn_rate=0)
        if (get_color(right_colorsensor) == Color.BLACK):
            ev3.speaker.beep()
            forward_distance(speed=75, turn_rate=0, distance=75)
            pastdistance = True
        if robot.distance() >= maxdistance:
            pastdistance = True
    gyro_stop()

    # put down energy collector and turn to follow the line
    back_motor.run_angle(speed=600,rotation_angle=-80,then=Stop.HOLD,wait=False)
    gyroturn(angle=90)
    gyro_stop()
    back_motor.run_time(speed=1000,time=800,then=Stop.HOLD,wait=True)

def get_energy():
    # keep following the line, get ready to high five
    linefollow.line_follow(length=240-30+20,speed=200,sensor="right",side="left", Ki=0.0000)
    gyro_stop()

#
# push hand (smart connect) out
# backup hopefully straight
# 
def push_hand_go_back():
    main_motor.run_time(speed=1600,time=2000,then=Stop.HOLD,wait=True) # put hand out
    gyro_straight(distance=83,speed=-200)
    gyro_stop()
    main_motor.run_time(speed=-600,time=2000,wait=False) # retract

#
# Go home around the waterfall
# Collect the two looped water units
# Three steps (turn, straight, turn, straight, turn, straight)
# 
def go_home():
    # turn carefully
    acceleration("heading", 20)
    gyroturn(148)
    acceleration("heading", 30)
    # straight past waterfall
    gyro_straight(distance=250,speed=300, t_prime=1)
    ev3.speaker.beep()
    forward_angle(speed=300,turn_rate=90,angle=77)    # turn
    ev3.speaker.beep()
    gyro_straight(distance=350 - 250, speed=400)    # straight
    gyroturn(angle=270, rate_control=1.2, speed=350, stop=False)    # turn
    # finally get back home
    robot.drive(speed=400, turn_rate=0)
    time.sleep(1.00)
    gyro_stop()