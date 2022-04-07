#!/usr/bin/python3
import socket

host = ""
port = 12282
BUFF_SIZE = 128

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = (host,port)
sock.bind(server_address)

while True:
    print("\nwaiting for request... ")
    message, client_address = sock.recvfrom(BUFF_SIZE)
    print("echo request from {} port {}".format(client_address[0],client_address[1]))
    try:
        if int(message.decode()) % 2 == 0:
            st = "짝수입니다"
            print(st)
        else:
            st = "홀수입니다"
            print(st)
    except:
        st = "숫자가 아닙니다"
        print(st)

    sock.sendto(st.encode(), client_address)

sock.close()
