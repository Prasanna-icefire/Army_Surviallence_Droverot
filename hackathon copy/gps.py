import socketio
sio=socketio.Client()
sio.connect('http://13.232.28.46:8000')
@sio.on("gps-follow")
def on_message(data):
	print(data)
	f=open("gps.txt", "w")
	f.write(data)
"""	
f=open("gps.txt", "r")
a=f.read()
"""
