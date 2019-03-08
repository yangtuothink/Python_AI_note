"""
 一次性的执行脚本文件

目的
    实现将文件中的 数据插入在数据库中

"""
import pymysql

f = open("e_dict.txt")
db = pymysql.connect("127.0.0.1", "root", "123456", "dict")
cursor = db.cursor()
for line in f:  # 循环读取文件内容
    tmp = line.split(" ")
    word = tmp[0]
    mean = " ".join(tmp[1:]).strip()

    sql = 'insert into words (word, mean) values ("%s","%s")' % (word, mean)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
f.close()
