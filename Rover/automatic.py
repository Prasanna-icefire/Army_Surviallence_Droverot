import requests as reqs
import urllib3
import socketio  
import os
import curses
import socketio
import random
from gpiozero import DistanceSensor
from gpiozero import Motor
from gpiozero import Servo
from gpiozero import LED
from time import sleep
motor1 = Motor(forward=27, backward=17)
motor2 = Motor(forward=5, backward=0)
red = LED(22)
red.on()
blue = LED(11)
blue.on()
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)
def my_front():
    motor1.forward()
def my_back():
    motor1.backward()
def my_front_right():
    motor1.forward()
    motor2.forward()
def my_front_left():
    motor1.forward()
    motor2.backward()
def my_back_right():
    motor1.backward()
    motor2.forward()
def my_back_left():
    motor1.backward()
    motor2.backward()
def my_break():
    motor1.stop()
    motor2.stop()
def Rand(start,end,num): 
    res = [] 
  
    for j in range(num): 
        res.append(random.randint(start, end)) 
  
    return res 
sensor = DistanceSensor(echo =16 ,trigger = 21)
dis=10
dil=0.5
bdil=0.3
try:
   while (True):
            f=open("rov.txt","r")
            data=f.read()
            f.close()
            if(data):
             if(data=='w' or data=='e'):
              exit()   
            ulval=sensor.distance*100
            print(ulval)
            res=Rand(1,3,1)
            if(ulval>dis):
               if(res[0]==1):
                 my_front()
                 print("Forward")
                 sleep(dil)
                 my_break()
                 sleep(bdil)
               elif(res[0]==2):
                 print("Front Left")
                 my_front_left()
                 sleep(dil)
                 my_break()
                 sleep(bdil)
               elif(res[0]==3):
                 print("front_right")
                 my_front_right()
                 sleep(dil)
                 my_break()
                 sleep(bdil)
            else:
               if(res[0]==1):
                 my_back()
                 sleep(dil)
                 my_break()
                 sleep(bdil)
               elif(res[0]==2):
                 my_back_left()
                 sleep(dil)
                 my_break()
                 sleep(bdil)
               elif(res[0]==3):
                 my_back_right()
                 sleep(dil)
                 my_break()
                 sleep(bdil)
                

            
             

             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()


