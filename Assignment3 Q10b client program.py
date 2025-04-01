import socket

HOST = '127.0.0.1'
PORT = 65432

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        data = client_socket.recv(1024)
        print("Received:", data.decode())
except Exception as e:
    print("Client error:", e)
