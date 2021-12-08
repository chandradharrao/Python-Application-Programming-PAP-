#udp
'''
no streaming of packets between client and server
no guarentee of packet delivery
'''


import socket
hostname = socket.gethostname()
ipaddr = socket.gethostbyname(hostname)
print(ipaddr)
port=20000

#create socket
udpsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#bind address and port
udpsocket.bind((ipaddr,port))

print(f"udp server listening on {port}....")

while True:
    data,client_ip = udpsocket.recvfrom(1024) #recieve fro many client that sends
    
    print(f"{client_ip} has sent {data.decode()}")

    #send a replyt to client
    udpsocket.sendto(f" Server>> Hi client".encode(),client_ip)

