import socket

s = socket.socket(socket.AF_INET)
s.bind(("127.0.0.1", 9000))
s.listen(5)
ds,caddr = s.accept()

print(s)
print(ds)
print(caddr)

message = ds.recv(1000)

print(message.decode())