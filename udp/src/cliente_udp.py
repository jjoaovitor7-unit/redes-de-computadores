# -*- coding: utf-8 -*-

import socket
import matplotlib.pyplot
from ping3 import ping, verbose_ping

HOST = '127.0.0.1' # Endereço IP do Servidor
PORT = 8080        # Porta que o Servidor está

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

x_lista = []
ping_lista = []

print('Para sair use CTRL+C')
print('Opções:\nping\nperda de pacote')
msg = input('')
msg = bytes(msg, 'utf8')

#http://condor.depaul.edu/sjost/lsp121/documents/ascii-npr.htm
try:
     
     while msg != '\x11':
         verif = msg.decode('utf8')
     
         if verif == 'ping' or verif == 'Ping':
             print('----')
             print('Ping|')
             print('------------')
             ping_alvo = str(ping('127.0.0.1', unit='ms', size=56))
             print(ping_alvo)
             verbose_ping_alvo = verbose_ping('127.0.0.1', count=4)
             verbose_ping_alvo = str(verbose_ping_alvo).replace('None', '------------')
             print(verbose_ping_alvo)
             break
          
         elif verif == 'perda de pacote' or verif == 'perda de pacotes':
           print('-----------------------')
           print('Perda de Pacote (Teste)|')
           print('-----------------------')
           x = 0
           int(x)
               
           while True:
               x+=1
               
               if x >= 0 and x <= 50:
                   ping_alvo = str(ping('127.0.0.1', unit='ms', size=56))
                   ping_lista.append(ping_alvo)
                   x_lista.append(x)
                   pacotes = (x, ping_alvo)
                   pacotes = bytes(str(pacotes), 'utf8')
                   print(pacotes)
                    
                   if x >= 50 and x <= 51:
                       matplotlib.pyplot.xlabel('Pacote (nº)')
                       matplotlib.pyplot.ylabel('Ping')
                       matplotlib.pyplot.plot(x_lista, ping_lista)
                       matplotlib.pyplot.show()
                    
         else:
             udp.sendto(msg, dest)
             msg = input('')
             msg = bytes(msg, 'utf8')
        
except KeyboardInterrupt:
    print('Conexão finalizada.')
udp.close()
