"""
import requests as reqs
import urllib3
url = 'http://13.232.28.46:3000/getcmds'
import time
cookies={"key":"LfhnMr*at2xq@EtP%pSU#gwyT4s+Y$vPabdN3q=CqceJQCZ44bJ*+_gM#*KyZqVMhD2jBawe!$YAf=jm"}
"""\
import socketio
sio=socketio.Client()
sio.connect('http://13.232.28.46:8000')
while True:
	@sio.on("rov")
	def on_message(data):
		print(data)
# response = reqs.get(url,cookies=cookies)       
# data=response.json()
# print(response.status_code)
# if data['move']:     
#  print(data['move'])

