# tcp - server - socket

import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 8000))
sk.listen()
conn, addr = sk.accept()
conn.send(b"hello")
data = conn.recv(1024)
print(data)
conn.close()
sk.close()