from select import select
import socket

# 创建套接字作为关注的 IO
s = socket.socket()
s.bind(("127.0.0.1", 8888))
s.listen(5)

# 添加到关注列表
rlist = [s]
wlist = []
xlist = []

# 监控关注的 IO
while True:
    rs, ws, xs = select(rlist, wlist, xlist)
    # 遍历返回值列表, 确定就绪的 IO
    for r in rs:
        # s 就绪, 有客户请求链接
        if r is s:
            c, addr = s.accept()
            print("Connect from", addr)
            # 将客户端连接套接字加入关注
            rlist.append(c)
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close(0)
                continue
            print("Receive:", data.decode())
            # r.send(b"OK")
            # send 这个是可以自行控制的, 可以放入 wlist 照片那个主动操作此 IO
            wlist.append(r)

    for w in ws:
        w.send(b"OK")
        wlist.remove(w)
    for x in xs:
        pass
