# udp - client - socket
import socket

ip_port = ('127.0.0.1', 9000)
udp_sk = socket.socket(type=socket.SOCK_DGRAM)
udp_sk.sendto(b"hi", ("127.0.0.1", 9000))
data, addr = udp_sk.recvfrom(1024)
print(data)
