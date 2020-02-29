import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = 'localhost'
port = 52816
print("starting up on %s port %d" % (ip, port))
servidor.bind((ip,port))
servidor.listen(1)
i = 0

while True:
    if i == 0:
        print("Waiting for a connection.")
        cliente, direccion = servidor.accept()
        print("Conection from: %s %d" % (direccion[0], direccion[1]))
    respuesta = cliente.recv(16)
    if respuesta:
        print("Received: %s" % respuesta)
        print("Sending data back to the client")
        cliente.send(respuesta)
        i+=1
    else:
        print("no more data from: %s %d" %(direccion[0], direccion[1]))
        cliente.close()
        i=0