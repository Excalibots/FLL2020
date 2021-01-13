#!/usr/bin/env pybricks-micropython
from configruation import *

def do_step_tracker():
	print ("going forward out of home")
	l=20
	r=20.1
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