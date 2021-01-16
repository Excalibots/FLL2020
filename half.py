#!/usr/bin/env pybricks-micropython
from configruation import *

def do_step_tracker():
 	print ("going forward out of home")
 	l=30
 	r=30
 	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 0.95)

 	print ("reach stepper and push")
 	l=28
 	r=30
 	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 4)


def go_back_from_step_tracker():

 	x=-20
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

 	print ("reach stepper and push")
 	l=20
 	r=23
 	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 0.8)
	
 	print ("reach stepper and push")
 	l=32
 	r=20
 	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 3)

 	print ("reach stepper and push")
 	l=-21
 	r=-10
 	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 1.2)

 	print ("reach stepper and push")
 	l=1
 	r=8
 	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 0.1)

 	print ("reach stepper and push")
 	l=20
 	r=20
 	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 1.0)

 	print ("reach stepper and push")
 	l=0
 	r=20
 	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 2.0)


def do_rower():
	print("align")
	while color2.color_name != "White":
		print(color2.color_name)
		tank.on(SpeedPercent(-20), SpeedPercent(-20))
		print(color2.color_name)
	tank.stop()
	tank.on_for_degrees(SpeedPercent(-20), SpeedPercent(-20),120)
	leftBlack =  True
	rightBlack = True
	tankDegrees = 0
	leftMotor.reset()
	rightMotor.reset()
	while color2.color_name !="Black":
		tank.on(SpeedPercent(-10), SpeedPercent(0))
		tankDegrees = leftMotor.degrees
		if abs(tankDegrees) > 75:
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
		tank.on_for_degrees(SpeedPercent(10),SpeedPercent(-10),tankDegrees/2)
		tankDegrees=0
		tank.stop()
	else:
		tank.on_for_degrees(SpeedPercent(10),SpeedPercent(-10),tankDegrees/2)
		sleep(1)
		tankDegrees = 0
		leftMotor.reset()
		rightMotor.reset()
		while color2.color_name !="Black":
			print(color2.color_name)
			tank.on(SpeedPercent(0), SpeedPercent(-10))
			tankDegrees = rightMotor.degrees
			if abs(tankDegrees) > 75:
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
			sleep(.5)
			tank.on_for_degrees(SpeedPercent(-10),SpeedPercent(-10),tankDegrees*2)
			tank.on_for_degrees(SpeedPercent(-10),SpeedPercent(10),tankDegrees/2)
			tank.stop()
	tank.on_for_seconds(SpeedPercent(20),SpeedPercent(20),2.5)
	#nirav's version of doing the rower
	print("go forward")
	tank.on_for_degrees(SpeedPercent(-30), SpeedPercent(-20),500)
	tank.on_for_degrees(SpeedPercent(15), SpeedPercent(-35),94)
	tank.on_for_degrees(SpeedPercent(5), SpeedPercent(-20),85)
	print("turn to the rower")
	tank.on_for_degrees(SpeedPercent(20), SpeedPercent(-20),100)
	tank.on_for_seconds(SpeedPercent(-10), SpeedPercent(-10),2.1)
	tank.on_for_seconds(SpeedPercent(10), SpeedPercent(10),1.7)
	tank.on_for_degrees(SpeedPercent(-20), SpeedPercent(0),40)
	tank.on_for_degrees(SpeedPercent(10), SpeedPercent(10),90)

	#end nirav's version of doing the rower
