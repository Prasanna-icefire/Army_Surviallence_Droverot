import socketio
sio=socketio.Client()
sio.connect('http://13.232.28.46:8000')
@sio.on("add")
def on_message(data):
	print(data)
	f=open("add.txt", "w")
	f.write(data)
sio.emit('train',{'response': 'my response'})	
@sio.on("learn_faces")
def on_message1(data):
	print(data)
	f=open("add.txt", "w")
	f.write(data)
sio.emit('training-completed',{'response': '200'})    