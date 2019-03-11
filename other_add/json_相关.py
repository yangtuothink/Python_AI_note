import json

"""
json.dumps(dict) 
    功能:   将 python字典 转换成 json字符串
    参数:  字典
    返回值:  json 字符串
    
json.loads()
    功能:   将 json字符串 转换成 python字典
    参数:  json 字符串
    返回值:  字典
"""

a = {"a": 1}
print(json.dumps(a))        # {"a": 1}
print(type(json.dumps(a)))  # <class 'str'>

b = json.dumps(a)
print(json.loads(b))        # {'a': 1}
print(type(json.loads(b)))  # <class 'dict'>

