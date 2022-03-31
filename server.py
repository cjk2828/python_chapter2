import socket
BSIZE = 1000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", 8000))

data,caddr = s.recvfrom(BSIZE)

# print(s)

print(data.decode())
print(caddr)

s.sendto("Nice to see you, Client".encode(),caddr)

s.close()