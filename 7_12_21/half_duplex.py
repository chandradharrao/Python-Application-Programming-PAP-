#two mode sequential communication
#two way communication but only one at a time

from os import truncate
from socket import * #then not socket.socket

port=5000
tsocket = socket(AF_INET,SOCK_STREAM)
tsocket.bind(("",port))
tsocket.listen(1)
print("server running.....")

while True:
    comm,client_Addr = tsocket.accept() #accept a connection

    while True:
        msg = comm.recv(2048).decode()
        print(">>",msg)
        if msg=="q":
            comm.close()
            break

        comm.send(input().encode())