a = [1, 2, 3]
b = a
c = a.copy()
import copy

d = copy.deepcopy(a)

print(b is a)  # True
print(c is a)  # False
print(d is a)  # False

"""
赋值:
    完全的 数据/内存地址 共享  (两者完全一致的值和内存地址)
        值如果是 可变类型 双方会同时变动
        值如果是 不可变类型 双方不会同时变动
浅拷贝
    不完全的数据共享    
        原理: 拷贝数据重新开辟新的内存空间来存储, 只拷贝第一层
        不可变类型无法使用 copy 方法
        可变类型内嵌套可变时, 只拷贝最外层数据
深拷贝
    完全的数据共享
        原理: 同浅拷贝开辟新的内存空间, 可拷贝到最深层的数据
        不可变类型同样可以调用 deepcopy 方法
        可变类型内嵌套可变时, 拷贝到最深层数据
"""

"""
赋值
"""
# 不可变类型
print("=" * 10)
a = "112"
b = a
print(b)  # 112
a = "456"
print(b)  # 112
# 可变类型
a = [1, 2, 3]
b = a
print(b)  # [1, 2, 3]
a.append(1)
print(b)  # [1, 2, 3, 1]

"""
浅拷贝
"""
print("=" * 10)
# 对于不可变的类型是无法使用浅拷贝的
# a = 123   # a = "123"
# b = a.copy()
# print(b)    # 'int'/'str' object has no attribute 'copy'
a = [1, 2, 3, 4, ["a", "b"]]
b = a.copy()
a[0] = "a"
print(b)  # [1, 2, 3, 4, ['a', 'b']]
a[4][1] = 123
print(b)  # [1, 2, 3, 4, ['a', 123]]

"""
深拷贝
"""
print("=" * 10)
import copy

a = str(123)
b = copy.deepcopy(a)
a = [1, 2, 3]
print(a)
print(b)  # 123

a = [1, 2, 3, 4, ["a", "b"]]
b = copy.deepcopy(a)
a[4][1] = 123
print(a)  # [1, 2, 3, 4, ['a', 123]]
print(b)  # [1, 2, 3, 4, ['a', 'b']]
