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
    data_sock.sendall("HTTP/1.0 200 OK\r\n"
          "Context-Type: text/html\r\n\r\n"
          "<HTML><BODY>"
          "<H1>Hello,World!</H1>"
          "</BODY></HTML>".encode())

    data_sock.close()