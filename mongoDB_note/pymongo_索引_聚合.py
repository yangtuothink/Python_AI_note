from pymongo import MongoClient

conn = MongoClient("localhost", 27017)
db = conn.stu
myset = db.class0

# -------------------------------索引--------------------------------
# 创建
# index_name = myset.create_index("name")
# index_age = myset.create_index("age",name="Age",sparse=True)
# index_age = myset.create_index("age",name="Age",sparse=True,unique=True)


# 　删除索引
# myset.drop_index("Age")
# myset.drop_indexes()


# 查看
# for i in myset.list_indexes():
# print(i)

# ------------------------------聚合----------------------------------
lis = [
    {"$group": {"_id": "$sex", "num": {"$sum": 1}}},
]

cursor = myset.aggregate(lis)
for i in cursor:
    print(i)

conn.close()