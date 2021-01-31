#!/usr/bin/env python3
from configruation import *


def follow_line_1(speed, time):
	print('following line')
	tank.cs = ColorSensor(INPUT_3)
	tank.follow_line(
        kp=1.8, ki=0.009, kd=0,
        speed=SpeedPercent(speed),
        follow_for=follow_for_ms,
        ms=time,
        follow_left_edge=True,
		target_light_intensity=17
        )

def follow_line_2():
	tank.cs = ColorSensor(INPUT_1)
	tank.follow_line(
    	kp=1.8, ki=0.009, kd=0,
    	speed=SpeedPercent(-30),
    	follow_for=follow_for_ms,
    	ms=500,
    	follow_left_edge=False
    	)
# follow line for 1820 ms on the left edge of the line
def align_2(): # to be adjusted 
	sleep(.25)
	print("align for batcha")
	print(color3.color_name)
	tank.on_for_degrees(SpeedPercent(-20),SpeedPercent(-20),180)
	leftBlack =  True
	rightBlack = True
	tankDegrees = 0
	leftMotor.reset()
	rightMotor.reset()
	while color3.color_name !="Black":
		print(color3.color_name)
		tank.on(SpeedPercent(-10), SpeedPercent(10))
		tankDegrees = leftMotor.degrees
		if abs(tankDegrees) > 90:
			leftBlack = False
			tank.stop()
			break
	tank.stop()
	print("Robot looked left and found black line?")
	print(leftBlack)
	tankDegrees = tankDegrees * -1
	print ('Robot turned degrees')
	print(tankDegrees)
	leftMotor.reset()
	rightMotor.reset()
	if leftBlack:
		print('Since Robot saw the black line to the left move forward and then turn around to straight')
		tank.on_for_degrees(SpeedPercent(-10),SpeedPercent(-10),tankDegrees*3)
		tank.on_for_degrees(SpeedPercent(10),SpeedPercent(-10),tankDegrees)
		tankDegrees=0
		tank.stop()
	else:
		print('Robot did not see the black line when it turned left')
		print('now straightening out - check tankDegrees for accuracy')
		tank.on_for_degrees(SpeedPercent(10),SpeedPercent(-10),tankDegrees)
		tankDegrees = 0
		leftMotor.reset()
		rightMotor.reset()
		print('turn right until black line or until 40 degrees.')
		while color3.color_name !="Black":
			print(color3.color_name)
			tank.on(SpeedPercent(10), SpeedPercent(-10))
			tankDegrees = rightMotor.degrees
			if abs(tankDegrees) > 90:
				rightBlack = False
				tank.stop()
				break
		print('Robot looked right and found black line?')
		print(rightBlack)
		tank.stop()
		if (rightBlack):
			print('Since Robot saw the black line to the right move forward and then turn around to straight')
			tankDegrees = tankDegrees * -1
			print ('Robot turned degrees')
			print(tankDegrees)
			leftMotor.reset()
			rightMotor.reset()
			print(tankDegrees)
			print('move forward')
			tank.on_for_degrees(SpeedPercent(-10),SpeedPercent(-10),tankDegrees*2.25)
			print('stragihten out')
			tank.on_for_degrees(SpeedPercent(-10),SpeedPercent(10),tankDegrees)
			tank.stop()
	print('go back to wall')		
	tank.on_for_seconds(SpeedPercent(30),SpeedPercent(30),1.25)

