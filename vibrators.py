import RPi.GPIO as GPIO    
from time import sleep 
import random   
GPIO.setwarnings(False)    
GPIO.setmode(GPIO.BOARD)  
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
while True:
	#f=open("sock.txt","r")
	data=chr(random.randrange(97, 97 + 3))
	print(data)
	if(data=='a'):
		GPIO.output(8, GPIO.HIGH) 
    		GPIO.output(10, GPIO.LOW)  
		sleep(5)
		GPIO.output(8, GPIO.LOW) 
    		GPIO.output(10, GPIO.LOW)
		sleep(1) 
	if(data=='b'):
		GPIO.output(16, GPIO.HIGH) 
    		GPIO.output(18, GPIO.LOW)  
		sleep(5)
		GPIO.output(16, GPIO.LOW) 
    		GPIO.output(18, GPIO.LOW) 
		sleep(1)
	if(data=='c'):
		GPIO.output(22, GPIO.HIGH) 
    		GPIO.output(24, GPIO.LOW)  
		sleep(5)  
		GPIO.output(22, GPIO.LOW) 
    		GPIO.output(24, GPIO.LOW)
		sleep(1)
