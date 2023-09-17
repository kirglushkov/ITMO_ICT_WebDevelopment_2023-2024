import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_address = ('localhost', 12345)
sock.connect(server_address)
print('Connected to {}:{}'.format(*server_address))

try:
    message = 'i want to solve pythagorean theorem'
    sock.sendall(message.encode())

    data = sock.recv(4096)
    print('Received message from server:', data.decode())

    a = int(input('Enter the value of a: '))
    sock.sendall(str(a).encode())

    data = sock.recv(4096)
    print('Received message from server:', data.decode())
    b = int(input('Enter the value of b: '))
    sock.sendall(str(b).encode())

    data = sock.recv(4096)
    print('Received message from server:', data.decode())

finally:
    sock.close()