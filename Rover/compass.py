import socketio
sio=socketio.Client()
sio.connect('http://13.232.28.46:8000')
@sio.on("remitted-rov-coords")
def on_message(data):
	f=open("compass.txt","w")
	f.write(str(data["degree"]))
	print(str(data["degree"]))
	