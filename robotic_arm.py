from gpiozero import Servo
from time import sleep
clasp = Servo(15)
servo = Servo(14)
while True:
 clasp.min
 sleep(1)
 clasp.max
 sleep(1)
 servo.max
 sleep(1)
 servo.min
 sleep(1)

