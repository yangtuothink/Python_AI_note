#!/user/bin/env python3
# coding=utf8
"""
AID httpserver v3.0
"""

from socket import *
import sys
import json
from threading import Thread

# 导入配置信息
from httpserver_config import *


# 向 frame 发送请求
def connect_frame(**kwargs):
    s = socket()
    try:
        s.connect(frame_address)
    except Exception as e:
        print(e)
        return
    # 将请求发送给　frame
    s.send(json.dumps(kwargs).encode())
    data = s.recv(4096).decode()
    return data


# 封装　httpserver 基本功能
class HTTPserver(object):
    def __init__(self, address):
        self.address = address
        self.create_socket()
        self.bind(address)

    # 创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, DEBUG)

    # 绑定监听地址和端口
    def bind(self, address):
        self.ip = address[0]
        self.port = address[1]
        self.sockfd.bind(address)

    # 　启动服务
    def serve_forever(self):
        self.sockfd.listen(10)
        print("Listen the port %d ..." % self.port)
        while True:
            try:
                connfd, addr = self.sockfd.accept()
                print("Connect from", addr)
            except KeyboardInterrupt:
                self.sockfd.close()
                sys.exit("退出　httpserver 服务")
            except Exception as e:
                print(e)
                continue
            client = Thread(target=self.handle, args=(connfd,))
            client.setDaemon(True)
            client.start()

    # 处理浏览器的　http 请求
    def handle(self, connfd):
        request = connfd.recv(4096)
        # 处理客户端断开
        if not request:
            connfd.close()
            return
        request_lines = request.splitlines()
        # 获取请求行
        request_lines = request_lines[0].decode("utf-8")
        print(request_lines)
        # 这里可以使用正则当然更好, 但是目前来说无大用
        # 获取请求方法，　请求内容
        tmp = request_lines.split(" ")
        method = tmp[0]
        path_info = tmp[1]

        data = connect_frame(method=method, path_info=path_info)

        self.response(connfd, data)

    # 　处理返回的数据内容
    def response(self, connfd, data):

        # 根据情况组织响应
        if data != "404":
            response_headlers = "HTTP/1.1 200 OK\r\n"
        else:
            response_headlers = "HTTP/1.1 404 Not Found\r\n"

        response_headlers += '\r\n'
        response_body = data
        response = response_headlers + response_body
        connfd.send(response.encode())
        connfd.close()


httpd = HTTPserver(ADDR)
httpd.serve_forever()  # 启动服务程序
