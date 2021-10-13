import os
from flask import Flask, render_template
from flask_socketio import SocketIO, send

# Configuracion
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

# Cargamos la plantilla HTML con el frontend.
@app.route('/')
def index():
    return render_template('index.html')

# Recibirá los nuevos mensajes y los emitirá por socket.
@socketio.on('message') # recibir msj del lado del cliente al servidor (EVENTO) . 
def handle_Message(msg): # Comenzamos a manejar el msj.
    print('Mensaje: ' + msg) #mensaje en terminal.
    send(msg, broadcast = True) #mensaje al lado del cliente con su transmision.

# Iniciamos
if __name__ == '__main__':
    socketio.run(app)
