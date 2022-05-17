import socket
import time

INADDR_ANY = '203.250.137.160'
SENDER_PORT = 10001
MCAST_ADDR = "224.0.0.1"
MCAST_PORT = 9000

count = 1

def do_mcast(sock):
    global count
    host = socket.gethostname()
    message = "Hello from {}.\n"\
              "This is my {}th message since {}.\n"\
              "I send this message to 224.0.0.1 every "\
              "10 seconds...\n".format(host,count,time_str)
    sock.sendto(message.encode(),(MCAST_ADDR,MCAST_PORT))

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((INADDR_ANY,SENDER_PORT))
sock.setsockopt(socket.IPPROTO_IP,socket.IP_MULTICAST_TTL,1)

time_str = time.ctime()

while 1:
    print("multicasting a messasge {}th time".format(count))
    do_mcast(sock)
    time.sleep(10)
    count = count+1