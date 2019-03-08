"""
n 个人
开始循环 报数123
报到 3 离开
最后剩下的人是 原来的第几个人

"""
L = list(range(1, 101))
print(L)

"""
[1,2,3,4,5,6,7]
[1,2,0,4,5,0,7]
[1,0,0,4,5,0,0]
[1,0,0,4,0,0,0]
[0,0,0,4,0,0,0]
"""

# def chusan(l):
#     if l.count(0) == 99:
#         ind = 0
#         for i in l:
#             if i == 0:
#                 ind += 1
#             return ind

l = list(range(1, 8))
print(l)
i = 0

while True:
    if l.count(0) == (len(l)-1):
        break
    for x in range(len(l)):
        if l[x] != 0:
            i += 1
        if i % 3 == 0:
            l[x] = 0

print(l)
