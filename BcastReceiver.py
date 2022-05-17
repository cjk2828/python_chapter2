import socket

INADDR_ANY = '203.250.137.160'
BCAST_PORT = 9001

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)
sock.bind((INADDR_ANY,BCAST_PORT))

while 1:
    try:
        data,addr = sock.recvfrom(1024)
    except socket.error as e:
        pass
    else:
        print("\nI got message from {} {}".format(addr[0],addr[1]))
        print("Message:")
        print(data.decode())