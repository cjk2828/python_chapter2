import socket
BSIZE = 1000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.bind(("",8001))

s.sendto("Hello UDP server".encode(),("127.0.0.1",8000))
# print(s)

reply, saddr = s.recvfrom(BSIZE)

print(reply.decode())
print(saddr)
s.close()