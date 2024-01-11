import socket 
import os 

HOST = '127.0.0.1'
PORT = 12345
SERVER_PATH = 'Server_Files/'
SIZE = 1024
FORMAT = "utf-8"

def handle_client(client_socket):
    request = client_socket.recv(SIZE).decode()
    if request.startswith('UPLOAD'):
        filename = request.split(' ') [1]
        with open(SERVER_PATH + filename, 'w') as file:
            while True:
                data = client_socket.recv(SIZE).decode(FORMAT)
                if not data:
                    break
                file.write(data)
            print(f'File {filename} uploaded.')
    elif request.startswith('DELETE'):
        filename = request.split(' ') [1]
        file_path = SERVER_PATH + filename
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f'File {filename} deleted.')
        else:
            print(f'File {filename} not found.')
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"Server listening on {HOST}:{PORT}") 

    if not os.path.exists(SERVER_PATH):
        os.makedirs(SERVER_PATH)
    
    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}") 
        handle_client(client_socket)

if __name__ == '__main__':
    main()
