#!/usr/bin/env python3

from configruation import *
from half import *
from other_runs import *
from run1 import *
from threading import Thread

#set up the runs here
# each function does a discrete task.
#tasks are split to small units to help testing each one individually
#different team memnbers can work on different runs and parts within the runs
def R1(state):
	if state:
		print('starting run 1')
	else:
		print('Run 1')
		PushSlideBox()
		GoBackFromSlide()
		GoToBoccia()
		goTOframe()
		DropBlocks()   
		GoToMiniBoccia()		
		goingtoweightmachine()
		doWeights()
		GoBackFromWeight()
		#use a thread to move arm while moving forward
		t = Thread(target=moveArm)
		t.start()
		DoSlide() 
	print('done')	

def R2(state):
	if state: 
		print('starting run tres')
	else:
		print('Run 2')
		newHopScotch()

def R3(state):
	if state:
		print('starting run tres')
	else:
		print('3rd run')
		do_step_tracker()
		go_back_from_step_tracker()
		ready_treadmill()
		do_treadmill()
		back_from_treadmill()
		#align against the south wall before attempting doRowerWithArm
		# this helps the robot to be consistent
		align()
		#move the arm down while going to rower
		t1 = Thread(target=moveArmDown)
		t1.start()
		doRowerWithArm()
		moveRowerArm()
		#move arm with slide figure up while getting position
		doPerson()
		t2 = Thread(target=moveArmUp)
		t2.start()
		goToPullUp()
		goUnderPullUp()
		doDanceNew()



def armDown(state):
	if state:
		#code to move arm down
		print('Moving Arm Down')
		medMotor.reset()
		medMotor.on(SpeedPercent(-50))
	else:
		#stop the arm movement
		print('Stopped Moving Arm Down')
		#print(medMotor.degrees())       
		medMotor.stop()		
def armUp(state):
	if state:
		#move arm up
		print('Moving Arm Up')
		medMotor.reset()
		medMotor.on(SpeedPercent(50))
	else:
		# stop the arm movement
		print('Stopped Moving Arm Up')
		#print(medMotor.degrees)       
		medMotor.stop()

def buttons():
	#This allows the different runs to be controlled but button press
	btn.on_right = R3
	btn.on_up = R2
	btn.on_down = armDown
	btn.on_enter = armUp
	btn.on_left = R1
	print('starting main')
	sound.play_tone(700, 0.5)
	sound.speak("Lets do this")
	
	while True:
		#start the process to listen to the button presses
		btn.process()
		sleep(0.01)
#the function that gets called when the program starts
buttons()
