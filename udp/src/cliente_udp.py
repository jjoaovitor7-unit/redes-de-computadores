import socket

HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 8080            # Porta que o Servidor esta

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

print('Para sair use CTRL+C')
msg = input('')
msg = bytes(msg, 'utf8')

while msg != '\x11':
    udp.sendto(msg, dest)
    msg = input()
    msg = bytes(msg, 'utf8')
udp.close()
