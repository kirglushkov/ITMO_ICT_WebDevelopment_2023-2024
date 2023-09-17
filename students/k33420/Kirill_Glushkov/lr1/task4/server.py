import socket
import threading

# Define constants for server IP address and port
SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen(5)

connected_clients = []

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
            if not message:
                connected_clients.remove(client_socket)
                client_socket.close()
                break
            
            for client in connected_clients:
                if client != client_socket:
                    client.send(message.encode())
        
        except:
            continue

def accept_clients():
    while True:
        client_socket, client_address = server_socket.accept()

        connected_clients.append(client_socket)

        threading.Thread(target=handle_client, args=(client_socket,)).start()

threading.Thread(target=accept_clients).start()