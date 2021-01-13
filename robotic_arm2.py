from gpiozero import Servo
from time import sleep
clasp = Servo(15)
servo = Servo(14)
while True:
 servo.min()
 sleep(1)
 servo.max()
 sleep(1)
 servo.mid()
 sleep(1)
#clasp.min()
#sleep(1)
#clasp.max()
#sleep(1)
