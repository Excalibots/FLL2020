#!/usr/bin/env python3


from configruation import *
from threading import Thread

def PushSlideBox():
	#move forward until it clears home
	tank.on_for_degrees(SpeedPercent(-20),SpeedPercent(-20),220)
	#follow line for 1700 ms
	FollowLineToSlide(-18,1700)
	#move forward till the slidebox
	tank.on_for_degrees(SpeedPercent(-20),SpeedPercent(-20),160)

def GoBackFromSlide():
	#go back from slide till color 2 hits white
	print(color2.color_name)
	while color2.reflected_light_intensity < 45:
		print(color2.reflected_light_intensity)
		tank.on(SpeedPercent(15),SpeedPercent(15))
	tank.stop()
	#turn 90 degrees to face the boccia
	tank.on_for_degrees(SpeedPercent(-15),SpeedPercent(15),90)


def GoToBoccia():
	#follow line and go to boccia
	FollowLineToSlide(-15, 3000)
	#go slowly forward so taht the blue block is dropped and not the red one
	tank.on_for_degrees(SpeedPercent(-5),SpeedPercent(-5),80)

def goTOframe():
	#! go back till color3 sees whiteline
	while color3.reflected_light_intensity < 45:
		print(color2.reflected_light_intensity)
		tank.on(SpeedPercent(15),SpeedPercent(15))
	tank.stop()
	# Go to Frame
	#turn so that color 3 is not on white
	tank.on_for_degrees(SpeedPercent(10),SpeedPercent(-10),45)
	#turn till color3 sees white
	while color3.reflected_light_intensity < 45:
		tank.on(SpeedPercent(10),SpeedPercent(-10))
	tank.stop()
	# turn till color 3 sees black
	while color3.reflected_light_intensity > 17:
		tank.on(SpeedPercent(10),SpeedPercent(-10))
	tank.stop()
	# turn till color 3 sees white
	while color3.reflected_light_intensity < 40:
		tank.on(SpeedPercent(10),SpeedPercent(-10))
	tank.stop()	
	tank.on_for_degrees(SpeedPercent(10),SpeedPercent(-10),15)
	#move forward before looking for black line
	tank.on_for_degrees(SpeedPercent(-10),SpeedPercent(-10),45)
	#look for black line
	sleep(.25)
	print("find white line after green triangle before going to the black line")
	print(color2.reflected_light_intensity)
	#move forward till white
	while color2.reflected_light_intensity < 30:
		print(color2.reflected_light_intensity)
		tank.on(SpeedPercent(-7),SpeedPercent(-7))
	tank.stop()	
	print("finding black after green triangle...this number changes night versus")
	print(color2.reflected_light_intensity)
	#move forward till black
	while color2.reflected_light_intensity > 11:
		print(color2.reflected_light_intensity)
		tank.on(SpeedPercent(-7),SpeedPercent(-7))
	tank.stop()
	print("found black line")
	#turn till it sees black/white line
	print("turn till you see black/white line")
	print(color2.reflected_light_intensity)
	#turm till the black/white line intersection so that the robot can travel on the line
	while color2.reflected_light_intensity <  32:
		print(color2.reflected_light_intensity)
		tank.on(SpeedPercent(-5),SpeedPercent(5))
	tank.stop()
	print("found black/white line")
	#followline for 3500 ms
	FollowLineToSlide(-5,3500)
	tank.stop()
	#turn till it sees black/white line
	while color2.reflected_light_intensity >  20:
		tank.on(SpeedPercent(5),SpeedPercent(-5))
	tank.stop()
	#start lowering the blocks while going to the frame
	t = Thread(target=medMotor.on_for_degrees, args=(SpeedPercent(-100),2000,))
	t.start()
	#go to the frame
	FollowLineToSlide(-10,2000)
	tank.stop()

def DropBlocks():
	# Turn to the frame
	tank.on_for_degrees(SpeedPercent(-10),SpeedPercent(10),50)
	tank.on_for_degrees(SpeedPercent(-10),SpeedPercent(-10),50)
	#drop the blocks
	medMotor.on_for_degrees(SpeedPercent(-100),1200)
	medMotor.stop()
	#lift the arm up again while turning away from the frame
	t = Thread(target=medMotor.on_for_degrees, args=(SpeedPercent(100),850,))
	t.start()
	#medMotor.on_for_degrees(SpeedPercent(100),850)
	tank.on_for_degrees(SpeedPercent(10),SpeedPercent(10),50)
	tank.on_for_degrees(SpeedPercent(10),SpeedPercent(-10),50)
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
	tank.on_for_degrees(SpeedPercent(-10),SpeedPercent(10),44)
	#lift arm to push the boccia block in to the frame/target
	medMotor.on_for_degrees(SpeedPercent(100),900)
	#sleep(.5)	#tank.on_for_degrees(SpeedPercent(10),SpeedPercent(10),140)


def goingtoweightmachine():
	#medMotor.on_for_degrees(SpeedPercent(20),150)

	medMotor.on_for_degrees(SpeedPercent(100),1620)
	#! adding this because the robot is on the other side of the white line
	# turn to the white line
	while color2.reflected_light_intensity < 40:
			tank.on(SpeedPercent(-7),SpeedPercent(7))
	tank.stop()
	#turn to black
	while color2.reflected_light_intensity > 10:
			tank.on(SpeedPercent(-7),SpeedPercent(7))
	tank.stop()
	#turn to black/white so that the light sensor is on black/white
	#and ready to follow line 
	while color2.reflected_light_intensity < 20:
			tank.on(SpeedPercent(-7),SpeedPercent(7))
	tank.stop()
	#follow line to the weights
	FollowLineToSlide(-15,5000)

