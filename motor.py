import requests as reqs
import urllib3
import socketio  
import os
import curses
import socketio
sio=socketio.Client()
sio.connect('http://13.232.28.46:8000')
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
sensor = DistanceSensor(echo =16 ,trigger = 21)
try:
   while (True):
            f=open("demo.txt","r")
            data=f.read()
            f.close()      
            ulval=sensor.distance*100
            print(ulval)
            if data == 'h' :
                 my_back_right()
                 sleep(0.2)
                 my_break()
            elif data == 'f' :
                 my_back_left()
                 sleep(0.2)
                 my_break()
            elif data =='g' :
                 my_back()
                 sleep(0.2)
                 my_break()
            elif data == 'b' :
                 my_break()
                 sleep(1)
            elif data == 't' and ulval>40 :
                 print('Executing_forward')
                 my_front()
                 sleep(0.2)
                 my_break()
            elif data == 'y' and ulval >40:
                 print('Executing_right')
                 my_front_right()
                 sleep(0.2)
                 my_break()
            elif data == 'r' and ulval>40:
                 my_front_left()
                 sleep(0.2)
                 my_break()

            elif data == 'b' :
                 my_break()
                 sleep(1)
            elif data == 'b' :
                 my_break()
                 sleep(1)           
            elif (ulval<=20):
                 my_break()
                 sleep(1)
                 my_back_left()
                 sleep(0.2)
                 my_break()
                 sleep(1)
                 my_front_right()
                 sleep(0.2)
                 my_front_left()
                 sleep(0.2)
            else:
                 my_break()
                 sleep(1)

             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()


