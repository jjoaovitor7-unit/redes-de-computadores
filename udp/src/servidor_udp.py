# -*- coding: utf-8 -*-

import socket

HOST = '127.0.0.1' # Endereco IP do Servidor
PORT = 8080        # Porta que o Servidor esta

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)

while True:
    msg, cliente = udp.recvfrom(1024)
    if msg:
        print(cliente, msg)
udp.close()
