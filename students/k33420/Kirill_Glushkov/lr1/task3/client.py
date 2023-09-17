import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 8080)
client_socket.connect(server_address)

try:
    client_socket.sendall('GET / HTTP/1.1\r\nHost: {}\r\n\r\n'.format(server_address[0]).encode())

    response = client_socket.recv(4096).decode()
    print('Received HTML code:\n')
    print(response)

finally:
    client_socket.close()