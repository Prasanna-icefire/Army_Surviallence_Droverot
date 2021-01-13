import socketio
sio=socketio.Client()
sio.connect('http://13.232.28.46:8000')
#print(sio.sid)
#sio.emit('from-client',{'foo':'bar'})
@sio.on("arm")
def on_message(data):
	print(data['cmd'])
	f=open("arm.txt","w")
	f.write(data['cmd'])
	f.close()
		
"""
sio.disconnect()	
@sio.on("gps-follow")
def on_message(data):
	print(data)
@sio.on("learn_faces")
def on_message(data):
	print(data)	

@sio.on("rov")
def on_message(data):
	print(data)
	f=open("rov.txt", "w")
	f.write(data)
@sio.on("add")
def on_message(data):
	print(data)
	f=open("add.txt", "w")
	f.write(data)

@sio.on("")
def on_message(data):
	print(data)

@sio.event
def my_message1(data):
    print(data)
    sio.emit('my response')	


f=open("arm.txt", "r")
a=f.read()

f=open("rov.txt", "r")
a=f.read()

f=open("add.txt", "r")
a=f.read()
"""
