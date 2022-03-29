import socket

s = socket.socket()
s.connect(("127.0.0.1",9000))
print(s)

s.send("Hello socket".encode())