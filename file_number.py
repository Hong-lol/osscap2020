import RPi.GPIO as GPIO
import time

delay = 0.000001

GPIO.setmode(GPIO.BCM)
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
laser_out=12
laser_in=13

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
gpio.setup(laser_out, gpio.OUT)
gpio.setup(laser_in, gpio.IN)

screen = [[0 for x in range(32)] for x in range(16)]

def clock():
    GPIO.output(clock_pin, 1)
    GPIO.output(clock_pin, 0)

def latch():
    GPIO.output(latch_pin, 1)
    GPIO.output(latch_pin, 0)

def bits_from_int(x):
    a_bit = x & 1
    b_bit = x & 2
    c_bit = x & 4
    return (a_bit, b_bit, c_bit)

def set_row(row):
    #time.sleep(delay)
    a_bit, b_bit, c_bit = bits_from_int(row)
    GPIO.output(a_pin, a_bit)
    GPIO.output(b_pin, b_bit)
    GPIO.output(c_pin, c_bit)
    #time.sleep(delay)

def set_color_top(color):
    #time.sleep(delay)
    red, green, blue = bits_from_int(color)
    GPIO.output(red1_pin, red)
    GPIO.output(green1_pin, green)
    GPIO.output(blue1_pin, blue)
    #time.sleep(delay)

def set_color_bottom(color):
    #time.sleep(delay)
    red, green, blue = bits_from_int(color)
    GPIO.output(red2_pin, red)
    GPIO.output(green2_pin, green)
    GPIO.output(blue2_pin, blue)
    #time.sleep(delay)

def refresh():
    for row in range(8):
        GPIO.output(oe_pin, 1)
        set_color_top(0)
        set_row(row)
        #time.sleep(delay)
        for col in range(32):
            set_color_top(screen[row][col])
            set_color_bottom(screen[row+8][col])
            clock()
        #GPIO.output(oe_pin, 0)
        latch()
        GPIO.output(oe_pin, 0)
        time.sleep(delay)

def fill_rectangle(x1, y1, x2, y2, color):
    for x in range(x1, x2):
        for y in range(y1, y2):
            screen[y][x] = color


def set_pixel(x, y, color):
    screen[y][x] = color

def number0(x, y):
    for a in range(3):
        screen[y][x+2]=1
        screen[y+7][x+2]=1
        x+=1
    x-=3
    for b in range(6):
        screen[y+1][x+1]=1
        screen[y+1][x+5]=1
        y+=1
    
    
def number1(x, y):
    for a in range(8):
        screen[y][x+3]=1
        y+=1
    y-=8
    screen[y+1][x+2]=1
    screen[y+7][x+2]=1
    screen[y+7][x+4]=1
    
def number2(x, y):
    for a in range (3):
        screen[y][x+2]=1
        x+=1
    x-=3
    screen[y+1][x+1]=1
    for b in range (3):
        screen[y+1][x+5]=1
        y+=1
    y-=3
    screen[y+4][x+4]=1
    screen[y+5][x+3]=1
    screen[y+6][x+2]=1
    for c in range (5):
        screen[y+7][x+1]=1
        x+=1

def number3(x, y):
    for a in range (3):
        screen[y][x+2]=1
        screen[y+3][x+2]=1
        screen[y+7][x+2]=1
        x+=1
    x-=3
    screen[y+1][x+1]=1
    screen[y+1][x+5]=1
    screen[y+2][x+5]=1
    screen[y+6][x+1]=1
    for b in range (3):
        screen[y+4][x+5]=1
        y+=1

def number4(x, y):
    for a in range(8):
        screen[y][x+5]=1
        y+=1
    y-=8
    for b in range(5):
        screen[y+5][x+1]=1
        x+=1
    x-=5
    screen[y+1][x+4]=1
    screen[y+2][x+3]=1
    screen[y+3][x+2]=1
    screen[y+4][x+1]=1
        

def number5(x,y):
    for a in range (3):
        screen[y][x+2]=1
        screen[y+3][x+2]=1
        screen[y+7][x+2]=1
        x+=1
    x-=3
    screen[y][x+5]=1
    for b in range(4):
        screen[y][x+1]=1
        y+=1
    y-=4
    for c in range(3):
        screen[y+4][x+5]=1
        y+=1
    y-=3
    screen[y+6][x+1]=1
    

def number6(x, y):
    for a in range(3):
        screen[y][x+2]=1
        screen[y+3][x+2]=1
        screen[y+7][x+2]=1
        x+=1
    x-=3
    for b in range(6):
        screen[y+1][x+1]=1
        screen[y+1][x+5]=1
        y+=1
    y-=6
    screen[y+2][x+5]=0
    screen[y+3][x+5]=0

def number7(x, y):
    for a in range(5):
        screen[y][x+1]=1
        x+=1
    x-=5
    for b in range(3):
        screen[y][x+5]=1
        screen[y+5][x+2]=1
        y+=1
    y-=3
    screen[y+3][x+4]=1
    screen[y+4][x+3]=1

def number8(x, y):
    for a in range (3):
        screen[y][x+2]=1
        screen[y+3][x+2]=1
        screen[y+7][x+2]=1
        x+=1
    x-=3
    for b in range (6):
        screen[y+1][x+1]=1
        screen[y+1][x+5]=1
        y+=1
    y-=6
    screen[y+3][x+1]=0
    screen[y+3][x+5]=0
    

def number9(x, y):
    for a in range(3):
        screen[y][x+2]=1
        screen[y+4][x+2]=1
        screen[y+7][x+2]=1
        x+=1
    x-=3
    for b in range(6):
        screen[y+1][x+1]=1
        screen[y+1][x+5]=1
        y+=1
    y-=6
    screen[y+4][x+1]=0
    screen[y+5][x+1]=0
turget=input("number")
turget=list(turget)

if turget[1]=="1":
    number1(16,0)
        
elif turget[1]=="2":
    number2(16,0)
        
elif turget[1]=="3":
    number3(16,0)
        
                
elif turget[1]=="4":
    number4(16,0)
        
elif turget[1]=="5":
    number5(16,0)
        
elif turget[1]=="6":
    number6(16,0)
        
elif turget[1]=="7":
    number7(16,0)
        
elif turget[1]=="8":
    number8(16,0)
        
elif turget[1]=="9":
    number9(16,0)
        
else :
    number0(16,0)



if turget[2]=="1":
    number1(24,0)
        
elif turget[2]=="2":
    number2(24,0)
        
elif turget[2]=="3":
    number3(24,0)
        
elif turget[2]=="4":
    number4(24,0)
        
elif turget[2]=="5":
    number5(24,0)
        
elif turget[2]=="6":
    number6(24,0)
        
elif turget[2]=="7":
    number7(24,0)
    
elif turget[2]=="8":
    number8(24,0)

elif turget[2]=="9":
    number9(24,0)
else :
    number0(24,0)

