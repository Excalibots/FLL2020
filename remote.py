#!/usr/bin/env python3

from time import sleep
from ev3dev2.sound import Sound
from ev3dev2.motor import OUTPUT_A, OUTPUT_D, LargeMotor, SpeedPercent, MoveTank, MoveDifferential
from ev3dev2.wheel import EV3Tire
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4

import termios
import tty
import sys
from ev3dev2.sensor.lego import ColorSensor


mdiff = MoveDifferential(OUTPUT_A, OUTPUT_B, EV3Tire, 16 * STUD_MM)
mdiff = MoveDifferential()



tank = MoveTank(OUTPUT_A, OUTPUT_D)
tank.cs = ColorSensor(INPUT_2)
sound = Sound()
global l
global r
l = 0
r = 0
global steering_angle
steering_angle = 0
sound.speak("AVENGERRRRRR")
i = 1
d = 1
global robot 

def getch():
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(fd)
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings) 
	return ch



def going_forward():
	print ("going forward")
	global l
	global r
	x=10
	l=x
	r=x
	x=x+1
def going_backward():
	print ("going back")
	global l
	global r
	l = -10
	r = -10
def going_left():
	print ("going forward")
	global l
	global r
	l=-5
	r=5
def going_right():
	print ("going forward")
	global l
	global r
	l=5
	r=-5

"""
def line_following():
	print ("line following")
	global l
	global r
	line_sensor = ColorSensor(Port.S3)
	global robot
	BLACK = 9
	WHITE = 85
	threshold = (BLACK + WHITE) / 2
	DRIVE_SPEED = 20
	PROPORTIONAL_GAIN = 1.2
	deviation = line_sensor.reflection() - threshold
	turn_rate = PROPORTIONAL_GAIN * deviation
	robot.drive(DRIVE_SPEED, turn_rate)
"""
def stop():
	print ("Stop")
	global l
	global r
	l = 0
	r = 0


while True:
	k = getch() 
	if k == "w":
		going_forward()

	if k =="s":
		going_backward()
	if k =="a":
		going_left()
	if k =="d":
		going_right()
	if k=="x":
		stop()
	#if k== "l":
	#	line_following()

	tank_pair.on(left_speed=l, right_speed=r)
