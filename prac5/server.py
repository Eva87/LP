import os
import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = 'localhost'
port = 5005
print("starting up on %s port %d" % (ip, port))
servidor.bind((ip, port))
servidor.listen(2)

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
    ruta = '../prac5/html'
    filename = ruta + respArray[1]
    ruta2 = ruta + '/form.html'
    tam = os.path.getsize(ruta2)
    file = open(ruta2, 'rb')
    text = file.read(tam)

    if "fname=" in respuesta:
        nombre = respuesta.split('fname=')
        ap = nombre[1].split('&lname=')
        ap1 = ap[1].split(' HTTP')

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
    file.close()
    cliente.send(respArray[0].encode())
    cliente.send(respCont.encode())
    cliente.send('\n'.encode())
    cliente.send(text)

    textopost=cliente.recv(1024)
    textopost=textopost.decode()
    #print(textopost)
    subtextopost = textopost.split('\n')
    stp1=subtextopost[1].split(':')
    stp2=subtextopost[2].split(':')
    stp3=subtextopost[3].split(':')
    stp4=subtextopost[4].split(':')
    stp5=subtextopost[5].split(':')
    stp6=subtextopost[6].split(':')


    diccionariopost = {
        'User-Agent': stp1[1],
        'Accept': stp2[1],
        'Accept-Language': stp3[1],
        'Accept-Encoding': stp4[1],
        'Connection': stp5[1],
        'Upgrade-Insecure-Requests': stp6[1],
    }

    print("Inicio datos del formulario ")
    print(diccionariopost)
    print(ap[0] + " " + ap1[0])
    print("Fin datos del formulario ")
    cliente.close()
