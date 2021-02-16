#!/usr/bin/env python3


from configruation import *
from threading import Thread

def test123():
	FollowLineToSlide(-15,1000)
	tank.on_for_degrees(SpeedPercent(-20),SpeedPercent(-20),60)
	FollowLineToSlide(-15,7000)

def PushSlideBox():
	tank.on_for_degrees(SpeedPercent(-20),SpeedPercent(-20),220)
	FollowLineToSlide(-12,2200)
	tank.on_for_degrees(SpeedPercent(-20),SpeedPercent(-20),160)

def GoBackFromSlide():
	print(color2.color_name)
	while color2.reflected_light_intensity < 45:
		print(color2.reflected_light_intensity)
		tank.on(SpeedPercent(15),SpeedPercent(15))
	tank.stop()
	tank.on_for_degrees(SpeedPercent(-15),SpeedPercent(15),90)


def GoToBoccia():
	FollowLineToSlide(-15, 3000)
	tank.on_for_degrees(SpeedPercent(-5),SpeedPercent(-5),80)

def goTOframe():
	#! Go Back
	while color3.reflected_light_intensity < 45:
		print(color2.reflected_light_intensity)
		tank.on(SpeedPercent(15),SpeedPercent(15))
	tank.stop()
	#tank.on_for_degrees(SpeedPercent(20),SpeedPercent(20),140)
	# turn to Frame
	#tank.on_for_degrees(SpeedPercent(20),SpeedPercent(-20),140)
	# Go to Frame
	#turn so that color 3 is not on white
	tank.on_for_degrees(SpeedPercent(10),SpeedPercent(-10),45)
	#turn till color3 sees white
	while color3.reflected_light_intensity < 45:
		tank.on(SpeedPercent(10),SpeedPercent(-10))
	tank.stop()
	# turn till color 3 sees black
	while color3.reflected_light_intensity > 20:
		tank.on(SpeedPercent(10),SpeedPercent(-10))
	tank.stop()
	# turn till color 3 sees white
	while color3.reflected_light_intensity < 45:
		tank.on(SpeedPercent(10),SpeedPercent(-10))
	tank.stop()	
	tank.on_for_degrees(SpeedPercent(10),SpeedPercent(-10),15)
	#move forward before looking for black line
	tank.on_for_degrees(SpeedPercent(-20),SpeedPercent(-20),45)
	#look for black line
	sleep(.25)
	print("find white line after green triangle before going to the black line")
	print(color2.reflected_light_intensity)
	while color2.reflected_light_intensity < 30:
		print(color2.reflected_light_intensity)
		tank.on(SpeedPercent(-7),SpeedPercent(-7))
	tank.stop()	
	print("finding black after green triangle...this number changes night versus")
	print(color2.reflected_light_intensity)
	while color2.reflected_light_intensity > 11:
		print(color2.reflected_light_intensity)
		tank.on(SpeedPercent(-7),SpeedPercent(-7))
	tank.stop()
	print("found black line")
	#turn till it sees black/white line
	print("turn till you see black/white line")
	print(color2.reflected_light_intensity)
	while color2.reflected_light_intensity <  32:
		print(color2.reflected_light_intensity)
		tank.on(SpeedPercent(-5),SpeedPercent(5))
	tank.stop()
	print("found black/white line")
	FollowLineToSlide(-5,3500)
	tank.stop()
	#turn till it sees black/white line
	while color2.reflected_light_intensity >  20:
		tank.on(SpeedPercent(5),SpeedPercent(-5))
	tank.stop()
	FollowLineToSlide(-10,2000)
	tank.stop()
def DropBlocks():
	# Turn to the frame
	tank.on_for_degrees(SpeedPercent(-10),SpeedPercent(10),45)
	tank.on_for_degrees(SpeedPercent(-10),SpeedPercent(-10),45)
	#drop the blocks
	medMotor.on_for_degrees(SpeedPercent(-100),3200)
	medMotor.stop()
	sleep(.25)
	#lift the arm up again
	medMotor.on_for_degrees(SpeedPercent(100),850)
	tank.on_for_degrees(SpeedPercent(10),SpeedPercent(10),45)
	tank.on_for_degrees(SpeedPercent(10),SpeedPercent(-10),45)
	medMotor.stop()


def GoToMiniBoccia():
	#move forward
	tank.on_for_degrees(SpeedPercent(10),SpeedPercent(10),30)
	#turn toward the boccia
	tank.on_for_degrees(SpeedPercent(10),SpeedPercent(-10),37)

	#move forward and push the boccia to face the target
	tank.on_for_degrees(SpeedPercent(-7),SpeedPercent(-7),170)

	#move away from boccia to clear the boccia before moving forward
	tank.on_for_degrees(SpeedPercent(10),SpeedPercent(-10),10)
	#move foward so that the robot is on the other side of the boccia
	tank.on_for_degrees(SpeedPercent(-10),SpeedPercent(-10),30)
	#turn inwards to have the arm be read to move the Boccia up
	tank.on_for_degrees(SpeedPercent(-10),SpeedPercent(10),47)
	#lift arm to push the boccia block in to the frame/target
	medMotor.on_for_degrees(SpeedPercent(100),900)
	#sleep(.5)	#tank.on_for_degrees(SpeedPercent(10),SpeedPercent(10),140)


