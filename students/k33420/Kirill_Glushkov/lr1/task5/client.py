import socket
import json

def send_request(request):
    server_address = ('localhost', 8080)
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)
    
    client_socket.sendall(request.encode('utf-8'))
    
    response = client_socket.recv(1024).decode('utf-8')
    
    print(response)
    
    client_socket.close()

if __name__ == '__main__':
    while True:
        choice = input("Enter 'GET' to retrieve marks or 'POST' to add marks: ")

        if choice.upper() == 'GET':
            request = "GET /marks HTTP/1.1\r\n\r\n"
        elif choice.upper() == 'POST':
            name = input("Enter discipline name: ")
            marks_str = input("Enter comma-separated marks: ")
            marks = [int(mark) for mark in marks_str.split(',')]
            data = {'name': name, 'marks': marks}
            request_data = json.dumps(data)
            request = f"POST /add_marks HTTP/1.1\r\nContent-Length: {len(request_data)}\r\nContent-Type: application/json\r\n\r\n{request_data}"
        else:
            continue
        
        send_request(request)