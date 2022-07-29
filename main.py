'''
RPI-Pico Robot for education volunteering
Build date: 22.07.29
language: Python(micropython)
Target: Raspberry Pi Pico(Arm v6-M)
'''
#includes
from machine import Pin, UART
from time import sleep
from neopixel import Neopixel

#setup-variables
numpix = 8
NPXL_BASE = 28

#setup-defines
UART1_BT = UART(1, 9600) #UART1_TX: 11, UART!_RX: 12
#UART1_BT.init(9600, bits=8, parity=None, stop=1)

led = Pin(25, Pin.OUT) #internal LED, for debug
MotorR_F = Pin(4, Pin.OUT)
MotorR_B = Pin(5, Pin.OUT)
MotorL_F = Pin(6, Pin.OUT)
MotorL_B = Pin(7, Pin.OUT)

pixels = Neopixel(numpix, 0, NPXL_BASE, "GRB") #Init neopixel(G, R, B)
pixels.brightness(50)

white = (255, 255, 255)
yellow = (255, 100, 0)
orange = (255, 50, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

#run
while True:
#     led.high()
#     sleep(1)
    if UART1_BT.any():
        RcvBT = UART1_BT.readline()
    
    if RcvBT == "1":
        MotorR_F.high()
        MotorR_B.low()
        MotorL_F.high()
        MotorL_B.low()
        pixels.fill(white)
        
    elif RcvBT == "2":
        MotorR_F.low()
        MotorR_B.high()
        MotorL_F.low()
        MotorL_B.high()
        pixels.fill(red)
    
    elif RcvBT == "3":
        MotorR_F.high()
        MotorR_B.low()
        MotorL_F.low()
        MotorL_B.high()
        pixels.fill(blue)
        
    elif RcvBT == "4":
        MotorR_F.low()
        MotorR_B.high()
        MotorL_F.high()
        MotorL_B.low()
        pixels.fill(orange)
        
    elif RcvBT == "0":
        MotorR_F.low()
        MotorR_B.low()
        MotorL_F.low()
        MotorL_B.low()
        pixels.fill(green)
