import socketio
sio=socketio.Client()
sio.connect('http://13.232.28.46:8000')
@sio.on("rov")
def on_message(data):
  print(data)
  f = open("demo.txt","w")
  f.write(data)
  f.close()