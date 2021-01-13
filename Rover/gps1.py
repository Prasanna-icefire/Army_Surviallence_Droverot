#this generates source cooordinates
import serial
import time
import string
import pynmea2

while True:
	port="/dev/ttyAMA0"
	ser=serial.Serial(port, baudrate=9600, timeout=0.5)
	dataout = pynmea2.NMEAStreamReader()
	newdata=ser.readline()
	#print(newdata)
	if newdata[0:6] == b"$GPGGA":
		print("Entered if")
		newmsg=pynmea2.parse(newdata.decode("utf-8"))
		lat=newmsg.latitude
		lng=newmsg.longitude
		gps = {"Latitude":str(lat),"Longitude":str(lng)}
		print(gps)
		f=open("source.txt","w")
		f.write(str(gps))