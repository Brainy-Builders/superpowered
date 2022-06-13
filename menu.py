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
#import newlinefollow
import linefollow
from common import *
import os
import unusedcargo
import line_a_line
import poopybridge
import plane
import wheel_cleaner
import gyrostraight
import load_cargo
import amazon
import planetruckfinish
import coach
import sortingcenter
import threading
import robot_parade
import os
import multiprocessing
import signal
from gyroturno import *
import large_cargo

data = {"time": 150, "started": False, "values": load_data()}

def thread():
    while data["time"] >= 0:
        data["time"] -= 1
        if data["time"] < 45:
            ev3.light.on(Color.RED)
        elif data["time"] > 50:
            ev3.light.on(Color.GREEN)
        
        #     ev3.speaker.beep()
        #     ev3.speaker.beep()
        if data["time"] >= 45 and data["time"] <= 50:
            time.sleep(.5)
            ev3.light.on(Color.GREEN)
            time.sleep(.5)
            ev3.light.off()
            
        else:
            time.sleep(1)
qw = threading.Thread(target=thread)
ev3.screen.set_font(med_font)
lis = [
    "sorting cetr",         # 0
    "playne",               # 1
    "UPS",                  # 2
    "large cargo",          # 3
    "load cargo dash",      # 4
    "finish",               # 5
    "unused",               # 6
    "clean wheel",          # 7
    "color calibration",    # 8
    "detection",            # 9
    "line test"             # 10 
]
def printn(text, end="\n"):
    if len(text) > 36:
        raise TypeError("more than nesecary")
    print(text, end=end)

printused = ev3.screen.print
selected = 0
screen = ev3.screen
if len(lis)%2 != 0:
    lis.append("NONE")
def printscrn():
    for _ in range(0, len(lis), 2):
        object1 = str(str(_) + ":" + str(lis[_]))
        try:
            object2 = str(_ + 1) + ":" + lis[_ + 1]
        except:
            object2 = ""
        screen.print(
            object1
            + str("").center(
                5
            )
            + object2
        )
        
    fmt = len("Gyro: {}".format(gyro.angle()))
    tme = "Time: {}".format(data["time"])
    
    totals = fmt+len(tme)
    # comment out the next line if it doesnt work
    totals += len(data["values"])
    if totals % 2 != 0:
        totals -= 1
    totals = 36 - totals
    try:
        screen.print("Gyro: {}".format(gyro.angle())+" "*totals/2+data['values']+" "*totals/2+tme)
    except:
        screen.print("Gyro: {}".format("Unplugged")+" "*totals+tme)
def functions(x):
    global selected
    if not data["started"]:
        data["stated"] = True
        if selected != 0:
            qw.start()
        else:
            sortingcenter.sorting_center(qw)
    if x == 1:
        if plane.plain() == 0: #abort
            selected -= 1 
    elif x == 2:
        amazon.fedex()
    elif x == 3:
        large_cargo.largecargovroom()
    elif x == 4:
        load_cargo.main()
        # os.system(open('pybrcks.json', 'r').read())
        
    elif x == 5:
        planetruckfinish.finish()
    elif x == 6:
        main_motor.run_until_stalled(speed=400, then=Stop.COAST, duty_limit=None)
        main_motor.run_time(speed= 400, time=100, then = Stop.COAST, wait = True)
        # coach.rocks()
        pass
    elif x == 7:
        wheel_cleaner.wheelcleaner()
    if x == 8:
        calibration() 
    elif x == 9:
        detection()
    elif x == 10:
        line_a_line.line_a_line(white="yes")
while True: 
    time.sleep(.2)
    ev3.screen.clear()
    ev3.screen.set_font(big_font)
    ev3.screen.print("\n->"+lis[selected])
    ev3.screen.set_font(med_font)
    printscrn()
    # print(selected)
    if Button.DOWN in ev3.buttons.pressed():
        if selected == 0:
            selected = len(lis) - 1
            time.sleep(.01)
        else:
            selected -= 1
    elif Button.UP in ev3.buttons.pressed():
        if selected == (len(lis) - 1):
            selected = 0
            time.sleep(.01)
        else:
            selected += 1
    elif Button.CENTER in ev3.buttons.pressed():
        ev3.speaker.beep()
        if selected != 3:
            robot.drive(-100, 0)
        time.sleep(0.25)
        gyro.reset_angle(0)
        robot.stop()
        
        functions(selected)
        selected += 1
        data['values'] = load_data()