#!/usr/bin/env python3


from configruation import *



def PushSlideBox():
	medMotor.on_for_degrees(SpeedPercent(35),30)
	tank.on_for_degrees(SpeedPercent(-20),SpeedPercent(-20),320)
	FollowLineToSlide(-10,2000)
	tank.on_for_degrees(SpeedPercent(-20),SpeedPercent(-20),160)

def GoBackFromSlide():
	print(color2.color_name)
	while color2.reflected_light_intensity < 49:
		print(color2.reflected_light_intensity)
		tank.on(SpeedPercent(15),SpeedPercent(15))
	tank.stop()
	tank.on_for_degrees(SpeedPercent(-15),SpeedPercent(15),90)


def GoToBoccia():
	FollowLineToSlide(-15, 3000)
	tank.on_for_degrees(SpeedPercent(-5),SpeedPercent(-5),80)

def goTOframe():
	tank.on_for_degrees(SpeedPercent(20),SpeedPercent(20),140)
	tank.on_for_degrees(SpeedPercent(20),SpeedPercent(-20),200)
	tank.on_for_degrees(SpeedPercent(-20),SpeedPercent(-20),200)
	while color2.reflected_light_intensity < 45:
		print(color2.reflected_light_intensity)
		tank.on(SpeedPercent(-15),SpeedPercent(-15))
	tank.stop()

def DropBlocks():
	tank.on_for_degrees(SpeedPercent(-25),SpeedPercent(-25),30)
	medMotor.on_for_degrees(SpeedPercent(20),380)


def GoToMiniBoccia():
	medMotor.on_for_degrees(SpeedPercent(-25),120)
	tank.on_for_degrees(SpeedPercent(10),SpeedPercent(-10),100)
	tank.on_for_degrees(SpeedPercent(-12),SpeedPercent(-12),140)
	tank.on_for_degrees(SpeedPercent(-12),SpeedPercent(11),60)
	medMotor.on_for_degrees(SpeedPercent(-35),40)

def goingtoweightmachine():
	tank.on_for_degrees(SpeedPercent(20),SpeedPercent(20),180)

	medMotor.on_for_degrees(SpeedPercent(-100),120)

	tank.on_for_degrees(SpeedPercent(-20),SpeedPercent(-20),180)


	while color2.reflected_light_intensity > 30:
		print(color2.reflected_light_intensity)
		tank.on(SpeedPercent(-15),SpeedPercent(-15))
	tank.stop()

	tank.cs = ColorSensor(INPUT_2)
	tank.follow_line(
	kp=1.8, ki=0.009, kd=0,
	speed=SpeedPercent(12),
	follow_for=follow_for_ms,
	ms=3,
	follow_left_edge=True,
	target_light_intensity=17)

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