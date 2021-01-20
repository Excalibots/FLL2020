#!/usr/bin/env python3

from configruation import *
from half import *
from other_runs import *
from run3 import *

#set up the runs here
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
        run3_b()

def run_3b(state):
    if state:
        print('starting run tres')
        sound.beep()
    else:
        print('Run 3')
        run3_b()

def tests(state):
        if state:
            print('starting run tres')
            sound.beep()
        else:
            print('Tests')
            print('Tests')
            while True:
                test()

def buttons():
    btn.on_right = run_tres
    btn.on_up = run_dos
    btn.on_down = run_3b
    btn.on_enter = tests
    btn.on_left = run_uno
    print('starting main')
    
    while True:
        btn.process()
        sleep(0.01)

buttons()