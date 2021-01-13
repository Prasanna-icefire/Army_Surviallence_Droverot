from gpiozero import DistanceSensor
from time import sleep
sensor = DistanceSensor(echo =16 ,trigger = 21)
i=0
while True:
        if(i%10==0):
	 print('Distance: ',sensor.distance * 100)
	 f = open("ultra.txt","w")
         f.write(str(sensor.distance*100))
         f.close()
        i=i+1