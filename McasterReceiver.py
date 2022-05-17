import socket
import struct

INADDR_ANY = '203.250.137.160'
MCAST_ADDR = "224.0.0.1"
MCAST_PORT = 9000

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((INADDR_ANY,MCAST_PORT))


# mreq = socket.inet_aton(MCAST_ADDR)+socket.inet_aton(INADDR_ANY)
mreq = struct.pack("4s4s",socket.inet_aton(MCAST_ADDR),socket.inet_aton(INADDR_ANY))
sock.setsockopt(socket.IPPROTO_IP,socket.IP_ADD_MEMBERSHIP,mreq)


while 1:
    try:
        data,addr = sock.recvfrom(1024)
    except socket.error as e:
        pass
    else:
        print("\nI got message from {} {}".format(addr[0],addr[1]))
        print("Message:")
        print(data.decode())