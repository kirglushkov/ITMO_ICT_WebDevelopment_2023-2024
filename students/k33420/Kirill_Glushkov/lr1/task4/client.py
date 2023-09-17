import socket
import threading

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            break

def send_message(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode())

        if message == 'exit':
            client_socket.close()
            break

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))
threading.Thread(target=receive_messages, args=(client_socket,)).start()
threading.Thread(target=send_message, args=(client_socket,)).start()