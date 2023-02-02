import time 
import math 
from common import *
from pybricks.iodevices import Ev3devSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font
from gyroturno import *
from gyrostraight import *
from pidlinefollow import *
from linefollow import *
from line_a_line import *
import threading
import logging

def cs_data(truth):
    i = 0
    cs_data = open(r"cs_data_trey", "w")
    cs_data.write("sensor,red,green,blue,reflectivity,ambient,classification,truth\n")
    time.sleep(2)
    ev3.speaker.beep()
    while not Button.LEFT in ev3.buttons.pressed():
        ev3.screen.print(i)
        i += 1
        xyzabc = left_colorsensor.rgb()
        my_data = ["LEFT", xyzabc[0], xyzabc[1], xyzabc[2], left_colorsensor.reflection(), left_colorsensor.ambient(), str(left_colorsensor.color()).split('.')[-1], truth, "\n"]
        my_line=[str(i) for i in my_data]
        my_line = ",".join(my_line)
        cs_data.write(my_line)
        cbazyx = right_colorsensor.rgb()
        my_data = ["RIGHT", cbazyx[0], cbazyx[1], cbazyx[2], right_colorsensor.reflection(), right_colorsensor.ambient(), str(right_colorsensor.color()).split('.')[-1], truth, "\n"]
        my_line=[str(i) for i in my_data]
        my_line = ",".join(my_line)
        cs_data.write(my_line)
    cs_data.close()

def trey_test():
    gyro.reset_angle(90)
    tyro = Ev3devSensor(Port.S2)
    print("first tyro: ", tyro.read('GYRO-G&A'))
    fid = open("trey.txt", "w")    
    track_stuff = []
    acceleration("heading", 100)
    speed_list = [400]
    direction = 1
    for max_speed in speed_list:
        for _ in range(400):
            calc_speed = int(max_speed * math.sin(2*math.pi*_/200))
            robot.drive(0,calc_speed)
            track_stuff.append((calc_speed,0, time.time(),tyro.read('GYRO-G&A')))
            # track_stuff.append((my_speed, turn, time.time(),gyro.angle(), gyro.speed()))
            time.sleep(0.04)
    gyro_stop()
    for row in track_stuff:
        for thing in row: 
            print(thing,end=",", file=fid)
        print("",file=fid)
    fid.close()
    ev3.speaker.beep()


def turn_test_2():
    fid = open("coach.txt", "w")    
    track_stuff = []
    accel_list = [50]
    for accel_val in accel_list:
        ev3.speaker.say("acceleration"+str(accel_val))
        acceleration("heading", accel_val)
        speed_list = [50,100,150,200,300,400]
        direction = 1
        for my_speed in speed_list:
            for turn in range(4):
                robot.drive(0,my_speed * direction)
                for _ in range(50):
                    track_stuff.append((my_speed, turn, time.time(),gyro.angle()))
                    time.sleep(0.04)
                direction = -direction 
        gyro_stop()
    for row in track_stuff:
        for thing in row: 
            print(thing,end=",", file=fid)
        print("",file=fid)
    fid.close()
    ev3.speaker.beep()

def acceltest():
    # acceleration("distance", )
    for _ in [39, 38, 37, 36, 35, 34, 33, 32, 31, 30]:
        ev3.speaker.say(str(_)+"%")
        acceleration("distance", _)
        acceleration("heading", _)
        # left_wheel.control.limits(800, 16*_,100)
        # right_wheel.control.limits(800, 16*_,100)
        # robot = DriveBase(left_wheel, right_wheel, cwd, cat)
        # robot.distance_control.limits(603,24*_,100)
        # robot.heading_control.limits(571,23*_,100)

        # Drive forward 300
        forward_angle(0, 300, 200)
        # ev3.speaker.beep()
        forward_angle(0, 100, 160)
        gyro_stop()
        ev3.speaker.beep()
        time.sleep(1)
        forward_angle(0, -300, -200)
        # ev3.speaker.beep()
        forward_angle(0, -100, -160)
        gyro_stop()
        time.sleep(4)


    for _ in [100, 50, 25, 10, 5]:
        ev3.speaker.say(str(_)+"%")
        # left_wheel.control.limits(800, 16*_,100)
        # right_wheel.control.limits(800, 16*_,100)
        # robot = DriveBase(left_wheel, right_wheel, cwd, cat)
        robot.distance_control.limits(603,24*_,100)
        robot.heading_control.limits(571,23*_,100)

        # Drive forward 300
        forward_distance(speed=400, turn_rate=0, distance=300)
        ev3.speaker.beep()
        forward_distance(speed=100, turn_rate=0, distance=100)
        gyro_stop()
        ev3.speaker.beep()
        time.sleep(1)

        # Turn around
        robot.turn(360)
        gyro_stop()
        robot.turn(-360)
        gyro_stop()

        forward_distance(speed=-400, turn_rate=0, distance=-300)
        ev3.speaker.beep()
        forward_distance(speed=-100, turn_rate=0, distance=-100)
        gyro_stop()
        ev3.speaker.beep()
  
    ev3.speaker.beep()