def newHopScotch():
	tank.on_for_degrees(SpeedPercent(-10),SpeedPercent(-12),400)
	sleep(0.5)
	tank.on_for_degrees(SpeedPercent(-10),SpeedPercent(-12),168)
	sleep(0.5)
	tank.on_for_degrees(SpeedPercent(30),SpeedPercent(30),1000)


def doWeights():
	#turn away from the weight machine to lower the arm
	tank.on_for_degrees(SpeedPercent(10),SpeedPercent(-10),55)
	#lower the arm
	medMotor.on_for_rotations(SpeedPercent(-100),8)
	#turn to the weight machine
	tank.on_for_degrees(SpeedPercent(-10),SpeedPercent(10),52)
	#lift the arm up
	medMotor.on_for_rotations(SpeedPercent(100),6.5)
	#lower the arm so that the weight is off of the arm
	medMotor.on_for_rotations(SpeedPercent(-100),3)
	#move away from the weight machine so that the arm is free of the weight machine
	tank.on_for_degrees(SpeedPercent(10),SpeedPercent(-10),40)
	#FollowLineToSlide(15,5200)



def GoBackFromWeight():
	#lift arm up
	medMotor.on_for_rotations(SpeedPercent(100),4.5)
	#turn so that the robot is kind of parallel to the wall
	tank.on_for_degrees(SpeedPercent(-10),SpeedPercent(10),25)
	print('going back from weight machine')
	#set left black and right black variables to true
	leftBlack =  True
	rightBlack = True
	tankDegrees = 0
	leftMotor.reset()
	rightMotor.reset()
	#Robot could be on th eleft side of the black line or right side of the black line
	#if it is on th left side
	#When the robot turns it will find the black line
	while color1.reflected_light_intensity > 30:
		tank.on(SpeedPercent(-10), SpeedPercent(10))
		tankDegrees = leftMotor.degrees
		#if the robot turned more than 45 degrees and didn't see the black line then 
		# that means the robot is on the other side of the black line
		if abs(tankDegrees) > 45:
			leftBlack = False
			tank.stop()
			break
	tank.stop()
	#If the robot was not on the left side
	#do the same and find the black line on the other side
	if (not leftBlack):
		tank.on_for_degrees(SpeedPercent(10),SpeedPercent(-10),abs(tankDegrees))
		leftMotor.reset()
		while color1.reflected_light_intensity > 30:
			tank.on(SpeedPercent(10), SpeedPercent(-10))
			tankDegrees = leftMotor.degrees
			if abs(tankDegrees) > 45:
				tank.stop()
				break
		tank.stop()	
	#go to slide
	#! speed this part to save save time
	FollowLineC1(7,9750)
	#FollowLineC1(10,5750)

	#*turning to face slide while lowering the arm
	t3 = Thread(target=medMotor.on_for_rotations, args=(SpeedPercent(100),-7.1,))
	t3.start()
	sleep(.25)
	#turn to be right under the slide figures
	tank.on_for_degrees(SpeedPercent(20),SpeedPercent(0),500)
	#move to be right at the edge of the slide figures
	tank.on_for_degrees(SpeedPercent(-15),SpeedPercent(-15),40)
	tank.stop()
	sleep(.5)
	tank.on_for_degrees(SpeedPercent(10),SpeedPercent(10),20)

def DoSlide():
	#move till the arm moves up
	tank.on_for_degrees(SpeedPercent(-7),SpeedPercent(-7),200)
	# go back
	tank.on_for_degrees(SpeedPercent(20),SpeedPercent(20),80)
	#turn to be away from the frame
	tank.on_for_degrees(SpeedPercent(20),SpeedPercent(-20),50)
	tank.on_for_degrees(SpeedPercent(20),SpeedPercent(20),80)
	medMotor.on_for_rotations(SpeedPercent(100),-3)
	#tank.on_for_degrees(SpeedPercent(10),SpeedPercent(10),100)
	tank.on_for_degrees(SpeedPercent(-20),SpeedPercent(20),75)
	#sleep(5)
	tank.on_for_degrees(SpeedPercent(-10),SpeedPercent(-10),100)
	tank.on_for_degrees(SpeedPercent(-40),SpeedPercent(	-40),1300)

def moveForward():
	tank.on_for_degrees(SpeedPercent(-3),SpeedPercent(-3),150)
	tank.stop()		

def FollowLineToSlide(speed,time):
	#line follower function 
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
	#line follower function 
	tank.cs = ColorSensor(INPUT_1)
	tank.follow_line(
	kp=1.8, ki=0.009, kd=0,
	speed=SpeedPercent(speed),
	follow_for=follow_for_ms,
	ms=time,
	follow_left_edge=False,
	target_light_intensity=50
	)

def moveArm():
	sleep(.35)
	medMotor.on_for_rotations(SpeedPercent(60),3.5)

def threadTest():
		t3 = Thread(target=medMotor.on_for_degrees, args=(SpeedPercent(-100),2000,))
		t3.start()
		tank.on_for_degrees(SpeedPercent(10),SpeedPercent(10),400)