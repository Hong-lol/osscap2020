#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 19:51:06 2020

@author: hogeon
"""
#초음파센서값 지속 출력

import RPi.GPIO as gpio

import time

  

gpio.setmode(gpio.BCM)

  

trig = 12

echo = 25

  

print "start"

 
gpio.setup(trig, gpio.OUT)

gpio.setup(echo, gpio.IN)

 

try :

  while True :

    gpio.output(trig, False)

    time.sleep(0.5)

 

    gpio.output(trig, True)

    time.sleep(0.00001)

    gpio.output(trig, False)

 

    while gpio.input(echo) == 0 :

      pulse_start = time.time()

 

    while gpio.input(echo) == 1 :

      pulse_end = time.time()

 

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17000

    distance = round(distance, 2)

 

    print "Distance : ", distance, "cm"

except :

  gpio.cleanup()



#초음파센서에 접근하면 LED On  

import RPi.GPIO as gpio 
import time 
import sys 
import warnings 
warnings.filterwarnings('ignore') 
LED = 4 
TRIGER = 24 
ECHO = 23 

gpio.setmode(gpio.BCM) 
gpio.setup(TRIGER, gpio.OUT) 
gpio.setup(ECHO,gpio.IN) 
gpio.setup(LED, gpio.OUT) 

startTime = time.time() 
try: 
    while True: 
        gpio.output(TRIGER,gpio.LOW) 
        time.sleep(0.1) 
        gpio.output(TRIGER,gpio.HIGH) 
        time.sleep(0.00002) 
        gpio.output(TRIGER,gpio.LOW) 
        
        while gpio.input(ECHO) == gpio.LOW: 
            startTime = time.time() 
        while gpio.input(ECHO) == gpio.HIGH: 
            endTime = time.time() 
        
        period = endTime - startTime 
        dist1 = round(period * 1000000 / 58, 2) 
        dist2 = round(period * 17241, 2) 
        
        try: 
            if dist2 <= 20: 
                print('error124') 
                gpio.output(LED, gpio.HIGH) 
                time.sleep(1) 
                gpio.output(LED, gpio.LOW) 
                time.sleep(1) 
        
        except KeyboardInterrupt: 
            print("error") 
        
        print('Dist1', dist1, 'cm', ', Dist2', dist2, 'cm') 
except KeyboardInterrupt: 
    gpio.cleanup() 
    sys.exit()
    
    
'''
ToDo

GPIO로 센서값 받아오기
센서값 확인 후 오류값 빈도 및 오차범위 측정
오류값 및 오차 범위 보정 알고리즘(찾는중)
LED 오픈소스랑 다른 코드를 통해 Matrix에 출력
'''
