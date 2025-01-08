from flask import Flask, request
from flask_socketio import SocketIO, emit
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'example_secret_key'
socketio = SocketIO(app, async_mode='eventlet')

clients = {}
message_count = 0

@socketio.on('connect')
def handle_connect():
    global message_count
    clients[request.sid] = 0
    emit('server_message', {'message': 'Welcome to the WebSocket server!'}, broadcast=False)
    print(f"New client connected: {request.sid}")

@socketio.on('disconnect')
def handle_disconnect():
    if request.sid in clients:
        del clients[request.sid]
    print(f"Client disconnected: {request.sid}")

@socketio.on('client_message')
def handle_client_message(data):
    global message_count
    message = data.get('message', '')
    char_count = len(message)
    clients[request.sid] += 1
    message_count += 1
    emit('server_message', {'message': f'Your message has {char_count} characters.'}, broadcast=False)
    print(f"Received message from {request.sid}: {message}")

def send_report():
    while True:
        socketio.sleep(10)
        socketio.emit('server_message', {'message': f'Total messages received: {message_count}'}, room=None)

threading.Thread(target=send_report, daemon=True).start()

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
