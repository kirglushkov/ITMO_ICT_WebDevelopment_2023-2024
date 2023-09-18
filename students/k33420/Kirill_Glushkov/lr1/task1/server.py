import socket
import math

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific IP address and port
server_address = ('localhost', 12345)
print('Starting the server on {}:{}'.format(*server_address))
sock.bind(server_address)

while True:
    print('\nОжидание сообщениея...')
    data, adress = sock.recvfrom(4096)

    print('Получено сообщение от {}: {}'.format(adress, data.decode()))
    message = b'Hello, client'
    sock.sendto(message, adress)
