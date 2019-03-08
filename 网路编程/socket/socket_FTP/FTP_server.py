import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 8888))
sk.listen(3)
conn, addr = sk.accept()
print("Connect from:", addr)
f = open("aa.jpg", "wb")
while True:
    data = sk.recv(1024)
    if not data:
        break
    f.write(data)
conn.close()
sk.close()
