from socket import *

server={
    'name':'localhost',
    'port':5000
}

socket = socket(AF_INET,SOCK_STREAM) #create client side socket
socket.connect((server['name'],server['port']))
print("client has been started...")

while True:
    sent = input()
    socket.send(sent.encode())

    #recieve from server
    msg = socket.recv(2048).decode()
    print(msg)

    if sent=="q":
        print("closing client connection...")
        socket.close()
        quit()
