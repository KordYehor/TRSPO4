import socket
import threading
import time

def server():
    HOST = '127.0.0.1'
    PORT = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print('Server start working...')
        client_socket, address = s.accept()
        with client_socket:
            print('Connected to', address)
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                print('Received message from client:', data.decode())
                client_socket.sendall(b'Hello client')


def client():
    HOST = '127.0.0.1'
    PORT = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'Hello server!')
        data = s.recv(1024)
        print('Received message from server:', data.decode())


server_thread = threading.Thread(target=server)
server_thread.start()

time.sleep(2)
client_thread = threading.Thread(target=client)
client_thread.start()

server_thread.join()
client_thread.join()
