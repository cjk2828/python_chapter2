import socket

host = '203.250.133.88'
port = 12282
BUFF_SIZE = 128

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_address = (host,port)
print("connecting to {} port {}".format(server_address[0],server_address[1]))
sock.connect(server_address)

message = input("Enter File Name : ")
message = bytes(message.encode())

try:
    sock.sendall(message)
    data = sock.recv(BUFF_SIZE)
    if data.decode() == "NOT FOUND":
        print("{}".format(data.decode()))
    else:
        filename = message.decode()
        accessMode = "w"
        myfile = open(filename, accessMode)
        while True:
            print("{}".format(data.decode()),end = "")
            myfile.write(data.decode())
            data = sock.recv(BUFF_SIZE)
            if(data.decode()==""):
                myfile.close()
                break;
except Exception as e:
    print("Exception : {}".format(e))
sock.close()