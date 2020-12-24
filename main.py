#!/usr/bin/env python3

from time import sleep
from ev3dev2.sound import Sound
from ev3dev2.motor import OUTPUT_A, OUTPUT_D, LargeMotor, SpeedPercent, MoveTank, MoveDifferential, follow_for_ms
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor


#mdiff = MoveDifferential(OUTPUT_A, OUTPUT_B, EV3Tire, 16 * STUD_MM)
#mdiff = MoveDifferential()

tank = MoveTank(OUTPUT_A, OUTPUT_D)
tank.cs = ColorSensor(INPUT_3)


global l
global r
l = 0
r = 0

tank.on(left_speed=l, right_speed=r)

#tank_pair.on(left_speed=l, right_speed=r)

# Follow the line for 4500ms
def follow_line():
	tank.follow_line(
		kp=1.5, ki=0.009, kd=0.2,
		speed=SpeedPercent(10),
		follow_for=follow_for_ms,
		ms=14000,
		follow_left_edge=True,
		off_line_count_max=1000000
	)


#center of letter g in league
#28 cm


def run_one():
	print ("going forward")
	x=25
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 1.6)



	print ("going left")
	r=15
	l=0
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 0.37 )


	print ("going forward")
	x=16
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 0.55)

	print ("going right")
	r=0
	l=15
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r),0.22 )

	print ("going backward")
	x=-16
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 0.47)

	print ("going left")
	r=15
	l=-25
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r),0.48	)

	print ("going forward")
	x=16
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 1.6)

	print ("going backward")
	x=-16
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 2)

	
# #
# 	print ("going backward")s
# 	x=-30
# 	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 2.1)

# 	print ("going left")
# 	r=30
# 	l=-50
# 	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r),0.33)
	

	#turn right
	#backward

	#turn left
	#straight
	#left
	#straight into white area


run_one()

#Test Program to check sensors and motors.