import socket

host = '203.250.133.88'
port = 10124
BUFF_SIZE = 128

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_address = (host,port)
print("connecting to {} port {}".format(server_address[0],server_address[1]))
sock.connect(server_address)

message = input("Enter message : ")
message = bytes(message.encode())

try:
    sock.sendall(message)
    data = sock.recv(BUFF_SIZE)
    print("Received from server : {}".format(data.decode()))
except Exception as e:
    print("Exception : {}".format(e))

sock.close()