 from gpiozero import Servo
 from time import sleep
 clasp = Servo(15)
 servo = Servo(14)

 clasp.value=1
 sleep(1)
 clasp.min()
 sleep(1)
 servo.value = -1
 sleep(1)
 servo.value = 0
 sleep(1)
 servo.value = 0.5
 sleep(1)
 clasp.value=-1
 sleep(1)

