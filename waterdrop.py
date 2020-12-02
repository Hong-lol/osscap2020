import RPi.GPIO as GPIO
import time
import random

delay = 0.0015

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
red1_pin = 11
green1_pin = 27
blue1_pin = 7
red2_pin = 8
green2_pin = 9
blue2_pin = 10
clock_pin = 17
a_pin = 22
b_pin = 23
c_pin = 24
latch_pin = 4
oe_pin = 18

GPIO.setup(red1_pin, GPIO.OUT)
GPIO.setup(green1_pin, GPIO.OUT)
GPIO.setup(blue1_pin, GPIO.OUT)
GPIO.setup(red2_pin, GPIO.OUT)
GPIO.setup(green2_pin, GPIO.OUT)
GPIO.setup(blue2_pin, GPIO.OUT)
GPIO.setup(clock_pin, GPIO.OUT)
GPIO.setup(a_pin, GPIO.OUT)
GPIO.setup(b_pin, GPIO.OUT)
GPIO.setup(c_pin, GPIO.OUT)
GPIO.setup(latch_pin, GPIO.OUT)
GPIO.setup(oe_pin, GPIO.OUT)

screen = [[0 for x in range(32)] for x in range(16)]
num=rand.randint(1,6)
while 1:
    screen[1][4]=1
    refresh()
    screen[1][3]=1
    refresh()
    for i in range(14): 
        screen[i+2][a+1]=1
        refresh()
        screen[i+2][a]=1
        refresh()
        screen[i][a+1]=0
        refresh()
        screen[i][a]=0
        refresh()
        time.sleep(0.0005) 
    screen[15][a+1]=0 
    screen[15][a]=0 
    screen[14][a]=0 
    screen[14][a+1]=0
    refresh()
    time_start=time.time()
    while 1:
        time_finish=time.time()
        if time_finnish-time_start>delay_time:
            break;
