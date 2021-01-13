import requests as reqs
import urllib3
url = 'http://13.232.28.46:3000/getcmds'
cookies={"key":"LfhnMr*at2xq@EtP%pSU#gwyT4s+Y$vPabdN3q=CqceJQCZ44bJ*+_gM#*KyZqVMhD2jBawe!$YAf=jm"}
response = reqs.get(url,cookies=cookies)       
data=response.json()
#print(response.status_code)     
print(data['move'])

