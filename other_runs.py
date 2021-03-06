
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
	x=10
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 0.58)

	x=25
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 1.00)

	
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
	x=-20
	tank.on_for_degrees(SpeedPercent(x), SpeedPercent(x), 35)
	sleep(.50)


	print ("going backward")
	x=-15
	tank.on_for_degrees(SpeedPercent(x), SpeedPercent(x), 180)
	# slide guy falls by this line

	# print ("going right")
	# r=0
	# l=15
	# tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 0.25)

	print ("going left")
	r=-15
	l=15
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r), 0.25)
	print(color2.reflected_light_intensity)
	
	while color2.reflected_light_intensity < 30:
		print(color2.reflected_light_intensity)
		tank.on(SpeedPercent(15), SpeedPercent(-15))
	tank.stop()
	sleep(.25)

	while color2.reflected_light_intensity > 15:
		print(color2.reflected_light_intensity)
		tank.on(SpeedPercent(5), SpeedPercent(-5))
	tank.stop()
	sleep(.25)
	print('follow line')
	foll_line()
	#sleep(0.25)
	sleep(.25)
	tank.on_for_degrees(SpeedPercent(-7),SpeedPercent(-10),55)
	#tank.on_for_seconds(SpeedPercent(-3),SpeedPercent(-3),1) # try for 1 more time to push the block on boccia
	sleep(.25)
	tank.on_for_degrees(SpeedPercent(10),SpeedPercent(7),110)

	#mission 3
	
	tank.on_for_degrees(SpeedPercent(10),SpeedPercent(-10),90)
	
	tank.on_for_degrees(SpeedPercent(-15),SpeedPercent(-15),380)
	tank.on_for_degrees(SpeedPercent(-7),SpeedPercent(-7),70) # dump the crate into the boccia target area
	#tank.on_for_degrees(SpeedPercent(7),SpeedPercent(7),160)  dump the crate into the boccia target area
	
	tank.on_for_degrees(SpeedPercent(-10),SpeedPercent(10),68) # turn on an angle to go to base after dumping the crate in the target area
	
	leftMotor.reset()
	x = 10
	while abs(leftMotor.degrees) < 1200:
		if x < 50:
			x = x + 3
			y = x
		tank.on(SpeedPercent(x),SpeedPercent(y))
	tank.stop()
	tank.on_for_degrees(SpeedPercent(30),SpeedPercent(-30),90)
	tank.on_for_degrees(SpeedPercent(50),SpeedPercent(50),400)
	

def foll_line():
	tank.cs = ColorSensor(INPUT_2)
	tank.follow_line(
		kp=1.8, ki=0.009, kd=0,
		speed=SpeedPercent(-10),
		follow_for=follow_for_ms,
		ms=3000,
		follow_left_edge=False
		)





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



def Bench_Scotch():
	print ("going forward")
	x=-5
	leftMotor.reset()
	print(leftMotor.degrees)
	dist = leftMotor.degrees
	while dist < 300:
		print(dist)
		print(x)
		tank.on(SpeedPercent(x), SpeedPercent(x))
		if (x > -20 and dist < 200):	
			x = x - .25
		if (dist > 200 and x < -5):
			x = x + .25
		dist = leftMotor.degrees*-1

	tank.stop
	r=-10
	l=0
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r),0.085 )
	

	print ("going forward")
	x=-10
	tank.on_for_seconds(SpeedPercent(x), SpeedPercent(x), 2)

	r=-10
	l=-1
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r),0.2 )

	sleep(0.5)

	print ("going forward")
	x=50
	tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 2)

def benchofthescotch():
	r=-12
	l=-10
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r),1.3 )

	r=-15
	l=-10
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r),1 )

	r=40
	l=30
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r),2 )

	r=10
	l=10
	tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r),1 )

	# print ("going forward")
	# x=-5
	# leftMotor.reset()
	# print(leftMotor.degrees)
	# dist = leftMotor.degrees
	# while dist < 300:
	# 	print(dist)
	# 	print(x)
	# 	tank.on(SpeedPercent(x), SpeedPercent(x))
	# 	if (x > -20 and dist < 200):	
	# 		x = x - .25
	# 	if (dist > 200 and x < -5):
	# 		x = x + .25
	# 	dist = leftMotor.degrees*-1

	# r=-0
	# l=-10
	# tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r),1 )

	# print ("going forward")
	# x=10
	# tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 1)

	# r=-10
	# l=-1
	# tank.on_for_rotations(SpeedPercent(l), SpeedPercent(r),1 )

	# print ("going forward")
	# x=10
	# tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 1)

	# sleep(0.5)

	# print ("going forward")
	# x=50
	# tank.on_for_rotations(SpeedPercent(x), SpeedPercent(x), 2)