import socket

PORT = 5050
SERVER = socket.gethostbyname('localhost')
FORMAT = 'utf-8'
connected = True
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER,PORT))


def client_send():
    dataFromServer = client_socket.recv(1024)
    print(dataFromServer.decode(FORMAT))
    msg = input("client->").encode()
    if msg == b'':
        msg = "None".encode()


    client_socket.send(msg)






while True:
    client_send()
