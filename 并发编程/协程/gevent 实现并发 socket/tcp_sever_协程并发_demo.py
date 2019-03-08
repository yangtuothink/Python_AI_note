import gevent
from gevent import monkey

monkey.patch_all()

from socket import *


def server():
    s = socket()
    s.bind(("127.0.0.1", 8090))
    s.listen()
    while True:
        c, addr = s.accept()  # 要在这里阻塞一下等待连接
        print("Connect from", addr)
        # handle(c)  # 处理客户端请求
        gevent.spawn(handle,c) # 利用协程来实现高并发

def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'ok')
    c.close()


server()
