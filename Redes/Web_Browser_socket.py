#Sockets

import socket

#Web Browser
meu_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
meu_socket.connect(('data.pr4e.org',80))

comando = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() #encoda o comando em bytes unicode UTF-8
meu_socket.send(comando)

while True:
    dados = meu_socket.recv(512)
    if len(dados) < 1:
        break
    print(dados.decode()) #desencoda os dados para o formato string unicode UTF-8
meu_socket.close()

