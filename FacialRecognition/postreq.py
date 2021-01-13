import requests 
import base64
with open("unknown.jpg", "rb") as img_file:
    my_string = base64.b64encode(img_file.read())
#print(my_string)
key=''
base64Img=''
data ={'base64Img': 'my_string','key':'LP!8RPSDE#w&rYx+Zk#Z%CNS&=jfE85PAM*DBXgGbaCShYyUSfbMk9R$Wx4?U*mh7FkK4&'};
#f=open("url.txt", "r")
#contents =f.read()
r = requests.post(url = 'http://13.232.28.46:3000/upload/base64', data = data) 
#data1=response.json()
#print(response.status_code)     
print(r.json())  
