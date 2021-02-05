#!/usr/bin/env python3

from configruation import *
from half import *
from other_runs import *
from run3 import *

#!Final Runs
def run_uno(state):
        if state:
            print('starting run tres')
            sound.beep()
        else:
            print('Run 1')
            run_one()

def run_dos(state):
        if state:
            print('starting run tres')
            sound.beep()
        else:
            print('Run 2')
            Bench_Scotch()

def run_tres(state):
    if state:
        print('starting run tres')
        sound.beep()
    else:
        print('Run 2a')
        do_step_tracker()
        go_back_from_step_tracker()
        ready_treadmill()
        do_treadmill()
        back_from_treadmill() 

        do_rower()
        Going_Weight()
        align_2()
        passive3()
        go_under_bridge()
        dance()
#?--------------------------Extras----------------------------------------
def run_3b(state):
    if state:
        print('starting run tres')
        sound.beep()
    else:
        print('Run 3')        
        do_rower()
        Going_Weight()
        align_2()
        passive3()
        go_under_bridge()
        dance()

def tests(state):
        if state:
            print('starting run tres')
            sound.beep()
        else:
            print('Tests')
            do_weights()

def buttons():
	btn.on_right = run_tres
	btn.on_up = run_dos
	btn.on_down = run_3b
	btn.on_enter = tests
	btn.on_left = run_uno
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