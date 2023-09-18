import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


message = b'Hello, server'
server_address = ('localhost', 12345)
sock.sendto(message, server_address)

data, _ = sock.recvfrom(4096)
print('Получено сообщение от сервера:', data.decode())

sock.close()