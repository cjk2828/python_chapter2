#!/usr/bin/python3
import socket

host = ""
port = 12282
BUFF_SIZE = 128
BACKLOG = 5

conn_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (host,port)
conn_sock.bind(server_address)

conn_sock.listen(BACKLOG)

while True:
    print("\nwaiting for request... ")
    data_sock, address = conn_sock.accept()
    print("echo request from {} port {}".format(address[0],address[1]))
    message = data_sock.recv(BUFF_SIZE)

    if message:
        print("recevied message: {} \n".format(message.decode()))
        data_sock.sendall(message)

    data_sock.close()