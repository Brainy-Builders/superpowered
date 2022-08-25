# Where everything is defined
# Objects defined here can be used in any of the files
# These should include the ev3 and robot
# This way the ev3 and robot don't need to be always passed to functions are arguments
#

import json
from functools import wraps
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (
    Motor,
    TouchSensor,
    ColorSensor,
    InfraredSensor,
    UltrasonicSensor,
    GyroSensor,
)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font
import time
import math
from gyroturno import *

# Define some useful things
min_font = Font(size=6)
tiny_font = Font(size=6)
med_font = Font(size=12)
big_font = Font(size=24, bold=True)
# Create your objects here.
ev3 = EV3Brick()
# Configure settings for this robot
left_wheel = Motor(Port.A)
right_wheel = Motor(Port.D)
wheel_diameter = 56
main_motor = Motor(Port.C)

try:
    open("back")
    back_motor= Motor(Port.C)
except:
    back_motor = Motor(Port.B)
#axle_track = 108 # Cor-3 robot from 2019 season
axle_track = 96  # Chloe's robot for 2020, '21, '22 seasons
try:
    gyro = GyroSensor(Port.S2, direction=Direction.CLOCKWISE)
    gyro.reset_angle(0)
except:
    class fg:
        def reset_angle(self,angle):
            pass
        def angle(self):
            return "fake gyro sensor "
    gyro=fg()
cwd = 90
cat = 134 
robot = DriveBase(left_wheel, right_wheel, cwd, cat)
def panic_alarm():
    ev3.light.on(Color.RED)
    ev3.screen.print("ERROR: COLOR_SENSORS NOT ENTERED ¯\_(ツ)_/¯")
    for i in range(0, 2):
        ev3.speaker.beep(750)
        time.sleep(.2)
        
up = Motor(Port.C)
side = Motor(Port.A)
try:
    left_colorsensor = ColorSensor(Port.S1)
except:
    left_colorsensor = "None"
    panic_alarm()
try:
    right_colorsensor = ColorSensor(Port.S4)
except:
    right_colorsensor = "None"
    panic_alarm()
# if color sensors are not attached panic
inf = 5000
BLACK = 6
#WHITE = 76
WHITE = 90
main_motor = Motor(Port.C)
def move_motor(speed, angle, mustWait=True):
      main_motor = Motor(Port.C)
    #   main_motor.reset_angle(0)
      main_motor.run_target(speed, int(main_motor.angle()) + angle, wait=mustWait)

def reset_motor():
    main_motor.run_target(900, 0)

def calibration():
    ev3.screen.clear()
    file = open("color.json", "w+")
    global BLACK
    global WHITE
    ev3.screen.set_font(med_font)
    time.sleep(1)
    ev3.screen.print("put the robot on WHITE")
    ev3.screen.print("(press CENTER)")
    color_list = []
    while True:
        if Button.CENTER in ev3.buttons.pressed():
            ev3.screen.print(
                "left: ",
                left_colorsensor.reflection(),
                "\nright:",
                right_colorsensor.reflection(),
                "\n l color", 
                str(left_colorsensor.rgb()),
                "\n r color", 
                str(right_colorsensor.rgb())
            )
            white = (
                left_colorsensor.reflection() + right_colorsensor.reflection()
            ) / 2
            color_list.append({"left": left_colorsensor.rgb()})
            color_list.append({"right": right_colorsensor.rgb()})
            print("white=", WHITE)
            time.sleep(5)
            break
    ev3.screen.print("put the robot on BLACK")
    ev3.screen.print("press CENTER")
    while True:
        if Button.CENTER in ev3.buttons.pressed():
            ev3.screen.print(
                "left: ",
                left_colorsensor.reflection(),
                "\nright:",
                right_colorsensor.reflection(),
            )
            black = (
                left_colorsensor.reflection() + right_colorsensor.reflection()
            ) / 2
            print("black=", BLACK)
            time.sleep(5)
            break
    ev3.screen.print("put the robot on the \nlight blue lake")
    ev3.screen.print("press CENTER")
    while True:
        if Button.CENTER in ev3.buttons.pressed():
            bluel = left_colorsensor.rgb()
            bluer = right_colorsensor.rgb()
            blueavg = (bluel[0]+bluer[0])/2
            blue = {"bluel":bluel, "bluer":bluer,"avg":blueavg}
            break
    ev3.screen.clear()
    time.sleep(5)
    ev3.screen.print("on white")
    while True:
        if Button.CENTER in ev3.buttons.pressed():
            whitel = left_colorsensor.rgb()
            whiter = right_colorsensor.rgb()
            whiteavg = (whitel[0]+whiter[0])/2
            white_1 = {"whitel": whitel, "whiter":bluer, "avg":whiteavg}
            break
    time.sleep(5)
    ev3.screen.clear()
    ev3.screen.print("black = ", black, "\nwhite = ", white)
    data = dict({"white": int(WHITE), "black": int(BLACK), "colors": {"blue":blue, "white":white_1}})
    json_data = json.dumps(data, indent=4)
    file.write(json_data)
    file.close()
    time.sleep(3)
