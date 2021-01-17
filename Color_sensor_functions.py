from time import sleep
from ev3dev.ev3 import *
from ev3dev2.led import Leds
from ev3dev2.motor import (OUTPUT_A, OUTPUT_B, OUTPUT_D, LargeMotor,
                           MediumMotor, MoveDifferential, MoveTank,
                           SpeedPercent, SpeedRPM, follow_for_ms)
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, TouchSensor
from ev3dev2.sound import Sound
from ev3dev2.wheel import EV3Tire
import sys
import logging
import time
from ev3dev2.button import ButtonBase
from ev3dev2.sensor import Sensor
import os
from logging import getLogger
from os.path import abspath
from ev3dev2 import get_current_platform, Device, list_device_names, DeviceNotDefined, ThreadNotRunning
from ev3dev2.stopwatch import StopWatch
import sys
import math
import select
import time
from threading import Thread


#----------------------------------------------------------------------------------


#MODE FUNCTIONS OF COLOR SENSOR

def reflect_mode(which_INPUT):
    ColorSensor(which_INPUT).mode='COL-REFLECT'
    #Reflected light. Red LED on.    

def ambient_mode(which_INPUT):
     ColorSensor(which_INPUT).mode='COL-AMBIENT'
    #Ambient light. Blue LEDs on.

def color_mode(which_INPUT):
    ColorSensor(which_INPUT).mode='COL-COLOR'
    #Color. All LEDs rapidly cycling, appears white.

def raw_reflect_mode(which_INPUT):
    ColorSensor(which_INPUT).mode='REF-RAW'
    #Raw reflected. Red LED on

def raw_colorRGB_mode(which_INPUT):
    ColorSensor(which_INPUT).mode='RGB-RAW'
    #Raw Color Components. All LEDs rapidly cycling, appears white.

#--------------------------------------------------------------------------
#COLOR VALUES TO BE DEFINED

COLOR_NOCOLOR = 0
#No color.

COLOR_BLACK = 1
#Black color.

COLOR_BLUE = 2
#Blue color.

COLOR_GREEN = 3
#Green color.

COLOR_YELLOW = 4
#Yellow color.

COLOR_RED = 5
#Red color.

COLOR_WHITE = 6
#White color.

COLOR_BROWN = 7
#Brown color.
#---------------------------------------------------------------------------
#Functions that detect values

def reflected_light_intensity(which_INPUT):
    ColorSensor(which_INPUT).reflected_light_intensity
    #Reflected light intensity as a percentage (0 to 100). Light on sensor is red.

def ambient_light_intensity(which_INPUT):
    ColorSensor(which_INPUT).ambient_light_intensity
    #Ambient light intensity, as a percentage (0 to 100). Light on sensor is dimly lit blue.

def color_detected(which_INPUT):
    ColorSensor(which_INPUT).color
    #Color detected by the sensor, categorized by overall value.
    #0: No color
    #1: Black
    #2: Blue
    #3: Green
    #4: Yellow
    #5: Red
    #6: White
    #7: Brown

def get_value_reflected(which_INPUT):
    ColorSensor(which_INPUT).mode='COL-REFLECT'
    while True:
        x = ColorSensor(which_INPUT).value()
        print(x)
        Sound.speak(x)
        sleep(3)

def line_follow_col_finder(which_INPUT):
    ColorSensor(which_INPUT).mode='COL-REFLECT'
    i = 0
    while i < 2000:
        x = ColorSensor(which_INPUT).value()
        if x == 4:
            tank.stop()
        i += 1
#------------------------------------------------------------------------------------

raw
#Red, green, and blue components of the detected color, as a tuple.
#
#Officially in the range 0-1020 but the values returned will never be that high. We do not yet know why the values returned are low, but pointing the color sensor at a well lit sheet of white paper will return values in the 250-400 range.
#
#If this is an issue, check out the rgb() and calibrate_white() methods.

calibrate_white()
#The RGB raw values are on a scale of 0-1020 but you never see a value anywhere close to 1020. This function is designed to be called when the sensor is placed over a white object in order to figure out what are the maximum RGB values the robot can expect to see. We will use these maximum values to scale future raw values to a 0-255 range in rgb().
#
#If you never call this function red_max, green_max, and blue_max will use a default value of 300. This default was selected by measuring the RGB values of a white sheet of paper in a well lit room.
#
#Note that there are several variables that influence the maximum RGB values detected by the color sensor - the distance of the color sensor to the white object - the amount of light in the room - shadows that the robot casts on the sensor

rgb
#Same as raw() but RGB values are scaled to 0-255

lab
#Return colors in Lab color space

hsv
#HSV: Hue, Saturation, Value H: position in the spectrum S: color saturation (“purity”) V: color brightness

hls
#HLS: Hue, Luminance, Saturation H: position in the spectrum L: color lightness S: color saturation

red
#Red component of the detected color, in the range 0-1020.

green
#Green component of the detected color, in the range 0-1020.

blue
#Blue component of the detected color, in the range 0-1020.

#----------------------------------------------------------------------------------