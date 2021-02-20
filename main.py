#!/usr/bin/env python3

from configruation import *
from half import *
from other_runs import *
from run1 import *
from threading import Thread

#set up the runs here
def R1(state):
	if state:
		print('starting run 1')
	else:
		print('Run 1')
		# PushSlideBox()
		# GoBackFromSlide()
		# GoToBoccia()
		goTOframe()
		DropBlocks()   
		GoToMiniBoccia()		
		goingtoweightmachine()
		doWeights()
		GoBackFromWeight()
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
		align()
		t1 = Thread(target=moveArmDown)
		t1.start()
		doRowerWithArm()
		moveRowerArm()
		doPerson()
		t2 = Thread(target=moveArmUp)
		t2.start()
		goToPullUp()
		goUnderPullUp()
		doDanceNew()



def armDown(state):
	if state:
		print('Moving Arm Down')
		medMotor.reset()
		medMotor.on(SpeedPercent(-50))
	else:
		print('Stopped Moving Arm Down')
		#print(medMotor.degrees())       
		medMotor.stop()		
def armUp(state):
	if state:
		print('Moving Arm Up')
		medMotor.reset() 
		medMotor.on(SpeedPercent(50))
	else:
		print('Stopped Moving Arm Up')
		#print(medMotor.degrees)       
		medMotor.stop()

def buttons():
	btn.on_right = R3
	btn.on_up = R2
	btn.on_down = armDown
	btn.on_enter = armUp
	btn.on_left = R1
	print('starting main')
	sound.play_tone(700, 0.5)
	sound.speak("Lets do this")
	# sound.play_tone(600, 0.5)
	# sound.play_tone(700, 0.5)
	# sound.play_tone(600, 0.5)
	# sound.play_tone(900, 1)

	# sound.play_song((
	# ('D4', 'e3'),      # intro anacrouse
	# ('D4', 'e3'),
	# ('D4', 'e3'),
	# ('G4', 'h'),       # meas 1
	# ('D5', 'h'),
	# ('C5', 'e3'),      # meas 2
	# ('B4', 'e3'),
	# ('A4', 'e3'),
	# ('G5', 'h'),
	# ('D5', 'q')))
	
	while True:
		btn.process()
		sleep(0.01)

buttons()
