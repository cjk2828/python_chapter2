import socket

host = '203.250.133.88'
port = 10070
BSIZE = 1000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.bind(("",8001))

server_address = (host,port)

message = input("Enter message : ")

try:
    s.sendto(message.encode(),server_address)
    reply, saddr = s.recvfrom(BSIZE)
    print(reply.decode())
    print(saddr)
except Exception as e:
    print("Exception: {}".format(e))

s.close()