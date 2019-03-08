import socket

sk = socket.socket()
sk.connect(("127.0.0.1", 8888))
f = open("bb.jpg", "rb")
while True:
    data = f.read(1024)
    if not data:
        break
    sk.send(data)
f.close()
sk.close()
