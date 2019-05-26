# -*- coding: utf-8 -*-

import socket

HOST = '127.0.0.1' # Endereco IP do Servidor
PORT = 8080        # Porta que o Servidor esta

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen()

while True:
    conn, cliente = tcp.accept()
    print('Conectado por', cliente)
    while True:
        msg = conn.recv(1024)
        if not msg:
            break
        print(cliente, msg)   
    print('Finalizando conexão do cliente', cliente)
    conn.close()
