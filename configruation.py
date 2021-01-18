#!/usr/bin/env python3

from time import sleep
from ev3dev2.sound import Sound
from ev3dev2.motor import OUTPUT_A, OUTPUT_D, OUTPUT_B, LargeMotor, MediumMotor, SpeedPercent, MoveTank, MoveDifferential, follow_for_ms
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor
import ev3dev2
from ev3dev2.wheel import EV3Tire

STUD_MM = 8
mdiff = MoveDifferential(OUTPUT_A, OUTPUT_D, EV3Tire, 16 * STUD_MM)
tank = MoveTank(OUTPUT_A, OUTPUT_D)
leftMotor = LargeMotor(OUTPUT_A)
rightMotor = LargeMotor(OUTPUT_D)
tank.cs = ColorSensor(INPUT_3)
color1 = ColorSensor(INPUT_1)
color2 = ColorSensor(INPUT_2)
color3 = ColorSensor(INPUT_3)
color4 = ColorSensor(INPUT_4)
med = MediumMotor(OUTPUT_B)



