# -*- coding: utf-8 -*-

import socket
import datetime

HOST = '127.0.0.1' # Endereço IP do Servidor
PORT = 8080        # Porta que o Servidor está

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)

while True:
    msg, cliente = udp.recvfrom(1024)
    cliente = str(cliente).replace('(', '[')
    cliente = str(cliente).replace(')', ']')
    
    if msg:
        mensagem = datetime.datetime.now()
        mensagem_horario = '[' + str(mensagem.hour) + ':' + str(mensagem.minute) + ':' + str(mensagem.second) + ']'
        print(mensagem_horario, cliente, msg)

udp.close()
