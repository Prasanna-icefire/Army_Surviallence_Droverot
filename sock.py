import socketio
sio=socketio.Client()
sio.connect('http://13.232.28.46:8000')
#print(sio.sid)
#sio.emit('from-client',{'foo':'bar'})
"""
@sio.on("arm")
def on_message(data):
	print(data)	
sio.disconnect()	
@sio.on("gps-follow")
def on_message(data):
	print(data)
@sio.on("learn_faces")
def on_message(data):
	print(data)	
"""
@sio.on("rov")
def on_message(data):
	print(data)
	
