"""
Frame 程序配置文件
"""
from views import *


# 配置框架地址
frame_ip = "0.0.0.0"
frame_port = 8080
frame_address = (frame_ip, frame_port)

# 静态网页位置
STATIC_DIR = "./static"

#
urls = [
    ("/time", show_time),
    ("/hello", say_hello)
]



