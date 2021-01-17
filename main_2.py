#!/usr/bin/env python3

#  in one thread, have the follow line 
# in the other thread, have the right side motor count rotations
# if motor rotations == some number, you should stop the robot
#all threads should be killed now
#lift the arm up
# move forward after arm is up
# move arm down 
# move backwards
# lift arm up to hit green thing
#bring arm back down to horizontal position (not original pos)
# turn left 
# lift arm up until totally vertical 
# move backwards
# turn for x degrees
# drop arm down
#go forward into the phone
# lift arm up quickly
# move back until sensor hits the line
# turn x degress until parallel with the wall
# move backwards for x rotations
#turn right from the back
# go forwards
# turn right
# lift arm til parallel with the floor
# go forwards through the bar until it hits the line
# turn left for x degrees
# go forward into dance mission and do multiple turns
#--------------------------------------------------------------------------
from time import sleep


import time

from ev3dev2.led import Leds
from ev3dev2.motor import (OUTPUT_A, OUTPUT_B, OUTPUT_D, LargeMotor,
                           MediumMotor, MoveDifferential, MoveTank,
                           SpeedPercent, SpeedRPM, follow_for_ms)
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, TouchSensor
from ev3dev2.sound import Sound
from ev3dev2.wheel import EV3Tire
import sys
import logging
import time
import ctypes
from ev3dev2.button import ButtonBase
from ev3dev2.sensor import Sensor
import os
from logging import getLogger
from os.path import abspath
from ev3dev2 import get_current_platform, Device, list_device_names, DeviceNotDefined, ThreadNotRunning
from ev3dev2.stopwatch import StopWatch
import sys
import math
import select
import time
import threading
from threading import Thread
import logging # this is used for logging
#-------------------------------------------------------------------------------
mdiff = MoveDifferential(OUTPUT_A, OUTPUT_D, EV3Tire, 16 * STUD_MM)
tank = MoveTank(OUTPUT_A, OUTPUT_D)
tank.cs = ColorSensor(INPUT_3)
tank.cs_2 = ColorSensor(INPUT_2)
motor_right = LargeMotor(OUTPUT_D)
m = MediumMotor(OUTPUT_B)
#-----------------------------------------------------------------------------

#use motor_right.count_per_rot() to count rotations 
# use __exit__(self, t, v, tb) to exit a thread maybe?

def follow_line():
	tank.follow_line(
		kp=1.8, ki=0.009, kd=0,
		speed=SpeedPercent(-20),
		follow_for=follow_for_ms,
		ms=3500, follow_left_edge=True
        )

def motor_rotation_finder():
    loop = 0
    while loop == 0:
        x = motor_right.count_per_rot()
        if x == 35: #put in some number here, this is the number of rotations the thing will look for to stop
            tank.stop()
            loop=2


m.on_for_rotations(30, 1, brake=True, block=True)
mdiff.on_for_distance(15, -100, brake=True, block=True)
a = threading.Thread(target=follow_line, daemon=True)
b = threading.Thread(target=motor_rotation_finder)

b.start()
a.start()

sys.exit() 