def run3_b():
	med.on_for_rotations(30, -1.39)
	print("arm down")
	mdiff.on_for_distance(25, -80)
	print("forward complete, ready to line follow")
	follow_line_1(-30,1200)  #speed is -30 and time is 1200 ms, change as approriate.
	print("follow line complete")
	rightMotor.on_for_rotations(-5, 0.09999)
	print("turn into mission complete")
	mdiff.on_for_distance(20, -13)
	print("going forward")
	med.on_for_rotations(24, -1.02)
	print("dropping arm")
	mdiff.on_for_distance(20, 28) #go for less here
	print("forward into mission complete")
	leftMotor.on_for_rotations(-5, 0.065)
	print("turned")
	mdiff.on_for_distance(20, 43)
	print("move backwards out of mission complete")
	leftMotor.on_for_rotations(-5, -0.078)
	print("turn out of mission complete")
	med.on_for_rotations(30, 1.1)
	print("mini boccia complete")
	mdiff.on_for_distance(25, -10)
	rightMotor.on_for_degrees(5, 45.59)
	mdiff.on_for_distance(25, -200)
	rightMotor.on_for_degrees(5, -190)
	med.on_for_rotations(30, 2.3)
	mdiff.on_for_distance(25, -160)
	print("do the dance")
	while True:
		tank.on_for_degrees(SpeedPercent(20),SpeedPercent(-20),90)
		tank.on_for_degrees(SpeedPercent(-20),SpeedPercent(20),90)




	#mdiff.on_for_distance(25, -10)
	#rightMotor.on_for_degrees(5, 45.59)
	#mdiff.on_for_distance(25, -200)
	#rightMotor.on_for_degrees(-50, 210)
	#leftMotor.on_for_degrees(50, 130)
	#mdiff.on_Sfor_distance(25, 60)
	#leftMotor.on_for_degrees(20, -40)
	#rightMotor.on_for_degrees(20, -60)









    #med.on_for_rotations(30, -0.6)
    #mdiff.on_for_distance(15, -30)
    #print("move forward")
    #leftMotor.on_for_rotations(-5, 0.32)
    #print("turned")
    #med.on_for_rotations(20, 1.2)
    #print("bring arm up")
    #mdiff.on_for_distance(15, 70)
    #rightMotor.on_for_rotations(-5, 0.55)
    #print("turn left until at phone flip ")
    #mdiff.on_for_distance(5, 70)
    #med.on_for_rotations(15, -1.65)
    #print("bring arm down till ground")
    ##rightMotor.on_for_rotations(-5, 0.05)
    ##med.on_for_rotations(15, -0.25)
    #mdiff.on_for_distance(5, -55)
    #print("move forward until into the phone")
    #med.on_for_rotations(50, 10)
    #print("flip phone")



    #mdiff.on_for_distance(20, 40)
    #print("move out of phone")
    #rightMotor.on_for_rotations(-5, 1.2)
    #print("turn until out of the phone")
    #mdiff.on_for_distance(20, -40)
    #print("move back to be align")
    #rightMotor.on_for_rotations(-5, 0.4)
    #print("align with the mini botia so that we can turn later")
    #mdiff.on_for_distance(20, 65)
    #print("move forward to mini botia")
    #leftMotor.on_for_rotations(-5, 0.6)
    #print("turn towards the bridge ")
    #mdiff.on_for_distance(20, 120)
    #print("go forward to bridge")
    #rightMotor.on_for_rotations(-5, -0.55)
    #print("turn until aligned with bridge")
    #mdiff.on_for_distance(10, 50)
    #print("move forwards until  ")
    #leftMotor.on_for_rotations(-5, 0.1) ###
    #med.on_for_rotations(50, -1.2)
    #mdiff.on_for_distance(10, 40)
    ##leftMotor.on_for_rotations(-5, 0.09) #0.09 or 0.12
    #mdiff.on_for_distance(10, 60)
    ##leftMotor.on_for_rotations(-5, 0.15)
    #mdiff.on_for_distance(10, 20)
    #med.on_for_rotations(50, -0.5)
    #leftMotor.on_for_rotations(-5, 0.15)
    #med.on_for_rotations(50, -0.1)
    #leftMotor.on_for_rotations(-5, -0.2)
    #med.on_for_rotations(50, 0.5)
    ##leftMotor.on_for_rotations(-5, -0.05)
    #mdiff.on_for_distance(10, -20)
    ##leftMotor.on_for_rotations(-5, -0.05)
    #mdiff.on_for_distance(10, -100)
    #sleep(2)

    #while True: 
        #med.on_for_rotations(50, 1.5)
        #rightMotor.on_for_rotations(-5, -0.4)
        #mdiff.on_for_distance(40, -120)
        #mdiff.on_for_distance(10, -20)
        #mdiff.on_for_distance(10, 20)
        #med.on_for_rotations(50, -0.5)
        #leftMotor.on_for_rotations(-5, -0.05)
        #leftMotor.on_for_rotations(-5, 0.05)
        #mdiff.on_for_distance(10, -20)   
        #mdiff.on_for_distance(10, 20)

def passive3():
	print('start run 3 passive attachment')
	tank.on_for_degrees(SpeedPercent(-20),SpeedPercent(-20),680)
	leftMotor.reset()
	tank.on_for_seconds(SpeedPercent(20),SpeedPercent(-20),.35)
	sleep(.25)
	tankDegrees = leftMotor.degrees
	print(tankDegrees)
	print(color3.reflected_light_intensity)
	while color3.reflected_light_intensity > 10:
		tank.on(SpeedPercent(-10),SpeedPercent(10))
		print(color3.reflected_light_intensity)
	tank.stop()
	follow_line_1(-10,3700)
	#tank.on_for_degrees(SpeedPercent(-10),SpeedPercent(-10),400)
	tank.on_for_degrees(SpeedPercent(10),SpeedPercent(-10),150)

def go_under_bridge():
	tank.on_for_degrees(SpeedPercent(20),SpeedPercent(20),750)
	tank.on_for_degrees(SpeedPercent(-20),SpeedPercent(-20),300)
	tank.on_for_degrees(SpeedPercent(-30),SpeedPercent(-30),300)
	tank.on_for_degrees(SpeedPercent(-30),SpeedPercent(30),75)

def dance():
	tank.on_for_degrees(SpeedPercent(-30),SpeedPercent(-30),460)
	tank.on_for_degrees(SpeedPercent(-30),SpeedPercent(0),160)
	#tank.on_for_degrees(SpeedPercent(30),SpeedPercent(30),60)
	i = 0
	while ( i < 15):
		tank.on_for_degrees(SpeedPercent(-30),SpeedPercent(30),180)
		tank.on_for_degrees(SpeedPercent(30),SpeedPercent(-30),180)
		tank.on_for_degrees(SpeedPercent(-30),SpeedPercent(30),50)
		tank.on_for_degrees(SpeedPercent(30),SpeedPercent(-30),50)
		i = i + 1
	sound.speak("All done here!")
