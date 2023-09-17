import socket

def serve_index_page():
    # Open and read the index.html file
    with open('index.html', 'r') as file:
        html_content = file.read()

    return html_content

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 8080)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print('Server started. Listening on {}:{}'.format(*server_address))

while True:
    print('Waiting for a client connection...')
    client_socket, client_address = server_socket.accept()
    print('Accepted client connection from {}:{}'.format(*client_address))

    try:
        response = serve_index_page()
        client_socket.sendall(response.encode())

        # Close the connection
        client_socket.close()
        print('Response sent. Connection closed.')

    except Exception as e:
        print('An error occurred: {}'.format(e))