import socket

host = '203.250.133.88'
port = 12282
BUFF_SIZE = 128

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server_address = (host,port)

message = input("Enter message : ")
message = bytes(message.encode())

try:
    bytes_sent = sock.sendto(message,server_address)
    data,address = sock.recvfrom(BUFF_SIZE)
    print("Received from server : {}".format(data.decode()))
except Exception as e:
    print("Exception : {}".format(e))

sock.close()