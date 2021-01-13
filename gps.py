import serial
import time
import string
import pynmea2
t=''
while True:
	port="/dev/ttyAMA0"
	ser=serial.Serial(port, baudrate=9600, timeout=0.5)

	dataout = pynmea2.NMEAStreamReader()
	newdata=ser.readline()
	t=str(newdata[0:6])
	print(t[2:])
	if t == "b'$GPGSV'":
		print("entered if")
		newmsg=pynmea2.parse(str(newdata))
		lat=newmsg.latitude
		lng=newmsg.longitude
		gps = "Latitude=" + str(lat) + "and Longitude=" + str(lng)
		print(gps)