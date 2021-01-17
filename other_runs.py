
#!/usr/bin/env python3


from configruation import *

global l
global r
l = 0
r = 0

tank.on(left_speed=l, right_speed=r)

#tank_pair.on(left_speed=l, right_speed=r)

# Follow the line for 4500ms
def follow_line():
	tank.follow_line(
		kp=2.85, ki=0.005, kd=0.02,
		speed=SpeedPercent(-10),
		follow_for=follow_for_ms,
		ms=65,
		follow_left_edge=True,
		off_line_count_max=1000000,
		sleep_time=0.005,
		target_light_intensity=30
	)
	


#center of letter g in league
#28 cm


def run_one():
	print ("going forward")
	x=25
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 1.63)


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
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 0.17)

	sleep(0.25)

	print ("going forward")
	x=16
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 0.09)

	print ("going backward")
	x=-16
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 0.4)


	print ("going left")
	r=30
	l=-1
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 1.7 )

	print ("going left")
	r=-1
	l=-30
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 0.59 )


	print ("going backward")
	x=-10
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 0.14)

	print ("going backward")

	x=16
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 0.5)

	print ("going left")
	r=-30
	l=0
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 0.3 )

	print ("going backward")

	x=16
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 0.5)


# run_one()

def run_two():
	print ("going backward")
	x=-25
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 1.63)

	print ("going right")
	l=-30
	r=10
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 0.35)

	print ("going right")
	r=-30
	l=-1
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 1 )

	print ("going forward")
	x=10
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 1)

	print ("going forward")
	x=40
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 2
	)


# run_two()


	
# # TOP LEFT = PORT 1
# # TOP RIGHT = PORT 4
# # BOTTOM LEFT = PORT 2
# # BOTTOM RIGHT = PORT 3
	
# # #
# # 	print ("going backward")s
# # 	x=-30
# # 	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 2.1)

# # 	print ("going left")
# # 	r=30
# # 	l=-50
# # 	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r),0.33)
	

# 	#turn right
# 	#backward

# 	#turn left
# 	#straight 
# 	#left
# 	#straight into white area

# run_one()

# # follow_line()


# #Test Program to check sensors and motors.

def run_half():

	print ("going forward out of home")
	l=20
	r=20.1
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 0.95)

	print ("reach stepper and push")
	l=28
	r=30
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 4)

	# ORIGINAL CODE TO COME BACK
	# print ("going forward")
	# l=-30
	# r=-20
	# tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 0.7)
	
	

	# print ("going forward")
	# l=0
	# r=25
	# tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 0.3)
	
	# print ("going forward")
	# l=10
	# r=15
	# tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 0.5)
 
	# tank.follow_line(
	# 	kp=3.00, ki=0.005, kd=0.02,
	# 	speed=SpeedPercent(10),
	# 	follow_for=follow_for_ms,
	# 	ms=4000,
	# 	follow_left_edge=False,
	# 	off_line_count_max=1000000,
	# 	sleep_time=0.005,
	# 	target_light_intensity=10
	# )

	# print ("going forward")
	# l=30
	# r=20

	# tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 4.0)

	
	# print ("going forward")
	# l=-30
	# r=-8
	# tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 1.4)

	# print ("going forward")
	# x=30
	# tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 1.5)

	# print ("going forward")
	# l=0
	# r=30
	# tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 3)

	# print ("going forward")
	# l=-20
	# r=-20
	# tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 1)

	# print ("going forward")
	# l=30
	# r=0
	# tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 0.9)

	# print ("going forward")
	# l=30
	# r=40
	# tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 1.0)

	# Row_Machine_Final()
	
#run_half()

def Weight():
	#ev3dev2.motor.on_for_rotations(SpeedPercent(x) 0.55)
	m = MediumMotor('outC')

	m.run_timed(time_sp=3000, speed_sp=-1500)
	sleep(1)
	m.run_timed(time_sp=3000, speed_sp=3000)

def Row_Machine():

	print ("going forward")
	x=-16
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 0.7)

	print ("going right")
	r=-25
	l=5
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r),0.38 )

	print ("going forward")
	x=-16
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 0.35)

	print ("going forward")
	x=-10
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 0.16)

	print ("going forward")
	x=10
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 0.31)

	print ("going right")
	r=-15
	l=3
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r),-0.1 )

	print ("going right")
	r=10
	l=0
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r),-0.1 )

	print ("going right")
	r=-15
	l=3
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r),-0.28 )

	print ("going forward")
	x=16
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 1)

	print ("going right")
	r=-15
	l=3
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r),-0.38 )

	print ("going forward")
	x=10
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 0.11)

	print ("going forward")
	x=-16
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 2.4)

	print ("going right")
	r=-15
	l=0
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r),0.85 )

	m = MediumMotor('outC')
	i = 0
	while i < 5:
		m.run_timed(time_sp=1000, speed_sp=-1000)
		sleep(1)
		m.run_timed(time_sp=1000, speed_sp=750)	
		i+=1


def Row_Machine1():

	print ("going forward")
	x=-16
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 0.50)

	print ("going right")
	r=-30
	l=0
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r),0.3 )

	print ("going forward")
	x=-16
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 0.51)

	print ("going right")
	r=40
	l=20
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r),1 )

	print ("going right")
	r=5
	l=-10
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r),0.5 )

def Row_Machine2():
	print ("going right")
	r=-20
	l=-20
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r),0.8 )

	print ("going right")
	r=-10
	l=10
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r),0.21 )

	print ("going forward")
	x=-16
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 0.51)

	print ("going back left")
	r=25
	l=-10
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r),0.7)

	print ("going forward")
	x=-5
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 0.2)

	print ("going backwards")
	x=5
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 0.3) 


def Row_Machine_Final():
	r=-15
	l=-25
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r),1.3)
	

	r=-10
	l=10
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r),0.55)

	r=-6
	l=-6
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r),0.8)


	r=20
	l=5
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r),1.5)

	r=20
	l=20
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r),1)

	r=20
	l=15
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r),1)


#Row_Machine_Final()

def Bench_Scotch():
	print ("going forward")
	x=-20
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 0.91)

	r=-10
	l=0
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r),0.1 )
	

	print ("going forward")
	x=-30
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 1.55)

	r=-10
	l=-1
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r),0.2 )

	sleep(0.5)

	print ("going forward")
	x=50
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 1.62)