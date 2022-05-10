#!/usr/bin/python3

import sys
import select
import socket
import errno
import os


host = ''
port = 10000
BACKLOG = 5

conn_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
conn_sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
conn_sock.setblocking(0)

conn_sock.bind((host,port))
conn_sock.listen(BACKLOG)

print('Server running...')
print('Enter quit to stop server ...')

#read, write, exception lists with sockets to poll
rd_list, wd_list,err_list = [sys.stdin,conn_sock],[],[]

while True:
    #check for events
    readable,writable,exception = select.select(rd_list,wd_list,err_list)
    for sock in readable:
        if sock is conn_sock:
            data_sock,client_address = conn_sock.accept()
            rd_list.append(data_sock)
        elif sock is sys.stdin:
            key = input()
            if key.upper() == "QUIT":
                sys.exit(0)
        else:
            data = sock.recv(1024)
            if not data: # connection closed by client
                sock.close()
                rd_list.remove(sock)
            else: #echo received message
                print("got request from ",sock.getpeername())
                print("received message :",data.decode())
                sock.sendall(data)
