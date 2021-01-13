import math
import requests as reqs
import urllib3
import socketio  
import os
import curses
import geopy.distance
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

def angleFromCoordinate(lat1,long1,lat2,long2):
    dLon = float(long2) - float(long1)
    y = math.sin(dLon) * math.cos(float(lat2))
    x = math.cos(float(lat1)) * math.sin(float(lat2)) - math.sin(float(lat1))* math.cos(float(lat2)) * math.cos(dLon)
    brng = math.atan2(y, x)
    brng = math.degrees(brng)
    brng = (brng + 360) % 360
    brng = 360 - brng
    print(brng)
    return brng
def getmyloc():
    f=open("source.txt",'r')
    data=f.read()
    f.close()
    return eval(data)    
def getdistance(lat1,long1,lat2,long2):
    coords_1 = (float(lat1),float(long1))
    coords_2 = (float(lat2),float(long2))
    print("co-ordinates in getdistance method ")
    print(coords_1,coords_2)
    ldis=geopy.distance.vincenty(coords_1, coords_2).km
    print(ldis)
    return(ldis)
sensor = DistanceSensor(echo =16 ,trigger = 21)
def read_destination_coordinates():
    f=open("descoor.txt",'r')
    data=f.read()
    f.close()
    return eval(data)
def heading_angle():
    f=open("compass.txt",'r')
    data=f.read()
    f.close()
    print("Errorrrrrrrrr")
    print(data)
    return (data)
source = getmyloc()    
 
try:
    destination = read_destination_coordinates()
    
    ldis = getdistance(source['Latitude'],source['Longitude'],destination['lat'],destination['lon'])
    while ldis>0.01:
      ulval=sensor.distance*100
      if(ulval<10):
        my_back()
        sleep(1)
        my_front_right()
        sleep(1)
        my_break()
      else:
        main_angle=angleFromCoordinate(source['Latitude'],source['Longitude'],destination['lat'],destination['lon'])#testt
        present_angle=heading_angle()
        diff=float(present_angle)-main_angle
        print("heading angle is "+str(present_angle))
        print("main angle is "+str(main_angle))
        if(abs(diff)>40):
          if(diff>180):
            print("Front_left")
            my_front_left()
            sleep(1)
            my_break()
            sleep(0.5)
          else:
            print("Front_right")
            my_front_right()
            sleep(1)
            my_break()
            sleep(0.5)
        else:
          print("Front")
          my_front()
          sleep(1)
          my_break()
          sleep(0.5)
      source = getmyloc()
             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()



        
 
      
    
    

