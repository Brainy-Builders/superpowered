#  __  __ ______ _   _ _    _ 
# |  \/  |  ____| \ | | |  | |
# | \  / | |__  |  \| | |  | |
# | |\/| |  __| |     | |  | |
# | |  | | |____| |\  | |__| |
# |_|  |_|______|_| \_|\____/ 

################################
#SELECTED -> Collect           #
# 1:Collect 2:Oil Supporter    #
# 3:Truck          4:Waterfall #
# 5:Power            6:TV flip #
# 7:Toy Factory      8:Black X #
#9:Color Viewer10:Color Collect#
# 11:Acceleration 12:Gyro Path #
# 13:Self Test         14:None #
################################
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
import final_mission
import toy_factory
import gyropath
import pidlinefollow

skip_truck = True # truck used to be a seperate mission with it's own function
# these 2 flags determine weather to use legacy versions of missions
old_oil=False
simple_water=False 

data = {"time": 150, "started": False, "values": load_data(),"start":time.time()} # global_data for multithreading
mission_list = [ # list of all missions
    "collect",       #  0
    "oil supporter", #  1
    "truck",         #  2
    "waterfall",     #  3
    "power",         #  4
    "tv flip",       #  5
    "toy factory",   #  6
    "black_x",       #  7
    "color viewer",  #  8
    "color collect", #  9
    "coach",         # 10
    "gyro path",     # 11
    "self_test"      # 12
    ]

def thread(): # Background loop
    while data["time"] >= 0:
        

        if data["time"] < 6: # 3 second warning for last mission
            ev3.light.on(Color.RED) # Urgent, hurry up for the last mission
        elif data["time"] > 50: 
            ev3.light.on(Color.GREEN)# Relax you've got time
        if data["time"] >= 6 and data["time"] <= 50:
            # I'd start to hurry up if I were you
            ev3.light.on(Color.YELLOW)
        time.sleep(1) # When it doesn't flash wait 1 second to not overload the thread
        data["time"] = 150 - (time.time() - data["start"])
        print(data["time"])


sw = threading.Thread(target=thread) # create a refrence to the service worker

ev3.screen.set_font(med_font) # Set font to be actually readable

def printn(text, end="\n"):
    if len(text) > 36:
        raise TypeError("more than nesecary")
    print(text, end=end)

selected = 10
screen = ev3.screen
if len(mission_list)%2 != 0:
    mission_list.append("NONE")

def printscrn():
    for _ in range(0, len(mission_list), 2):
        object1 = str(str(_) + ":" + str(mission_list[_]))
        try:
            object2 = str(_ + 1) + ":" + mission_list[_ + 1]
        except:
            object2 = ""
        screen.print(
            object1
            + "     "
            + object2
        )
        
    fmt = len("Gyro: {}".format(gyro.angle()))
    tme = "Time: {:.0f}".format(data["time"])
    
    totals = fmt+len(tme)
    # comment out the next line if it doesn't work
    totals += len(data["values"])
    if totals % 2 != 0:
        totals -= 1
    totals = 36 - totals # 36 chars is the screen width
    # Calculate spacing in order to make sure all chars fit on screen
    try:
        screen.print("Gyro: {}".format(gyro.angle()))
    except Exception as e:
        print(e)
        screen.print("Gyro: {}".format("Unplugged")) # If getting the gyro angle fails, it's not plugged in. 

def functions(x):
    global selected
    print("SELECTED: ",selected)
    if not data["started"]:
        data["stated"] = True # Enable so we don't continously execute the thread
        data["start"]  = time.time()
        sw.start() # start the service worker
    # each index corresponds to a mission
    if selected == 0:     # collect
        collectit.main()
    elif selected == 1:   # oil supporter
        if old_oil==True:
            oil_supporter.old_oil()
        else:    
            oil_supporter.main()
    elif selected == 2:   # truck
        oil_supporter.main()
    elif selected == 3:   # waterfall
        if simple_water==True:
            faucet.simple_water()
        else:
            faucet.advance_water()
    elif selected == 4:   # power
        power.power_generator()
    elif selected == 5:   # tv flip
        tv.flip_tv()
    elif selected == 6:   # toy factory
        toy_factory.toy()
    elif selected == 7:   # black_x
        final_mission.main()
    elif selected == 8:   # color viewer
        lib.view_color()
    elif selected == 9:   # color collect
        lib.cs_data("WHITE")
    elif selected == 10:  # xxx
        # gyropath.run() 
        # lib.gyrotimetest()
        ev3.speaker.say("new mission to help dynamic and pythonic droids")
        ev3.screen.draw_image(x = 0, y = 0, source = "splash.png", transparent=None)
        lib.coach()
        ev3.speaker.say("good luck dynamic and pythonic droids!")
    elif selected == 11:  # xxx
        gyropath.run() 
    if selected == 12:
        lib.self_test()
    
while True: 
    time.sleep(.2) # our ev3 screen run at  whopping 5hz
    # refresh screen
    ev3.screen.clear()
    ev3.screen.set_font(big_font)
    ev3.screen.print("\n->"+mission_list[selected] + ":"+str(selected)) # print selected mission and index
    ev3.screen.set_font(med_font)
    # print all missions and time and gyro
    printscrn()
    # button presses move menu
    if Button.DOWN in ev3.buttons.pressed():
        if selected == 0:
            selected = len(mission_list) - 1
            time.sleep(.01)
        else:
            selected -= 1
    elif Button.UP in ev3.buttons.pressed():
        if selected == (len(mission_list) - 1):
            selected = 0
            time.sleep(.01)
        else:
            selected += 1
    # run mission
    elif Button.CENTER in ev3.buttons.pressed():
        print("center")
        ev3.speaker.beep()
        if selected==1:
            main_motor.stop()
        # Back up against the wall, reset gyro angle
        # If the mission launch doesn't have a wall behind it, then we don't backup
        skip_backup = [1, 3, 4, 6, 7,10,11,12] 
        if selected not in skip_backup:
            robot.drive(-100, 0)
            time.sleep(0.25)
        gyro_stop()
        gyro.reset_angle(0)
        # Set baseline acceleration values
        acceleration("distance", 37)
        acceleration("heading", 30)
        #find which function needs to be run
        functions(selected)
        selected += 1

        if skip_truck and selected == 2:
            selected = 3
        if selected==1: # spin motors so attachments clip on easier
            main_motor.run(-25)
        elif selected == 5:
            back_motor.run(25)
            main_motor.run(25)