def goingtoweightmachine():
	#medMotor.on_for_degrees(SpeedPercent(20),150)

	medMotor.on_for_degrees(SpeedPercent(100),1620)
	while color2.reflected_light_intensity > 10:
			tank.on(SpeedPercent(-7),SpeedPercent(7))
	tank.stop()
	while color2.reflected_light_intensity < 20:
			tank.on(SpeedPercent(-7),SpeedPercent(7))
	tank.stop()
	FollowLineToSlide(-15,5000)

def newHopScotch():
	tank.on_for_degrees(SpeedPercent(-16),SpeedPercent(-18),400)
	tank.on_for_degrees(SpeedPercent(-10),SpeedPercent(-12),150)
	tank.on_for_degrees(SpeedPercent(50),SpeedPercent(50),1000)


def doWeights():
	tank.on_for_degrees(SpeedPercent(10),SpeedPercent(-10),55)
	medMotor.on_for_rotations(SpeedPercent(-100),8)
	tank.on_for_degrees(SpeedPercent(-10),SpeedPercent(10),60)
	medMotor.on_for_rotations(SpeedPercent(100),6.5)
	medMotor.on_for_rotations(SpeedPercent(-100),3)
	tank.on_for_degrees(SpeedPercent(10),SpeedPercent(-10),55)
	#FollowLineToSlide(15,5200)



def GoBackFromWeight():
	# medMotor.on_for_rotations(SpeedPercent(100),5)
	# tank.on_for_degrees(SpeedPercent(-10),SpeedPercent(10),25)
	# print('going back from weight machine')
	# leftBlack =  True
	# rightBlack = True
	# tankDegrees = 0
	# leftMotor.reset()
	# rightMotor.reset()
	# while color1.reflected_light_intensity > 15:
	# 	tank.on(SpeedPercent(-10), SpeedPercent(10))
	# 	tankDegrees = leftMotor.degrees
	# 	if abs(tankDegrees) > 45:
	# 		leftBlack = False
	# 		tank.stop()
	# 		break
	# tank.stop()
	# if (not leftBlack):
	# 	tank.on_for_degrees(SpeedPercent(10),SpeedPercent(-10),abs(tankDegrees))
	# 	leftMotor.reset()
	# 	while color1.reflected_light_intensity > 15:
	# 		tank.on(SpeedPercent(10), SpeedPercent(-10))
	# 		tankDegrees = leftMotor.degrees
	# 		if abs(tankDegrees) > 45:
	# 			tank.stop()
	# 			break
	# 	tank.stop()	
	# FollowLineC1(5,3000)
	# FollowLineC1(10,6500)
	tank.on_for_degrees(SpeedPercent(20),SpeedPercent(0),500)
	tank.on_for_degrees(SpeedPercent(15),SpeedPercent(15),40)
	medMotor.on_for_rotations(SpeedPercent(100),-6.5)
	tank.on_for_degrees(SpeedPercent(-15),SpeedPercent(-15),90)
	tank.on_for_degrees(SpeedPercent(10),SpeedPercent(10),15)
	# medMotor.on_for_rotations(SpeedPercent(100),10)

def DoSlide():
	#move till the arm moves up
	tank.on_for_degrees(SpeedPercent(-5),SpeedPercent(-5),200)
	# go back
	tank.on_for_degrees(SpeedPercent(20),SpeedPercent(20),100)
	#turn to be away from the frame
	tank.on_for_degrees(SpeedPercent(20),SpeedPercent(-20),100)
	medMotor.on_for_rotations(SpeedPercent(100),-4)
	tank.on_for_degrees(SpeedPercent(-20),SpeedPercent(	20),100)


	#medMotor.on_for_rotations(SpeedPercent(100),-2)
	# tank.on_for_degrees(SpeedPercent(20),SpeedPercent(0),100)
	# #tank.on_for_degrees(SpeedPercent(-10),SpeedPercent(-10),25)
	# medMotor.on_for_rotations(SpeedPercent(100),2)
	# sleep(3)
	# tank.on_for_degrees(SpeedPercent(-20),SpeedPercent(-20),100)
	# tank.on_for_degrees(SpeedPercent(0),SpeedPercent(20),100)
	# tank.on_for_degrees(SpeedPercent(-20),SpeedPercent(-20),1000)

def moveForward():
	tank.on_for_degrees(SpeedPercent(-5),SpeedPercent(-5),200)
	tank.stop()		

def FollowLineToSlide(speed,time):
	tank.cs = ColorSensor(INPUT_2)
	tank.follow_line(
	kp=1.8, ki=0.009, kd=0,
	speed=SpeedPercent(speed),
	follow_for=follow_for_ms,
	ms=time,
	follow_left_edge=True,
	target_light_intensity=17
	)

def FollowLineC1(speed,time):
	tank.cs = ColorSensor(INPUT_1)
	tank.follow_line(
	kp=1.8, ki=0.009, kd=0,
	speed=SpeedPercent(speed),
	follow_for=follow_for_ms,
	ms=time,
	follow_left_edge=False,
	target_light_intensity=17
	)

def moveArm():
	sleep(0.5)
	medMotor.on_for_rotations(SpeedPercent(65),3.5)