import socket

host_name = "www.pcu.ac.kr"
IP_addr = socket.gethostbyname(host_name)

print(IP_addr)

my_name = socket.gethostname()
print(my_name)
IP_addr = socket.gethostbyname(my_name)
print(IP_addr)