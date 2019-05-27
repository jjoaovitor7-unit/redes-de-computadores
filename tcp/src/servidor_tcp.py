# -*- coding: utf-8 -*-

import socket
import datetime

HOST = '127.0.0.1' # Endereço IP do Servidor
PORT = 8080        # Porta que o Servidor está

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen()

while True:
    conexao = datetime.datetime.now()
    conexao_horario = '[' + str(conexao.hour) + ':' + str(conexao.minute) + ':' + str(conexao.second) + ']'
    conn, cliente = tcp.accept()
    
    cliente = str(cliente).replace('(', '[')
    cliente = str(cliente).replace(')', ']')
    
    print(conexao_horario, '[Conexão Realizada]', str(cliente))
    
    while True:
        msg = conn.recv(1024)
        
        if not msg:
            break
            
        mensagem = datetime.datetime.now()
        mensagem_horario = '[' + str(mensagem.hour) + ':' + str(mensagem.minute) + ':' + str(mensagem.second) + ']'
        print(mensagem_horario, cliente, msg)
    
    desconexao = datetime.datetime.now()
    desconexao_horario = '[' + str(desconexao.hour) + ':' + str(desconexao.minute) + ':' + str(desconexao.second) + ']'   
    print(desconexao_horario, '[Conexão Finalizada]', cliente)
    conn.close()
