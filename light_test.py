#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 16:14:13 2020

@author: hogeon
"""

import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

laser_out = 12
laser_in = 13

gpio.setup(laser_out, gpio.OUT)
gpio.setup(laser_in, gpio.IN)

try:
    while True:
        light = gpio.input(laser_in)
        gpio.output(laser_out, True)
        print(light)
except:
    gpio.cleanup()