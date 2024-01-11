
import socket

# client config
HOST = '127.0.0.1'
PORT = 12345
SIZE = 1024
FORMAT = "utf-8"

def upload_file(filename):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        with open(filename, 'rb') as f:
            client.connect((HOST, PORT))
            client.send(f'UPLOAD {filename}'.encode()) 
            while True:
                data = f.read()
                if not data: 
                    print("File Upload Completed!")
                    break
                client.send(data)
        client.close()
    except:
        print(f"File {filename} does not exist on your system")

def delete_file(filename):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    client.send(f'DELETE {filename}'.encode())
    client.close()
    print(f"File: {filename} Deleted")

if __name__ == '__main__':
    command = ""
    while command != 'EXIT':
        try:
            entered = input("Enter 'UPLOAD' and the file name or 'DELETE' and the file name: ")
            command, filename = entered.split() 
            if not (command == 'UPLOAD' or command == 'DELETE' or command == 'EXIT') :
                print("Invalid input. Please use 'DELETE' or 'UPLOAD'")
                continue
            elif command == 'UPLOAD':
                upload_file(filename)
                print("Returned from the file upload! If you are done simply enter 'EXIT' to finish the program.")
            elif command == 'DELETE':
                delete_file(filename) 
                print("Returned from the file deletion! If you are done simply enter 'EXIT' to finish the program.")
        except:
            if(entered.strip() == "EXIT"):
                command = "EXIT"
            elif(entered.strip() == "UPLOAD" or entered.strip() == "DELETE"):
                print("Please enter a file name following your command!")
            else:
                print("Invalid input. Please use 'DELETE' or 'UPLOAD'")
