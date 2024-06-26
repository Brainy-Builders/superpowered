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
from line_a_line import *
import linefollow
import threading
import logging
import random

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


def gyro_track():
    gyro.reset_angle(0)
    giant_font = Font(size=200, bold=True)
    ev3.screen.set_font(giant_font)
    while(True):
        ev3.screen.clear()
        ev3.screen.print(gyro.angle())
        time.sleep(0.1)

def dance():
    # gyro_track()

    def show_angle():
        ev3.screen.clear()
        ev3.screen.print(gyro.angle()) 
        time.sleep(1)    

    ev3.screen.set_font(huge_font)
    ev3.screen.clear()
    gyro.reset_angle(0)
    acceleration("heading", 25)
    forward_distance(speed=200, turn_rate=0, distance=200)
    robot.drive(0,0)
    time.sleep(0.5)
    robot.stop()
    show_angle()
    ev3.speaker.beep()
    while(gyro.angle() <= 90):
        left_wheel.run(200)
    gyro_stop()
    ev3.speaker.beep()
    show_angle()
    while(gyro.angle() >= 0):
        right_wheel.run(200)
    gyro_stop()
    ev3.speaker.beep()
    show_angle()
    robot.turn(360)
    gyro_stop()
    show_angle()
    robot.turn(-360)
    gyro_stop()
    show_angle()
    ev3.speaker.say("cha cha cha")
    gyro_straight(distance=400, speed=-200, reset_angle=0)
    gyro_stop()
    ev3.speaker.beep()
    show_angle()
    time.sleep(5)
    gyro_track()

def goto_waterfall():
    robot.drive(speed=150,turn_rate=0)
    time.sleep(3)
    gyro_stop()
    ev3.speaker.say("mechanically aligned")
    gyro.reset_angle(45)

def second_follow_lines():
    robot.settings(straight_speed=150, straight_acceleration=100, turn_rate=180,  turn_acceleration=180)
    robot.straight(-150)
    gyroturno(0)
    gyro_stop()
    ev3.speaker.say("find the line")
    while(get_color(left_colorsensor) != Color.BLACK):
        robot.drive(100,0)
    robot.straight(50)
    gyro_stop()
    ev3.speaker.say("put left color sensor black")
    while(get_color(left_colorsensor) != Color.BLACK):
        robot.drive(0,30)
    robot.straight(-75)    
    gyro_stop()
    ev3.speaker.say("follow line")
    linefollow.line_follow(length=250, speed=100, sensor="left", side="left", Kp=0.7, Ki=0, Kd=0)
    gyro_stop()
    ev3.speaker.say("put right colorsensor on black")
    while(get_color(right_colorsensor) != Color.WHITE):
        robot.drive(100,0)
    ev3.speaker.beep()
    while(get_color(right_colorsensor) != Color.BLACK):
        robot.drive(100,0)
    gyro_stop()
    ev3.speaker.say("gyroturno")
    gyroturno(90)
    ev3.speaker.beep()
    # put left CS on white
    while(left_colorsensor.reflection() < 70):
        right_wheel.run(50)
    gyro_stop()
    ev3.speaker.say("follow the line")
    linefollow.line_follow(length=420, speed=100, sensor="left", side="left", Kp=0.4, Ki=0, Kd=0)
    gyro_stop()
    ev3.speaker.say("find black then backup")
    while(get_color(right_colorsensor) != Color.WHITE):
        robot.drive(50,0)
    while(get_color(right_colorsensor) != Color.BLACK):
        robot.drive(50,0)
    robot.straight(-50)
    gyro_stop()
    gyroturno(180)
    gyro_stop()

def align_tricks():
    # Rough line align
    ev3.speaker.say("align to the line")
    while( (get_color(left_colorsensor) != Color.BLACK) and (get_color(right_colorsensor) != Color.BLACK)):
        right_wheel.run(-75)
        left_wheel.run(-75)
    gyro_stop()
    forward_distance(speed=75, turn_rate=0, distance=25, t_prime=0.2)
    gyro_stop()
    while(left_colorsensor.reflection() > 15):
        left_wheel.run(-75)
    gyro_stop()
    while(right_colorsensor.reflection() > 15):
        right_wheel.run(-75)
    gyro_stop()
    
    # backup, forward to black
    robot.straight(-25)
    gyro_stop()
    while(left_colorsensor.reflection() > 15):
        left_wheel.run(50)
    gyro_stop()
    while(right_colorsensor.reflection() > 15):
        right_wheel.run(50)

    # forward, back  to black
    robot.straight(25)
    gyro_stop()
    while(left_colorsensor.reflection() > 20):
        left_wheel.run(-50)
    gyro_stop()
    while(right_colorsensor.reflection() > 20):
        right_wheel.run(-50)
    gyro_stop()

def drivebase_showoff():
    ev3.speaker.say("go back using drivebase")
    robot.settings(straight_speed=250, straight_acceleration=100, turn_rate=180,  turn_acceleration=180)
    robot.straight(600)
    robot.turn(90)
    robot.straight(680-75)
    robot.turn(135)

def loopzioni():
    ev3.speaker.say("Point me towards the waterfall")
     
    for _ in range(7):
        goto_waterfall()
        second_follow_lines()
        align_tricks()
        drivebase_showoff()
        ev3.speaker.say(str(_+1))
        ev3.speaker.say("loop done")
        ev3.speaker.say("robot made by the Brainy Builders")
        ev3.speaker.say("lets go again")
    ev3.speaker.say("done!")

