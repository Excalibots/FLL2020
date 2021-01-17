#!/usr/bin/env python3
from configruation import *


def follow_line_1():
    tank.follow_line(
        kp=1.8, ki=0.009, kd=0,
        speed=SpeedPercent(-20),
        follow_for=follow_for_ms,
        ms=1820,
        follow_left_edge=True
        )
# follow line for 1820 ms on the left edge of the line

def run3_b():
    med.on_for_rotations(15, 1, brake=True, block=True)
    print("arm up")
    mdiff.on_for_distance(15, -100, brake=True, block=True)  
    print("forward complete, ready to line follow")
    follow_line_1()
    print("follow line complete")
    rightMotor.on_for_rotations(5, 0.075, brake=True, block=True)
    print("turn into mission complete")
    mdiff.on_for_distance(15, -18, brake=True, block=True)
    print("going forward")
    med.on_for_rotations(30, -1.15, brake=True, block=True)
    print("dropping arm")
    mdiff.on_for_distance(15, 20, brake=True, block=True)
    print("forward into mission complete")
    leftMotor.on_for_rotations(5, 0.05, brake=True, block=True)
    print("turned")
    mdiff.on_for_distance(15, 33.4, brake=True, block=True)
    print("move backwards out of mission complete")
    leftMotor.on_for_rotations(5, -0.09, brake=True, block=True)
    print("turn out of mission complete")
    med.on_for_rotations(20, 1.1, brake=True, block=True)
    print("mini boccia complete")
    sleep(2)



    mdiff.on_for_distance(15, -20, brake=True, block=True)
    print("move forward")
    leftMotor.on_for_rotations(5, 0.32, brake=True, block=True)
    print("turned")
    med.on_for_rotations(20, 1, brake=True, block=True)
    print("bring arm up")
    sleep(15)
    mdiff.on_for_distance(15, -53, brake=True, block=True)
    print("move forward complete")
    rightMotor.on_for_rotations(5, 0.73, brake=True, block=True)
    print("turn left until at phone flip ")
    med.on_for_rotations(15, -1.9, brake=True, block=True)
    print("bring arm down till ground")
    sleep(3)
    mdiff.on_for_distance(5, -70, brake=True, block=True)
    print("move forward until into the phone")
    sleep(5)
    med.on_for_rotations(50, 2, brake=True, block=True)
    print("flip phone")
    sleep(2)



    mdiff.on_for_distance(20, 40, brake=True, block=True)
    print("move out of phone")
    rightMotor.on_for_rotations(5, 1.2, brake=True, block=True)
    print("turn until out of the phone")
    mdiff.on_for_distance(20, -40, brake=True, block=True)
    print("move back to be align")
    rightMotor.on_for_rotations(5, 0.4, brake=True, block=True)
    print("align with the mini botia so that we can turn later")
    mdiff.on_for_distance(20, 65, brake=True, block=True)
    print("move forward to mini botia")
    leftMotor.on_for_rotations(5, 0.6, brake=True, block=True)
    print("turn towards the bridge ")
    mdiff.on_for_distance(20, 120, brake=True, block=True)
    print("go forward to bridge")
    rightMotor.on_for_rotations(5, -0.55, brake=True, block=True)
    print("turn until aligned with bridge")
    mdiff.on_for_distance(10, 50, brake=True, block=True)
    print("move forwards until  ")
    leftMotor.on_for_rotations(5, 0.1, brake=True, block=True) ###
    med.on_for_rotations(50, -1.2, brake=True, block=True)
    mdiff.on_for_distance(10, 40, brake=True, block=True)
    #leftMotor.on_for_rotations(5, 0.09, brake=True, block=True) #0.09 or 0.12
    mdiff.on_for_distance(10, 60, brake=True, block=True)
    #leftMotor.on_for_rotations(5, 0.15, brake=True, block=True)
    mdiff.on_for_distance(10, 20, brake=True, block=True)
    med.on_for_rotations(50, -0.5, brake=True, block=True)
    leftMotor.on_for_rotations(5, 0.15, brake=True, block=True)
    med.on_for_rotations(50, -0.1, brake=True, block=True)
    leftMotor.on_for_rotations(5, -0.2, brake=True, block=True)
    med.on_for_rotations(50, 0.5, brake=True, block=True)
    #leftMotor.on_for_rotations(5, -0.05, brake=True, block=True)
    mdiff.on_for_distance(10, -20, brake=True, block=True)
    #leftMotor.on_for_rotations(5, -0.05, brake=True, block=True)
    mdiff.on_for_distance(10, -100, brake=True, block=True)
    sleep(2)

    while True: 
        med.on_for_rotations(50, 1.5, brake=True, block=True)
        rightMotor.on_for_rotations(5, -0.4, brake=True, block=True)
        mdiff.on_for_distance(40, -120, brake=True, block=True)
        mdiff.on_for_distance(10, -20, brake=True, block=True)
        mdiff.on_for_distance(10, 20, brake=True, block=True)
        med.on_for_rotations(50, -0.5, brake=True, block=True)
        leftMotor.on_for_rotations(5, -0.05, brake=True, block=True)
        leftMotor.on_for_rotations(5, 0.05, brake=True, block=True)
        mdiff.on_for_distance(10, -20, brake=True, block=True)   
        mdiff.on_for_distance(10, 20, brake=True, block=True)


