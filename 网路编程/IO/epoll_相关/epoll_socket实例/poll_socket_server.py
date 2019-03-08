
from socket import *
from select import *


"""
P = poll() 改成 epoll()
EPOLLIN EPOLLERR 所有的 poll 的事件前面加个 E 就变成 epoll 的了
改动非常简单
"""

# 创建要关注的IO
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(5)

# 创建poll对象
p = epoll()

# 建立查找字典
fdmap = {s.fileno(): s}  # 利用 fileno 的唯一标识来创建一个映射到具体对象

# 注册IO
p.register(s, EPOLLIN | EPOLLERR)  # 监听 读写事件

# 循环监控
while True:
    events = p.poll()  # 阻塞
    # 遍历列表，处理IO
    for fd, event in events:
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print("Connect from", addr)
            # 添加新的注册IO
            p.register(c, EPOLLIN | EPOLLHUP)
            fdmap[c.fileno()] = c
        elif event & EPOLLHUP:  # 与运算, event 已经有了, EPOLLHUP 没有就是假
            print("客户端退出")
            p.unregister(fd)  # 取消关注
            fdmap[fd].close()
            del fdmap[fd]
        elif event & EPOLLIN:  # 与运算, event 已经有了, EPOLLIN 没有就是假
            data = fdmap[fd].recv(1024)
            # if not data:
            #     p.unregister(fd) #取消关注
            #     fdmap[fd].close()
            #     del fdmap[fd]
            print("Receive:", data.decode())
            fdmap[fd].send(b'Receive your msg')
