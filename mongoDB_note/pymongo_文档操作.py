from pymongo import MongoClient

# 创建数据库链接
conn = MongoClient("localhost",27017)

# 创建数据库对象
db = conn.stu
# db = conn["stu"]

# 生成集合对象
myset = db.class0
# myset = db["class0"]

# 创建集合对象
myset = db.class4

# 数据操作


# -----------------------insert----------------------
# myset.insert_one({"name":"张铁林","King":"乾隆"})

# myset.insert_many([{"name":"张国立","King":"康熙"},\
    #  {"name":"陈道明","King":"康熙"}])

# myset.insert({"name":"唐国强","King":"雍正"})
# myset.insert([{"name":"陈建斌","King":"雍正"},\
    # {"_id":1, "name":"吴奇隆","King":"四爷"}])

# myset.save({"_id":1,"name":"聂远","King":"乾隆"})


#  ----------------------find-----------------------
# cursor = myset.find({"name":{"$exists":True}},{"_id":0})
# print(cursor.next()) # 打印下一个文档
# for i in cursor:
    # print(i)
    # print(i["name"],"--",i["King"])
# 所有的操作符加上引号,作为字符串形式
# true/false/null 改成 True/False/None


# for i in cursor.limit(3):
# for i in cursor.skip(3):
# for i in cursor.sort([("name",1),("age",-1)]):
# for i in cursor.sort([("name",1)]):
    # print(i)
# limit,sort,skip 使用时, 必须保证游标在最开始的位置

# dic = {"$or":[{"King":"乾隆"},{"name":"陈道明"}]}
# d = myset.find_one(dic,{"_id":0})
# print(d)


#  ----------------------update-----------------------
# myset.update_many({"King":"康熙"},{"$set":{"king_name":"玄烨"}})
# myset.update_one({"King":"雍正"},{"$set":{"king_name":"忘了名字"}})
# myset.update_one({"name":"郑少秋"},{"$set":{"King":"乾隆"}},upsert=True)
# myset.update({"King":"乾隆"},{"$set":{"king_name":"弘历"}})
# myset.update({"King":"乾隆"},{"$set":{"king_name":"弘历"}},multi=True)


# ------------------------delete----------------------
# myset.delete_one({"King":"康熙"})
# myset.delete_many({"King":"雍正"})
# myset.remove({"king_name":{"$exists":False}})
# myset.remove({"king_name":None},multi=True)


# ------------------------复合操作----------------------
# data = myset.find_one_and_delete({"name":"张铁林"})
# print(data)


# 关闭链接
conn.close()
