import socket
import time

INADDR_ANY = '203.250.137.160'
SENDER_PORT = 10001
BCAST_ADDR = "255.255.255.255"
BCAST_PORT = 9001

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((INADDR_ANY,SENDER_PORT))
sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

host = socket.gethostname()
time_str = time.ctime()
count = 1

while 1:
    message = "Hello from {}.\n" \
              "This is my {}th message since {}.\n" \
              "I broadcast this message every " \
              "10 seconds...\n".format(host, count, time_str)
    sock.sendto(message.encode(), (BCAST_ADDR, BCAST_PORT))
    print('broadcasting a message {}th time'.format(count))
    time.sleep(10)
    count = count+1