# tcp - client - socket

import socket

sk = socket.socket()
sk.connect(("127.0.0.1", 8000))
sk.send(b"hello")
data = sk.recv(1024)
print(data)
sk.close()