def easyturn(sequence):
    x = 0
    sleeptime = .5
    start_time = time.time()
    for x in sequence:
        print(x)
        # final_gyro_angle = gyroturno(x, 2, stop=True)
        robot.turn(x)
        print("after robot_turn()")
        ev3.screen.clear()
        ev3.screen.set_font(big_font)
        ev3.screen.print("Gyro:",str(gyro.angle()))
        time.sleep(sleeptime)
    end_time = time.time()
    final_time = (end_time - start_time)
    ev3.screen.set_font(big_font)
    ev3.screen.clear()
    ev3.speaker.set_volume(100)
    ev3.screen.print(str(final_time - (sleeptime * len(sequence)))[0:4])
    ev3.speaker.say(str(final_time - (sleeptime * len(sequence)))[0:4])

def turntest():
    robot.stop()
    print(robot.distance_control.limits())
    print(robot.heading_control.limits())
    robot.settings(straight_speed=300, straight_acceleration=300, turn_rate=200,  turn_acceleration=760)
    gyro.reset_angle(0)
    #robot.distance_control.limits(607,243,100)
    #forward_distance(400, 0, 400)
    #forward_distance(50, 0, 400)
    #robot.stop()
    #time.sleep(5)
    easyturn([90, 90, 90, 90])
    time.sleep(2)
    easyturn([-90, -90, -90, -90])
    # robot.straight(250)
    # easyturn([90, 180, 270, 360])
    # # time.sleep(2)
    # easyturn([270, 180, 90, 0])
    # robot.drive(-100,0)
    # for _ in range(3):
    #     ev3.speaker.beep()
    #     time.sleep(1)
    robot.stop()
    
def pidtest():
    # pidline(sensor='left', distance=1000, speed=30, Kp=0.45, Ki=0.9, Kd=1.1)
    ev3.speaker.beep()
    ev3.speaker.set_speech_options(voice='f2')
    ev3.speaker.say("starting test")
    for _ in range(100,200,20):
        ev3.speaker.say(str(_))
        line_follow(700,_,"left","right",Kp=0.6,Ki=0.00006,Kd=0)
        gyro_stop()

def gyrotest():
    gyro.reset_angle(0)

    # test_gyro_turno=False
    # if (test_gyro_turno):
    gyroturno(90)
    time.sleep(2)
    ev3.speaker.beep()
    gyroturno(180)
    ev3.speaker.beep()
    time.sleep(2)
    gyroturno(270)
    ev3.speaker.beep()
    time.sleep(2)
    gyroturno(0)
    ev3.speaker.beep()
    time.sleep(2)
    robot.stop()

    gyroturno(-90)
    ev3.speaker.beep()
    time.sleep(2)
    gyroturno(-180)
    ev3.speaker.beep()
    time.sleep(2)
    gyroturno(-270)
    ev3.speaker.beep()
    time.sleep(2)
    gyroturno(-0)
    robot.stop()
    # else:

    #     gyro_straight(distance=1000, speed=-100, reset_angle=45)
    #     ev3.speaker.beep()
    #     robot.stop()
def view_color():
    ev3.screen.set_font(med_font)
    while Button.LEFT not in ev3.buttons.pressed():
        time.sleep(.5)
        ev3.screen.clear()
        r_color = get_color(right_colorsensor)
        l_color = get_color(left_colorsensor)
        r_raw = get_color(right_colorsensor, raw=True)
        l_raw = get_color(left_colorsensor, raw=True)
        ev3.screen.print("press LEFT to end")
        ev3.screen.print("ml:")
        ev3.screen.print("L clr: {}".format(l_color))
        ev3.screen.print(" raw:", l_raw)
        ev3.screen.print("R clr: {}".format(r_color))
        ev3.screen.print(" raw:", r_raw)
        ev3.screen.print("pb L clr: {}".format(left_colorsensor.color()))
        ev3.screen.print("pb R clr: {}".format(right_colorsensor.color()))
        time.sleep(1)
def test_follow():
    
    line_follow(1000,200,"left" , "right", True)

def motor_test():
    
    time.sleep(5)
    def log():
        
        t=time.time()
        print(t,t+7)
        while time.time() < t+10.00001:
            print(str(time.time()-t)+", "+str(left_wheel.speed()))
        
    x=threading.Thread(target=log)
    x.start()
    left_wheel.run(650)
    time.sleep(1)
    left_wheel.stop()
    time.sleep(.5)
    left_wheel.run(650)
    time.sleep(1)
    left_wheel.brake()
    time.sleep(.5)
    left_wheel.run(650)
    time.sleep(1)
    left_wheel.hold()
    time.sleep(.5)
    ev3.speaker.beep(1000,900)
