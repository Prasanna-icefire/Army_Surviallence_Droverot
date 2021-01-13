import os
from time import sleep
while True:
   f=open("rov.txt","r")
   data=f.read()
   f.close()
   if(data):
     if(data=='x'):
       os.system("python automatic.py") 
     elif(data=='w'):
       sleep(2)
       os.system("python osrover.py")  
     elif(data=='e'):
       exit()   
       