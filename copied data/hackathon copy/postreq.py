import requests 
import base64
with open("my_image.jpg", "rb") as img_file:
    my_string = base64.b64encode(img_file.read())
#print(my_string)
key=''
base64Img=''
data ={'key':'LfhnMr*at2xq@EtP%pSU#gwyT4s+Y$vPabdN3q=CqceJQCZ44bJ*+_gM#*KyZqVMhD2jBawe!$YAf=jm'};
#f=open("url.txt", "r")
#contents =f.read()
r = requests.post(url = 'http://13.232.28.46:3000/cookie', data = data) 
#data1=response.json()
#print(response.status_code)     
print(r.json())  

     
