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
import threading
import tv
import lib
import oil_supporter
data = {"time": 150, "started": False, "values": load_data()}
lis = [
    "callums test",
    "turn test",
    "pid test",
    "gyro test",
    "color collect",
    "color viewer", 
    "tv flip",
    "oil supporter"
    ]
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

def printn(text, end="\n"):
    if len(text) > 36:
        raise TypeError("more than nesecary")
    print(text, end=end)

printused = ev3.screen.print
selected = 6
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
        qw.start()
    if selected == 0:
        lib.callum()
    elif selected == 1:
        lib.turntest()
    elif selected == 2:
        lib.pidtest()
    elif selected == 3:
        lib.gyrotest()
    elif selected == 5:
        lib.view_color()
    elif selected == 4:
        lib.cs_data(truth="NOTWHITE")
    elif selected == 6:
        tv.flip_tv()
    elif selected == 7:
        oil_supporter.followline()


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
        # Back up against the wall, reset gyro angle
        robot.drive(-100, 0)
        time.sleep(0.25)
        gyro.reset_angle(0)
        robot.stop()
        
        functions(selected)

        data['values'] = load_data()