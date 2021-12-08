#https://stackoverflow.com/questions/50046578/i-understad-why-i-get-typeerror-getsockaddrarg-af-inet-address-must-be-tuple

import socket

udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

udp_socket.sendto("Hi i am the server!!!".encode(),('127.0.1.1',20000))

msg = udp_socket.recvfrom(1024) #recieve a messag from server

print(f"Recieved {msg[0].decode()} from {msg[-1]}") 