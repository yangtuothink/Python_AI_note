#!/user/bin/env python3
# coding=utf8

"""
模拟网站后端应用处理程序
httpserver v3.0
"""

from socket import *
import select
import json

# 导入配置文件
from settings import *
from views import *


# 创建应用类,　用于具体处理请求
class Application(object):
    def __init__(self):
        self.ip = frame_address[0]
        self.port = frame_address[1]
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.sockfd.bind(frame_address)

    def start(self):
        self.sockfd.listen(5)
        print("Listen the port %d" % self.port)
        rlist = [self.sockfd]
        wlist = []
        xlist = []
        while True:
            rs, ws, xs = select.select(rlist, wlist, xlist)
            # 循环检查是否就绪
            for r in rs:
                # 　判断加入　关注列表
                if r is self.sockfd:
                    connfd, addr = r.accept()
                    rlist.append(connfd)
                else:
                    # 接受 httpserver 的请求
                    request = r.recv(2048).decode()
                    if not request:
                        rlist.remove(r)
                        continue
                    self.handle(r, request)

    # 处理请求
    def handle(self, connfd, request):
        request = json.loads(request)
        method = request["method"]
        path_info = request["path_info"]
        print(path_info)
        if method == "GET":
            if path_info == "/" or path_info[-5:] == ".html":
                data = self.get_html(path_info)
            else:
                data = self.get_data(path_info)
        elif method == "POST":
            pass
        # 得到网页内容就发送　未得到就发送404
        if data:
            connfd.send(data.encode())
        else:
            connfd.send(b"404")

    # 处理网页
    def get_html(self, path_info):
        if path_info == "/":
            get_file = STATIC_DIR + "/index.html"
        else:
            get_file = STATIC_DIR + path_info
        try:
            fd = open(get_file, encoding="utf8")
            data = fd.read()
        except IOError:
            return
        return data

    # 处理数据
    def get_data(self, path_info):
        for url, func in urls:
            if path_info == url:
                return func()
        return "404"


app = Application()
app.start()  # 启动后端框架服务