def coach():
    my_dist = 700
    wheel_diameter = 87
    my_rotations = my_dist / (3.14*wheel_diameter)
    my_rotation_angle = my_rotations * 360
    robot.stop()
    robot.reset()

    ev3.speaker.say("using drive, similar to wheel angle")
    for _ in range(4):
        my_speed = 100*(1+2*_)
        ev3.speaker.say("speed="+str(my_speed))
        ev3.speaker.beep()
        time.sleep(1)
        forward_dist(speed=my_speed, turn_rate=0, distance=my_dist)
        gyro_stop()
        time.sleep(1)
        forward_dist(speed=-my_speed, turn_rate=0, distance=-my_dist)
        gyro_stop()

    while(not Button.CENTER in ev3.buttons.pressed()):
        robot.stop()
    ev3.speaker.beep()        

    ev3.speaker.say("Using acceleration to gradually start and stop")
    for _ in range(4):
        my_speed = 100*(1+2*_)
        ev3.speaker.say("speed="+str(my_speed))
        ev3.speaker.beep()
        time.sleep(1)
        robot.stop()
        robot.settings(straight_speed=my_speed,
                       straight_acceleration=0.75*my_speed,
                       turn_rate=240,
                       turn_acceleration=180)
        robot.straight(my_dist)
        gyro_stop()
        time.sleep(1)
        robot.straight(-my_dist)
        gyro_stop()

    while(not Button.CENTER in ev3.buttons.pressed()):
        robot.stop()
    ev3.speaker.beep()        

    ev3.speaker.say("Using gyro to go in the right direction")
    gyro.reset_angle(angle=0)

    for _ in range(4):
        my_speed = 100*(1+2*_)
        ev3.speaker.say("speed="+str(my_speed))
        ev3.speaker.beep()
        time.sleep(1)
        gyro_straight(distance=my_dist, speed=my_speed, reset_angle=0, t_prime=1)
        gyro_stop()
        time.sleep(1)
        gyro_straight(distance=my_dist, speed=-my_speed, reset_angle=0, t_prime=1)
        gyro_stop()
    
    return 0

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
def gyroturntest():
    # gyro.reset_angle(0)
    # gyroturn(-90, stop=True)
    # return

    for _ in [90, 180, 270,]:
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
    sleeptime = .5
    start_time = time.time()
    for x in sequence:
        # final_gyro_angle = gyroturno(x, 2, stop=True)
        ev3.screen.clear()
        print("about to run gyroturno")
        gyroturn(x, rate_control=1.2, stop=True)
        # print("after robot_turn()")
        # ev3.screen.clear()
        # ev3.screen.set_font(big_font)
        # ev3.screen.print("Gyro:",str(gyro.angle()))
        time.sleep(sleeptime)
    end_time = time.time()
    final_time = (end_time - start_time)
    ev3.screen.set_font(big_font)
    ev3.screen.clear()
    ev3.speaker.set_volume(100)
    ev3.screen.print(str(final_time - (sleeptime * len(sequence)))[0:4])
    ev3.speaker.say(str(final_time - (sleeptime * len(sequence)))[0:4])
    # ev3.speaker.say(str(gyro.angle()))

def turntest():
    # robot.stop()
    # print(robot.distance_control.limits())
    # print(robot.heading_control.limits())
    # robot.settings(straight_speed=300, straight_acceleration=300, turn_rate=200,  turn_acceleration=760)
    # gyro.reset_angle(0)
    #robot.distance_control.limits(607,243,100)
    #forward_distance(400, 0, 400)
    #forward_distance(50, 0, 400)
    #robot.stop()
    #time.sleep(5)
    gyro.reset_angle(0)
    easyturn([90, 180, 270, 360])
    time.sleep(2)
    # easyturn([-90, -90, -90, -90])
    # robot.straight(250)
    # easyturn([90, 180, 270, 360])
    # # time.sleep(2)
    easyturn([270, 180, 90, 0])
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
    
def gyrotimetest():
    gyro_straight(target_time = 5)
    gyro_stop()
    time.sleep(2)
    gyro_straight(speed = -200, target_time = 5)
    gyro_stop()
    time.sleep(2)
    gyro_straight(distance = 200)
    gyro_stop()
    time.sleep(2)
    gyro_straight(distance = 200, speed = -200)
    gyro_stop()
    ev3.speaker.beep()


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
        
def self_test():
    tune = list(range(250,600,20))
    random.shuffle(tune)
    [ev3.speaker.beep(i,100) for i in tune]
    ev3.screen.clear()
    ev3.screen.set_font(med_font)
    # Check for unplugged devices
    erroring = []
    if left_colorsensor == "None":
        erroring.append("L-COLOR")
    if right_colorsensor == "None":
        erroring.append("R-COLOR")

    if False: pass

    if erroring != []:
        ev3.screen.set_font(big_font)
        ev3.screen.print("ERROR\n {}".format("\n".join(erroring)))
        ev3.speaker.beep(700,1000)
        time.sleep(0.1)
        ev3.speaker.beep(600,500)
        time.sleep(5)
        return 0
    gyro.reset_angle(0)
    g0 = gyro.angle()
    back_motor.run(500)
    main_motor.run(500)
    time.sleep(2)
    back_motor.stop()
    main_motor.stop()
    g1=gyro.angle()
    ev3.screen.print("Gyro-drift: {} deg".format(g1-g0))
    ev3.screen.print("L: {} R: {}".format(left_colorsensor.color(),right_colorsensor.color()).replace("Color.",""))
    robot.straight(100)
    robot.drive(-100,0)
    time.sleep(1)
    robot.stop()
    left_wheel.run(100)
    time.sleep(1)
    left_wheel.brake()
    right_wheel.run(100)
    time.sleep(1)
    right_wheel.stop()
    time.sleep(5)


