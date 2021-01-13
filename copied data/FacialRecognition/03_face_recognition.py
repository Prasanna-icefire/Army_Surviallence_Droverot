''''
Real Time Face Recogition
	==> Each face stored on dataset/ dir, should have a unique numeric integer ID as 1, 2, 3, etc                       
	==> LBPH computed model (trained faces) should be on trainer/ dir
Based on original code by Anirban Kar: https://github.com/thecodacus/Face-Recognition    

Developed by Marcelo Rovai - MJRoBot.org @ 21Feb18  

'''
import asyncio
import cv2
import numpy as np
import os 
import requests
import base64
import time



recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX
key = ''
#iniciate id counter
id = 0
base64Img =''

# names related to ids: example ==> Marcelo: id=1,  etc
names = ['None', 'Vinu', 'Anurag','aka'] 

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_BUFFERSIZE,1); 

cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height
frame_rate = 2
prev = 0

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:
    time_elapsed = time.time() - prev
    ret, img =cam.read()
    #time.sleep(0.5)
    if time_elapsed > 1./frame_rate:

        img = cv2.flip(img, -1) # Flip vertically

        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
           )

        for(x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

            # Check if confidence is less them 100 ==> "0" is perfect match 
            if (confidence < 100):
                id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
            else:


                cv2.imwrite('unknown.jpg',img)
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))
                with open("unknown.jpg", "rb") as img_file:
                    my_string = base64.b64encode(img_file.read())
#print(my_string)
                data ={'base64Img': my_string,'key':'LP!8RPSDE#w&rYx+Zk#Z%CNS&=jfE85PAM*DBXgGbaCShYyUSfbMk9R$Wx4?U*mh7FkK4&'};
#f=open("url.txt", "r")
#contents =f.read()
                r = requests.post(url = 'http://13.232.28.46:3000/upload/base64', data = data) 
#data1=response.json()
#print(response.status_code)     
                print(r.json())        
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
        cv2.imshow('camera',img) 

        k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
