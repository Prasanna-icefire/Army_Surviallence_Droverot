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
#sensor = DistanceSensor(echo =16 ,trigger = 21)
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
             f=open("demo.txt","r")
             data=f.read()
             f.close()
             sleep(0.5)
             #print(sensor.distance)
           #if(sensor.distance*100>80):
             if data == 'q':
             	 break
             if data == 'S': # Added for shutdown on capital S
                 os.system ('sudo shutdown now') # shutdown right now!
             elif data == 't' :
                 print('Executing_forward')
                 my_front()
                 sleep(0.3)
                 my_break()
             elif data == 'y':
                 print('Executing_right')
                 my_front_right()
                 sleep(0.3)
                 my_break()
             elif data == 'r':
                 my_front_left()
                 sleep(0.3)
                 my_break()
             elif data == 'h' :
                 my_back_right()
                 sleep(0.3)
                 my_break()
             elif data == 'f' :
                 my_back_left()
                 sleep(0.3)
                 my_break()
             elif data =='g' :
                 my_back()
                 sleep(0.3)
                 my_break()
             elif data == 'b' :
                 my_break()
                 sleep(1)

#           elif data == 'b' :
 #            my_break()
  #           sleep(1)           
   #        else:
    #         my_back()
     #        sleep(0.5)
      #       my_front_right()
       #      sleep(1)
        #     my_front_left()
         #    sleep(1)    
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()


