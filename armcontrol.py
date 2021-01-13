import os
f=open("arm.txt","r")
d=f.read()

while True:
 if d:
  if(d=='e'):
   os.system("python robotic_arm.py")
   time.sleep(10)
  elif(d=='d'):
   os.system("python robotic_arm2.py")
   time.sleep(10)
  else:
   f.close()
   exit()
