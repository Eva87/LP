import socket

def conexion(client):
    petition = client.recv(16)
    print("Received: %s" % petition)
    print("sending data back to the client.")
    client.send(petition)


ip = "0.0.0.0"
puerto = 52816
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("starting up on localhost port: %d " %puerto)

servidor.bind((ip, puerto))
servidor.listen(1)
print("Waiting for a connection:")

while True:
    cliente, direccion = servidor.accept()
    print("connection from ('%s',%d)" % (direccion[0], direccion[1]))
    conexion = target=conexion, args=(cliente,)
    conexion.start()

print("no more data from ('%s', %d)" % (direccion[0], direccion[1]))