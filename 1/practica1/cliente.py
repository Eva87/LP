import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = 'localhost'
puerto = 52816

mensaje = "This is the message. It will be repeated."

print("connect to %s port %d" %(ip,puerto))
cliente.connect((ip, puerto))
print("Sending: %s" %mensaje)
cliente.send(bytes(mensaje, "utf-8"))

iterador = 0
while iterador < len(mensaje):
    respuesta = cliente.recv(16)
    iterador += len(respuesta)
    print("Received: %s" %respuesta)

print("Closing socket")
cliente.close()