from socket import *
from time import sleep, ctime

sockfd = socket()
sockfd.bind(('127.0.0.1', 8888))
sockfd.listen(3)

# 设置非阻塞状态
# sockfd.setblocking(False)

# 设置超时时间
sockfd.settimeout(10)

while True:
    print("Waiting for connect...")
    try:
        connfd, addr = sockfd.accept()
    except BlockingIOError:
        sleep(2)
        print("%s connect error" % ctime())
        continue
    except timeout:
        print("timeout.......")
    else:
        print("Connect from", addr)
