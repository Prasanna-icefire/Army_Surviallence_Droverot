import socketio
sio=socketio.Client()
sio.connect('http://13.232.28.46:8000')
@sio.on("rover-op")
def on_message(data):
  print(data)
  f = open("rov.txt","w")
  f.write(data)
  f.close()
