#!/usr/bin/env python3
from configruation import *

def follow_line_1():
    tank.follow_line_1(
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
    follow_line_1()
    print("follow line complete")
    rightMotor.on_for_rotations(5, 0.075, brake=True, block=True)
    print("turn into mission complete")
    mdiff.on_for_distance(15, -18, brake=True, block=True)
    print("going forward")
    med.on_for_rotations(30, -1.15, brake=True, block=True)
    print("dropping arm")
    mdiff.on_for_distance(15, 20, brake=True, block=True)
    leftMotor.on_for_rotations(5, 0.05, brake=True, block=True)
    print("turned")
    mdiff.on_for_distance(15, 33.4, brake=True, block=True)
    leftMotor.on_for_rotations(5, -0.09, brake=True, block=True)
    med.on_for_rotations(20, 1.1, brake=True, block=True)
    print("mini boccia complete")
    sleep(2)



    mdiff.on_for_distance(15, -20, brake=True, block=True)
    leftMotor.on_for_rotations(5, 0.32, brake=True, block=True)
    med.on_for_rotations(20, 1, brake=True, block=True)
    sleep(15)
    mdiff.on_for_distance(15, -53, brake=True, block=True)
    rightMotor.on_for_rotations(5, 0.73, brake=True, block=True)
    med.on_for_rotations(15, -1.9, brake=True, block=True)
    sleep(3)
    mdiff.on_for_distance(5, -70, brake=True, block=True)
    sleep(5)
    med.on_for_rotations(50, 2, brake=True, block=True)
    sleep(2)



    mdiff.on_for_distance(20, 40, brake=True, block=True)
    rightMotor.on_for_rotations(5, 1.2, brake=True, block=True)
    mdiff.on_for_distance(20, -40, brake=True, block=True)
    rightMotor.on_for_rotations(5, 0.4, brake=True, block=True)
    mdiff.on_for_distance(20, 65, brake=True, block=True)
    leftMotor.on_for_rotations(5, 0.6, brake=True, block=True)
    mdiff.on_for_distance(20, 120, brake=True, block=True)
    rightMotor.on_for_rotations(5, -0.55, brake=True, block=True)
    mdiff.on_for_distance(10, 50, brake=True, block=True)
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


