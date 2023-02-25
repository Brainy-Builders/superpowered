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
from gyroturno import *
import os
import threading
import tv
import lib
import oil_supporter
import faucet
import power
import collectit
import epic_x
import toy_factory
import gyropath
import pidlinefollow

skip_truck = True
old_oil=False
simple_water=False

data = {"time": 150, "started": False, "values": load_data()}
lis = [
    "collect",
    "oil supporter",
    "truck",
    "waterfall",
    "power",
    "tv flip",
    "toy factory",
    "black_x", 
    "color viewer",
    "color collect",
    "acceleration",
    "gyro path"
    ]

def thread():
    while data["time"] >= 0:
        if Button.LEFT in ev3.buttons.pressed():
            main_menu()
        data["time"] -= 1
        if data["time"] < 20:
            ev3.light.on(Color.RED)
        elif data["time"] > 50:
            ev3.light.on(Color.GREEN)
        if data["time"] >= 21 and data["time"] <= 50:
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
selected = 1
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
        screen.print("Gyro: {}".format(gyro.angle()))
    except Exception as e:
        print(e)
        screen.print("Gyro: {}".format("Unplugged"))

def functions(x):
    global selected
    print("SELECTED: ",selected)
    if not data["started"]:
        data["stated"] = True
        qw.start()
    if selected == 0:     # collect
        collectit.main()
    elif selected == 1:   # oil supporter
        if old_oil==True:
            oil_supporter.old_oil()
        else:    
            oil_supporter.main()
    elif selected == 2:   # truck
        oil_supporter.oiltruck()
    elif selected == 3:   # waterfall
        if simple_water==True:
            faucet.get_to_there()
        else:
            faucet.hang_water_units()
    elif selected == 4:   # power
        power.power_generator()
    elif selected == 5:   # tv flip
        tv.flip_tv()
    elif selected == 6:   # toy factory
        toy_factory.toy()
    elif selected == 7:   # black_x
        epic_x.main()
    elif selected == 8:   # color viewer
        lib.view_color()
    elif selected == 9:   # color collect
        lib.cs_data("WHITE")
    elif selected == 10:  # xxx
        # gyropath.run() 
        lib.gyrotimetest()
    elif selected == 11:  # xxx
        gyropath.run() 
    
while True: 
    time.sleep(.2)
    ev3.screen.clear()
    ev3.screen.set_font(big_font)
    ev3.screen.print("\n->"+lis[selected] + ":"+str(selected))
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
        print("center")
        ev3.speaker.beep()
        if selected==1:
            main_motor.stop()
        # Back up against the wall, reset gyro angle
        skip_backup = [1, 3, 4, 6, 7,10,11]
        if selected not in skip_backup:
            robot.drive(-100, 0)
            time.sleep(0.25)
        gyro_stop()
        gyro.reset_angle(0)
        acceleration("distance", 37)
        acceleration("heading", 30)
        functions(selected)
        selected += 1
        if skip_truck and selected == 2:
            selected = 3
        data['values'] = load_data()
        if selected==1:
            main_motor.run(-25)
        elif selected == 5:
            back_motor.run(25)
