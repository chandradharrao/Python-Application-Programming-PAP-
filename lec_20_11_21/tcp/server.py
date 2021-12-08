#https://pymotw.com/2/socket/tcp.html

from socket import *
port = 5000
socket = socket(AF_INET,SOCK_STREAM) #tcp connection
socket.bind(("",port))
socket.listen(1) #listen for 1 tcp connection from client
print("Welcome to the server")


'''
socket.accept()->(conn,address) accept client tcp connection : where conn is the new socket object usable to send and recieve data on the connection

address is the address of the clinet'''

while True:
    communication_socket,client_address = socket.accept() 
    try:
        print(f"connection from {client_address}")

        while True:
            sent = communication_socket.recv(2048).decode() #byte size-2048
            print(">>",sent)

            msg = input()
            communication_socket.send(msg.encode())

            if msg=='q': 
                break
    finally:
        print("closing server connection...")
        communication_socket.close()
        quit()
