import os
import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = 'localhost'
port = 5005
print("starting up on %s port %d" % (ip, port))
servidor.bind((ip, port))
servidor.listen(1)

ap = [" ", " "]
ap1 = [" ", " "]
while True:
    print("Waiting for a connection.")
    cliente, direccion = servidor.accept()
    print("Conection from: %s %d" % (direccion[0], direccion[1]))
    resp = cliente.recv(44)
    respuesta = resp.decode()
    print("Received: %s" % respuesta)
    respArray = respuesta.split()
    conex = (respArray[2], "200", "OK")
    respArray[0] = ' '.join(conex)

    ruta = '../prac4/html'
    filename =  ruta + respArray[1]
    ruta2= ruta + '/form.html'
    tam = os.path.getsize(ruta2)
    file = open(ruta2, 'rb')
    text = file.read(tam)
    file.close()

    if "fname=" in respuesta:
        nombre = respuesta.split('fname=')
        ap = nombre[1].split('&lname=')
        ap1=ap[1].split(' HTTP')

    contenido = {
        'Cache-Control': 'no-store',
        'Content-Length': tam,
        'Content-Type': 'text/html; charset=utf8',
        'Connection': 'close',
        'Contenido del fichero': ap[0] + " " + ap1[0],
    }
    respCont = ''.join('%s: %s\n' % (k, v) for k, v in contenido.items())
    print(" ")

    print(respCont)
    print(text)
    cliente.send(respArray[0].encode())
    cliente.send(respCont.encode())
    cliente.send('\n'.encode())
    cliente.send(text)
    cliente.close()
