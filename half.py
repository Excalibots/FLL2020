#!/usr/bin/env python3
from configruation import *

def align():
	sleep(.25)
	print("align")
	tank.stop()
	tank.on_for_degrees(SpeedPercent(-20), SpeedPercent(-20),140)
	leftBlack =  True
	rightBlack = True
	tankDegrees = 0
	leftMotor.reset()
	rightMotor.reset()
	while color2.color_name !="Black":
		tank.on(SpeedPercent(-10), SpeedPercent(10))
		tankDegrees = leftMotor.degrees
		if abs(tankDegrees) > 40:
			leftBlack = False
			tank.stop()
			break
	tank.stop()
	print(leftBlack)
	print ("back to straight")
	tankDegrees = tankDegrees * -1
	print(tankDegrees)
	leftMotor.reset()
	rightMotor.reset()
	
	if leftBlack:
		tank.on_for_degrees(SpeedPercent(-10),SpeedPercent(-10),tankDegrees*2)
		tank.on_for_degrees(SpeedPercent(10),SpeedPercent(-10),tankDegrees/1)
		tankDegrees=0
		tank.stop()
	else:
		tank.on_for_degrees(SpeedPercent(10),SpeedPercent(-10),tankDegrees/1)
		tankDegrees = 0
		leftMotor.reset()
		rightMotor.reset()
		while color2.color_name !="Black":
			print(color2.color_name)
			tank.on(SpeedPercent(10), SpeedPercent(-10))
			tankDegrees = rightMotor.degrees
			if abs(tankDegrees) > 40:
				rightBlack = False
				tank.stop()
				break
		tank.stop()
		print(rightBlack)
		if (rightBlack):
			tankDegrees = tankDegrees * -1
			leftMotor.reset()
			rightMotor.reset()
			print(tankDegrees)
			tank.on_for_degrees(SpeedPercent(-10),SpeedPercent(-10),tankDegrees*2)
			tank.on_for_degrees(SpeedPercent(-10),SpeedPercent(10),tankDegrees)
			tank.stop()

def do_step_tracker():
	# print('lift arm')
	# med.on_for_rotations(100, 2.5, brake=True, block=True)

	print ("going forward out of home")
	l=30
	r=30
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 0.95)

	print ("reach stepper and push")
	l=28
	r=30
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 4)

def go_back_from_step_tracker():

	x=-25
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), .2)
	light_intensity = color1.reflected_light_intensity
	while light_intensity < 80:
		tank.on(SpeedPercent(x), SpeedPercent(x))
		light_intensity = color1.reflected_light_intensity
		print(light_intensity)
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), .2)
	light_intensity = color1.reflected_light_intensity
	while light_intensity < 80:
		tank.on(SpeedPercent(x), SpeedPercent(x))
		light_intensity = color1.reflected_light_intensity
		print(light_intensity)
	tank.stop()
	
	print ("reach stepper and push")
	l=-10
	r=20
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), .2)

	x = -10
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), .25)
	x = 10
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), .25)
		
	print ("reach stepper")
	l=20
	r=23
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 0.8)
	print ("push stepper")
	l=35
	r=24
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 2.5)


def ready_treadmill():
	#align()
	print ("align with wall")
	l=20
	r=20
	tank.on_for_seconds(SpeedPercent(l), SpeedPercent(r), 1)
	print ("turning back to face treadmillh")
	l=-20
	r=-20
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 0.6)
	l=-20
	r=20
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 0.3)

	print ("turning")
	l=0
	r=20
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 0.3)	

	print ("getting on treadmill")
	l=20
	r=20
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 1.1)

def do_treadmill():

	sleep(0.5)
	print('running on treadmill spin one wheel')
	l=0
	r=40
	tank.on_for_seconds(SpeedPercent(l), SpeedPercent(r), 2.75)

def doRowerWithArm():
	print('running on treadmill')
	#go forward
	tank.on_for_seconds(SpeedPercent(20),SpeedPercent(20),1.5)
	#Go Forward
	tank.on_for_degrees(SpeedPercent(-20),SpeedPercent(-20),260)
	#bring the arm down
	medMotor2.on_for_seconds(SpeedPercent(-10),2)
	#move in to make sure it gets locked
	tank.on_for_degrees(SpeedPercent(2),SpeedPercent(-2),10)
	#move out to make sure it gets locked
	tank.on_for_degrees(SpeedPercent(-2),SpeedPercent(2),10)

def moveRowerArm():
	#move in to the circle
	tank.on_for_degrees(SpeedPercent(0),SpeedPercent(6),120)
	medMotor2.on_for_degrees(SpeedPercent(10),200)
	tank.on_for_degrees(SpeedPercent(2),SpeedPercent(-2),15)

def moveArmDown():
	medMotor.on_for_seconds(SpeedPercent(-100),1.5)

def doPerson():
	medMotor.on_for_seconds(SpeedPercent(-100),1.5)
	#tank.on_for_degrees(SpeedPercent(2),SpeedPercent(-2),30)
def moveArmUp():
	medMotor.on_for_seconds(SpeedPercent(100),3.5)

