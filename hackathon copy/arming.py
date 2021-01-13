import os
while(True):
 f=open("arm.txt","r")
 c=f.read()
 f.close()
 if(c=='e'):
  os.system('python robotic_arm.py')
 elif(c=='d'):
  os.system('python robotic_arm2.py')
 else:
  exit() 