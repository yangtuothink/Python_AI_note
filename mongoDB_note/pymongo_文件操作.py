from pymongo import MongoClient
import bson.binary

conn = MongoClient("localhost",27017)
db = conn.image
myset = db.mm

# --------------------存储----------------------------------
# 读取图片内容
# with open("123.PNG","rb") as f:
    # data = f.read()

# 格式转化
# conntent = bson.binary.Binary(data)

# 插入数据库
# myset.insert_one({"filename":"123.jpg","data":conntent})


#--------------------取出文件-------------------------------
# img = myset.find_one({"filename":"123.jpg"})

# 写入本地
# with open("123.jpg","wb") as f:  # find_one　会自动转换不需要自己再转换了
    # f.write(img["data"])


conn.close()
