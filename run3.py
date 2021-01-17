#!/usr/bin/env python3

from time import sleep
import time
from ev3dev2.led import Leds
from ev3dev2.motor import (OUTPUT_A, OUTPUT_B, OUTPUT_D, LargeMotor,
                           MediumMotor, MoveDifferential, MoveTank,
                           SpeedPercent, SpeedRPM, follow_for_ms, MoveSteering)
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


STUD_MM = 8

#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_


mdiff = MoveDifferential(OUTPUT_A, OUTPUT_D, EV3Tire, 16 * STUD_MM)
tank = MoveTank(OUTPUT_A, OUTPUT_D)
tank.cs = ColorSensor(INPUT_3)
tank.cs_2 = ColorSensor(INPUT_2)
motor_right = LargeMotor(OUTPUT_D)
motor_lept = LargeMotor(OUTPUT_A)
med = MediumMotor(OUTPUT_B)
steering_drive = MoveSteering(OUTPUT_A, OUTPUT_D)
#-----------------------------------------------------------------------------


def follow_line():
    tank.follow_line(
        kp=1.8, ki=0.009, kd=0,
        speed=SpeedPercent(-20),
        follow_for=follow_for_ms,
        ms=1820,
        follow_left_edge=True
        )


def run3_b():
    med.on_for_rotations(15, 1, brake=True, block=True)
    print("arm up")
    mdiff.on_for_distance(15, -100, brake=True, block=True)
    print("forward complete, ready to line follow")
    follow_line()
    print("follow line complete")
    motor_right.on_for_rotations(5, 0.075, brake=True, block=True)
    print("turn into mission complete")
    mdiff.on_for_distance(15, -18, brake=True, block=True)
    print("going forward")
    med.on_for_rotations(30, -1.15, brake=True, block=True)
    print("dropping arm")
    mdiff.on_for_distance(15, 20, brake=True, block=True)
    motor_lept.on_for_rotations(5, 0.05, brake=True, block=True)
    print("turned")
    mdiff.on_for_distance(15, 33.4, brake=True, block=True)
    motor_lept.on_for_rotations(5, -0.09, brake=True, block=True)
    med.on_for_rotations(20, 1.1, brake=True, block=True)
    print("mini boccia complete")
    time.sleep(2)



    mdiff.on_for_distance(15, -20, brake=True, block=True)
    motor_lept.on_for_rotations(5, 0.32, brake=True, block=True)
    med.on_for_rotations(20, 1, brake=True, block=True)
    time.sleep(15)
    mdiff.on_for_distance(15, -53, brake=True, block=True)
    motor_right.on_for_rotations(5, 0.73, brake=True, block=True)
    med.on_for_rotations(15, -1.9, brake=True, block=True)
    time.sleep(3)
    mdiff.on_for_distance(5, -70, brake=True, block=True)
    time.sleep(5)
    med.on_for_rotations(50, 2, brake=True, block=True)
    time.sleep(2)



    mdiff.on_for_distance(20, 40, brake=True, block=True)
    motor_right.on_for_rotations(5, 1.2, brake=True, block=True)
    mdiff.on_for_distance(20, -40, brake=True, block=True)
    motor_right.on_for_rotations(5, 0.4, brake=True, block=True)
    mdiff.on_for_distance(20, 65, brake=True, block=True)
    motor_lept.on_for_rotations(5, 0.6, brake=True, block=True)
    mdiff.on_for_distance(20, 120, brake=True, block=True)
    motor_right.on_for_rotations(5, -0.55, brake=True, block=True)
    mdiff.on_for_distance(10, 50, brake=True, block=True)
    motor_lept.on_for_rotations(5, 0.1, brake=True, block=True) ###
    med.on_for_rotations(50, -1.2, brake=True, block=True)
    mdiff.on_for_distance(10, 40, brake=True, block=True)
    #motor_lept.on_for_rotations(5, 0.09, brake=True, block=True) #0.09 or 0.12
    mdiff.on_for_distance(10, 60, brake=True, block=True)
    #motor_lept.on_for_rotations(5, 0.15, brake=True, block=True)
    mdiff.on_for_distance(10, 20, brake=True, block=True)
    med.on_for_rotations(50, -0.5, brake=True, block=True)
    motor_lept.on_for_rotations(5, 0.15, brake=True, block=True)
    med.on_for_rotations(50, -0.1, brake=True, block=True)
    motor_lept.on_for_rotations(5, -0.2, brake=True, block=True)
    med.on_for_rotations(50, 0.5, brake=True, block=True)
    #motor_lept.on_for_rotations(5, -0.05, brake=True, block=True)
    mdiff.on_for_distance(10, -20, brake=True, block=True)
    #motor_lept.on_for_rotations(5, -0.05, brake=True, block=True)
    mdiff.on_for_distance(10, -100, brake=True, block=True)
    time.sleep(2)

    while True: 
        med.on_for_rotations(50, 1.5, brake=True, block=True)
        motor_right.on_for_rotations(5, -0.4, brake=True, block=True)
        mdiff.on_for_distance(40, -120, brake=True, block=True)
        mdiff.on_for_distance(10, -20, brake=True, block=True)
        mdiff.on_for_distance(10, 20, brake=True, block=True)
        med.on_for_rotations(50, -0.5, brake=True, block=True)
        motor_lept.on_for_rotations(5, -0.05, brake=True, block=True)
        motor_lept.on_for_rotations(5, 0.05, brake=True, block=True)
        mdiff.on_for_distance(10, -20, brake=True, block=True)   
        mdiff.on_for_distance(10, 20, brake=True, block=True)

run_one()