def goToPullUp():
	sleep(.5)
	#*Turn till white line
	while (color3.reflected_light_intensity < 40):
		tank.on(SpeedPercent(-10),SpeedPercent(10))
	tank.stop()
	#*turn till black line
	while (color3.reflected_light_intensity > 18):
		tank.on(SpeedPercent(-10),SpeedPercent(10))
	tank.stop()
	sleep(.25)
	tank.cs = ColorSensor(INPUT_3)
	tank.follow_line(
	kp=1.8, ki=0.009, kd=0,
	speed=SpeedPercent(-18),
	follow_for=follow_for_ms,
	ms=2500,
	follow_left_edge=False,
	target_light_intensity=17
	)
	while (color2.reflected_light_intensity < 40):
		tank.on(SpeedPercent(-10),SpeedPercent(-10))
	tank.stop()
	tank.on_for_degrees(SpeedPercent(-10),SpeedPercent(-10),200)
	while (color2.reflected_light_intensity < 40):
		tank.on(SpeedPercent(10),SpeedPercent(-10))
	tank.stop()
	while (color2.reflected_light_intensity > 20):
		tank.on(SpeedPercent(5),SpeedPercent(-5))
	tank.stop()	
	while (color2.reflected_light_intensity < 40):
		tank.on(SpeedPercent(5),SpeedPercent(-5))
	tank.stop()
	while (color2.reflected_light_intensity > 18):
		tank.on(SpeedPercent(-5),SpeedPercent(5))
	tank.stop()

def goUnderPullUp():
	tank.cs = ColorSensor(INPUT_2)
	tank.follow_line(
	kp=1.8, ki=0.009, kd=0,
	speed=SpeedPercent(-12),
	follow_for=follow_for_ms,
	ms=2000,
	follow_left_edge=False,
	target_light_intensity=17
	)	
	tank.follow_line(
	kp=1.8, ki=0.009, kd=0,
	speed=SpeedPercent(-18),
	follow_for=follow_for_ms,
	ms=1000,
	follow_left_edge=False,
	target_light_intensity=17
	)
	tank.on_for_degrees(SpeedPercent(-25),SpeedPercent(25),70) 
	tank.on_for_degrees(SpeedPercent(-35),SpeedPercent(-35),450)

def doDanceNew():
	counter = 1
	while (counter < 12):
		counter = counter + 1
		tank.on_for_degrees(SpeedPercent(-15),SpeedPercent(15),100) 
		tank.on_for_degrees(SpeedPercent(15),SpeedPercent(-15),100) 


def test():
	sound.speak("v4 Victory is I")
	sound.speak("excalibots are fly")
	sound.play_song((
	('D4', 'e3'),      # intro anacrouse
	('D4', 'e3'),
	('D4', 'e3'),
	('G4', 'h'),       # meas 1
	('D5', 'h'),
	('C5', 'e3'),      # meas 2
	('B4', 'e3'),
	('A4', 'e3'),
	('G5', 'h'),
	('D5', 'q')))

def back_from_treadmill():
	
	print('getting down from treadmilll')
	l=0
	r=-20
	tank.on_for_seconds(SpeedPercent(l), SpeedPercent(r), 0.3)

	x=-20
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x),0.75)
	# print(color1.color_name)
	# while color1.color_name !="Black":
	# 	tank.on(SpeedPercent(x), SpeedPercent(x))
	# tank.stop()

	tank.on_for_degrees(SpeedPercent(20), SpeedPercent(-20),110)

	tank.on_for_degrees(SpeedPercent(20), SpeedPercent(20),400)

def do_rower():
	# align()
	tank.on_for_seconds(SpeedPercent(20),SpeedPercent(20),2.5)
	#nirav's version of doing the rower

	print("go forward")
	tank.on_for_degrees(SpeedPercent(-20), SpeedPercent(-15),500)
	tank.on_for_degrees(SpeedPercent(5), SpeedPercent(-25),94)
	tank.on_for_degrees(SpeedPercent(5), SpeedPercent(-20),85)
	print("turn to the rower")
	tank.on_for_degrees(SpeedPercent(20), SpeedPercent(-20),90)
	tank.on_for_seconds(SpeedPercent(-10), SpeedPercent(-10),1.7)
	tank.on_for_seconds(SpeedPercent(10), SpeedPercent(10),2.1)
	tank.on_for_degrees(SpeedPercent(-18), SpeedPercent(5),30)
	tank.on_for_degrees(SpeedPercent(10), SpeedPercent(0),10)
	tank.on_for_degrees(SpeedPercent(30), SpeedPercent(30),60)
	tank.on_for_degrees(SpeedPercent(10), SpeedPercent(15),30)
	tank.on_for_degrees(SpeedPercent(-10), SpeedPercent(10),50)
	tank.on_for_degrees(SpeedPercent(-10), SpeedPercent(-10),10)
	#end nirav's version of doing the rower

def Going_Weight():
	print('going to Weight Machine')
	tank.on_for_degrees(SpeedPercent(-20), SpeedPercent(20),80)
	tank.on_for_degrees(SpeedPercent(-20), SpeedPercent(-20),390)
	tank.on_for_degrees(SpeedPercent(-20), SpeedPercent(20),165)
	tank.on_for_seconds(SpeedPercent(20), SpeedPercent(20),3)

	#tank.on_for_seconds(SpeedPercent(-20), SpeedPercent(-5),2)

def forklift():
	medMotor.on_for_degrees(SpeedPercent(100),250)
	medMotor.stop()

def forklift_down():
	medMotor.on_for_degrees(SpeedPercent(-100),250)
	medMotor.stop()


def go_back_from_step_tracker2():

	x=-25
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), .2)
	light_intensity = color1.reflected_light_intensity
	while light_intensity < 80:
		tank.on(SpeedPercent(x), SpeedPercent(x))
		light_intensity = color1.reflected_light_intensity
		print(light_intensity)
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), .2)
	light_intensity = color1.reflected_light_intensity
	while light_intensity < 80:
		tank.on(SpeedPercent(x), SpeedPercent(x))
		light_intensity = color1.reflected_light_intensity
		print(light_intensity)
	tank.stop()
	sleep(.5)
	print ("reach stepper and push")
	l=-10
	r=20
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), .2)

	x = -10
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), .25)
	x = 10
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 1.25)
	tank.on_for_degrees(SpeedPercent(-10), SpeedPercent(10), 45)

