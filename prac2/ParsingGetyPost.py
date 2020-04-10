

textoget ='GET /echo?message=%22Hello%20World!%22 HTTP/1.1\r\nHost: 127.0.0.1:5005\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36\r\nSec-Fetch-Dest: document\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signedexchange;v=b3;q=0.9\r\nSec-Fetch-Site: none\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-User: ?1\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: es-ES,es;q=0.9,en-GB;q=0.8,en;q=0.7\r\n\r\n'
textopost = 'POST /echo HTTP/1.1\r\nHOST: 127.0.0.1:5005\r\ncontent-type:application/x-www-form-urlencoded\r\ncontent-length: 23\r\n\r\nmessage=Hello World!!!!'

subtextoget = textoget.split()
print(subtextoget)

mensajeget = subtextoget[1].split('=')
mensajegetimp=""
for i in mensajeget:
    if i != mensajeget[0]:
        mensajegetimp=mensajegetimp+i
diccionarioget = {
    'method': subtextoget[0],
    'Url': subtextoget[1],
    'Version': subtextoget[2],
    'Host': subtextoget[4],
    'Connection': subtextoget[6],
    'Upgrade-Insecure-Requests:': subtextoget[8],
    'User-Agent': subtextoget[10]+" "+subtextoget[11]+" "+subtextoget[12]+" "+subtextoget[13]+" "+subtextoget[14]+" "+subtextoget[15]+" "+subtextoget[16]+" "+subtextoget[17]+" "+subtextoget[18]+" "+subtextoget[19],
    'Sec-Fetch-Dest': subtextoget[21],
    'Accept': subtextoget[23],
    'Sec-Fetch-Site': subtextoget[25],
    'Sec-Fetch-Mode': subtextoget[27],
    'Sec-Fetch-User': subtextoget[29],
    'Accept-Encoding': subtextoget[31]+" "+subtextoget[32]+" "+subtextoget[33],
    'Accept-Language': subtextoget[35],
    'Params':  {

        'message': [mensajegetimp,]
    }
}


print("diccionario get")
print(diccionarioget)


subtextopost = textopost.split()
contenttype = subtextopost[5].split(':')
print(subtextopost)

mensajepost = subtextopost[8].split('=')


mensajepostimp=""
mensajepostimp=mensajepostimp+mensajepost[1] + " "
j=0
for i in subtextopost:
    if j > 8:
        mensajepostimp=mensajepostimp+i
    j=j+1
diccionariopost = {
    'method': subtextopost[0],
    'Url': subtextopost[1],
    'Version': subtextopost[2],
    'Host': subtextopost[4],
    'content-type': contenttype[1],
    'content-length': subtextopost[7],

    'Params':  {
        'message': [mensajepostimp]
    }
}


print("diccionario post")
print(diccionariopost)