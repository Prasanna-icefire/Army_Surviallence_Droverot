import socketio
import ast
import json
sio=socketio.Client()
sio.connect('http://13.232.28.46:8000')
@sio.on("gps-follow")
def on_message(data):
  #print(data[b'lat'])
  stri="{'lat':"+data['lat']+",'lon':"+data['lon']+"}"
  f = open("descoor.txt","w")
  print(stri)
  f.write(stri)
  f.close()