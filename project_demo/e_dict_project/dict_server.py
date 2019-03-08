from gevent import monkey

monkey.patch_all()
from socket import *
import pymysql
import sys
import time
import gevent
import os

# 制定输入格式,提供用户输入指引
if len(sys.argv) < 3:
    print(""" Start as: 
    python3 dict_server.py 0.0.0.0 8000
    """)
    sys.exit()

# 定义全局变量
HOST = sys.argv[1]  # sys.argv 获取命令行参数
PORT = int(sys.argv[2])
ADDR = (HOST, PORT)
DICT_TEXT = "e_dict.txt"


# 搭建网络连接
def main():
    # l连接数据库
    db = pymysql.connect("127.0.0.1", "root", "123456", "dict")

    # 创建套接字
    s = socket()
    # s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 保证端口复用的
    s.bind(ADDR)
    s.listen(5)

    # 僵尸进程的处理
    # signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    # 循环等待连接
    while True:
        try:
            c, addr = s.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit("服务器退出")
            continue

        # 创建子进程
        gevent.spawn(do_child, c, db)

        # 如果在 linux 下直接这样也可以
        # pid = os.fork()
        # if pid == 0:
        #     s.close()
        #     do_child(c, db)
        #     sys.exit()
        # else:
        #     c.close()


# 处理客户端请求
def do_child(c, db):
    while True:
        data = c.recv(1024).decode()
        print(c.getpeername(), ":", data)
        if not data or data[0] == "E":
            c.close()
            sys.exit()
        elif data[0] == "R":
            do_register(c, db, data)
        elif data[0] == "L":
            do_login(c, db, data)
        elif data[0] == "Q":
            do_query(c, db, data)
        elif data[0] == "H":
            do_history(c, db, data)

    return


def do_register(c, db, data):
    l = data.split(" ")
    name = l[1]
    passwd = l[2]
    cursor = db.cursor()

    sql = "select * from user where name = '%s' " % name
    cursor.execute(sql)
    r = cursor.fetchone()
    if r != None:
        c.send(b"EXISTS")
        return

    # 插入用户
    sql = "insert into user (name, pwd) value ('%s','%s')" % (name, passwd)
    try:
        cursor.execute(sql)
        db.commit()
        c.send(b"OK")
    except:
        db.rollback()
        c.send(b"FAIL")
    return


def do_login(c, db, data):
    l = data.split(" ")
    name = l[1]
    passwd = l[2]
    sql = "select * from  user where name = '%s' and pwd = '%s'" % (name, passwd)
    # 查找用户
    cursor = db.cursor()
    cursor.execute(sql)
    r = cursor.fetchone()
    if r == None:
        c.send(b'FAIL')
    else:
        c.send(b"OK")
    return


def do_query(c, db, data):
    l = data.split(" ")
    name = l[1]
    word = l[2]
    # 插入历史记录
    cursor = db.cursor()
    tm = time.ctime()
    sql = "insert into hist (name, word, time) value ('%s','%s','%s')" % (name, word, tm)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    f = open(DICT_TEXT)
    for line in f:
        tmp = line.split(" ")[0]  # 获取单词
        if tmp > word:
            break
        elif tmp == word:
            c.send(line.encode())
            f.close()
            return
    c.send("没有该单词".encode())
    f.close()


def do_history(c, db, data):
    name = data.split(" ")[1]
    cursor = db.cursor()
    sql = "select * from hist where name='%s' order by id desc limit 10" % name
    cursor.execute(sql)
    r = cursor.fetchall()
    if not r:
        c.send(b"FAIL")
    else:
        c.send(b"OK")
        time.sleep(0.1)
    for i in r:
        msg = "%s %s %s" % (i[1], i[2], i[3])
        c.send(msg.encode())
        time.sleep(0.1)
    c.send(b"##")


if __name__ == '__main__':
    main()
