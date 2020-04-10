import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = 'localhost'
port = 5005
print("starting up on %s port %d" % (ip, port))
servidor.bind((ip, port))
servidor.listen(1)

while True:
    print("Waiting for a connection.")
    cliente, direccion = servidor.accept()
    print("Conection from: %s %d" % (direccion[0], direccion[1]))
    resp = cliente.recv(44)
    respuesta = resp.decode()
    print("Received: %s" % respuesta)

    mensajeget = respuesta.split('D')
    mensajegetimp = mensajeget[1].split('%20')
    mensajemandar = mensajegetimp[0] + " " + mensajegetimp[1]

    htt = " HTTP/1.1 200 OK "
    print(htt)
    respuesta = mensajeget[1]

    contenido = {
        'Cache-Control': 'no-store',
        'Content - Length': 15,
        'Content-Type': 'text/plain;charset=utf-8',
        'Connection': 'close',
    }
    print(" ")

    print(htt)
    print(contenido)
    print(mensajemandar)
    cliente.send(mensajemandar.encode())
    cliente.send('\n'.encode())
    cliente.close()

