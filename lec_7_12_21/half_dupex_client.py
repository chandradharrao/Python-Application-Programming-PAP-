from socket import *

server={
   "name=":"localhost" ,
   "port":5000
}

tsocket = socket(AF_INET,SOCK_STREAM)
tsocket.connect((server['name'],server['port']))

tsocket.send(input().encode())
rcv = tsocket.recv(2048)
print(rcv.decode())