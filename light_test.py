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
    queue = []
    now = 0
    display_time = 0
    
    while True:
        light = gpio.input(laser_in)
        gpio.output(laser_out, True)
        
        if light == 1 && now == 0:
            now = time.time()
        
        if light == 0 && now != 0:
            queue.append(now)
            now = 0
            if len(queue) > 5:
                queue.pop(0)
        
        if len(queue) == 5:
            ans = 0
            for i in range 4:
                ans += queue[i+1] - queue[i]
            display_time = ans / 5
        
        print(display_time)
            
        
except:
    gpio.cleanup()