def load_data():
    try:
        f = open("color.json", "r")
        data = json.load(f)    
        f.close()
        return data["white"], data["black"]
    except Exception as e:
        # return 11, 95
        # print("Jackson error (ignore):"+str(e))
    
        return 95, 11

def forward_dist(speed, turn_rate, distance):
    if(distance<0):
        end_distance = robot.distance()+distance
        while(robot.distance() > end_distance):
            robot.drive(speed,turn_rate)
    end_distance = robot.distance()+distance
    while(robot.distance() < end_distance):
        robot.drive(speed,turn_rate)
forward_distance = forward_dist

def load_avg(): 
    try:
        f = open("color.json", 'r')
        data = json.load(f)
        f.close()
        colors = data['colors']
        return (colors['blue']['avg']+colors['white']['avg'])/2
    except:
        return 45

def sus():
    ev3.screen.clear()
    iteration = 0
    temp = {}
    jsons = {}
    for i in range(0, 6):
        ev3.screen.print("presss the center button on white")
        while not Button.CENTER in ev3.buttons.pressed():
            pass
        ev3.screen.clear()
        temp["left"] = left_colorsensor.rgb()
        temp["right"] = right_colorsensor.rgb()
        jsons[str(iteration)+"white"] = temp
        temp = {}
        time.sleep(1)
        ev3.screen.print("presss the center button on blue")
        while not Button.CENTER in ev3.buttons.pressed():
            pass
        ev3.screen.clear()
        temp["left"] = left_colorsensor.rgb()
        temp["right"] = right_colorsensor.rgb()
        jsons[str(iteration)+"blue"] = temp
        temp = {}
        iteration += 1
        time.sleep(1)
    f = open("test.json", "w+")
    json.dump(jsons, f)
    f.close()
    del f

def detection():
    ev3.screen.set_font(med_font)
    while True:
        ev3.screen.clear()
        correct = left_colorsensor.rgb()[0] > 45 and right_colorsensor.rgb()[0] > 45 
        ev3.screen.print("left white: {0}\nright white: {1}\nboth white: {2}".format(left_colorsensor.rgb()[0] > 45, right_colorsensor.rgb()[0] > 45, correct))
        ev3.screen.print("right: {0}, left: {1}".format(right_colorsensor.rgb(), left_colorsensor.rgb()))
        ev3.screen.print("i think the colors are: \nLEFT: {0}, RIGHT: {1}".format(str(left_colorsensor.color()).strip("Color."), str(right_colorsensor.color()).strip("Color.")))
        time.sleep(.3)

def get_color(sensor):
    r=sensor.rgb()
    green,blue=r[1],r[2]
    reflectivity=sensor.reflection()
    if green <= 14.00:
            color = Color.BLACK
    if green >  14.00:
        if blue <= 72.00:
                color = "OTHER"
        if blue >  72.00:
            if reflectivity <= 40.50:
                    color = "OTHER"
            if reflectivity >  40.50:
                    color = Color.WHITE
    return color