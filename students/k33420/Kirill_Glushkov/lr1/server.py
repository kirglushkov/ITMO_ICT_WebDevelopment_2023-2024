import socket
import math

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific IP address and port
server_address = ('localhost', 12345)
print('Starting the server on {}:{}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)
print('Waiting for a connection...')

while True:
    # Accept a new connection
    connection, client_address = sock.accept()
    print('Connection established from', client_address)
    try:
        while True:
            data = connection.recv(4096)
            message = data.decode()
            if message == 'i want to solve pythagorean theorem':
                response = 'ok, provide me: a'
                connection.sendall(response.encode())
                data = connection.recv(4096)
                a = int(data.decode())
                connection.sendall('provide me: b'.encode())
                data = connection.recv(4096)
                b = int(data.decode())
                c = math.sqrt(a*a + b*b)
                response = 'The solution is: a={}, b={}, c={}'.format(a, b, c)
                connection.sendall(response.encode())
            else:
                pass
    finally:
        connection.close()