import requests as reqs
import urllib3
import socketio  
import os
import curses
from gpiozero import DistanceSensor
from gpiozero import Motor
from gpiozero import Servo
from gpiozero import LED
from time import sleep
motor1 = Motor(forward=27, backward=17)
motor2 = Motor(forward=0, backward=5)
sensor = DistanceSensor(echo =16 ,trigger = 21)
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
try:
  while (True):
            char = response.json()
            print(char)
            curses.flushinp()
            if(sensor.distance>40):
             if char == ord('q'):
                 break
             if char == ord('S'): # Added for shutdown on capital S
                 os.system ('sudo shutdown now') # shutdown right now!
             elif char == ord('t') :
                 my_front()
                 sleep(0.5)
                 my_break()
             elif char == ord('y') :
                 my_front_right()
                 sleep(0.5)
                 my_break()
             elif char == ord('r') :
                 my_front_left()
                 sleep(0.5)
                 my_break()
             elif char == ord('h') :
                 my_back_right()
                 sleep(0.5)
                 my_break()
             elif char == ord('f') :
                 my_back_left()
                 sleep(0.5)
                 my_break()
             elif char == ord('g') :
                 my_back()
                 sleep(0.5)
                 my_break()
             elif char == ord('b') :
                 my_break()
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()

