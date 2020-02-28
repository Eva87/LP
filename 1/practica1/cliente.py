import socket

servidor = "localhost"
puerto = 33060
mensaje = "This is the message it will be repeated."
mensaje = mensaje.encode()

Cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Cliente.connect((servidor, puerto))
print("Sending %s" % mensaje)

while True:
    Cliente.send(mensaje)
    respuesta = Cliente.recv(16)
    print ("received: %s" %respuesta)