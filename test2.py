"""
一句话实现 99 乘法表
"""

# for x in range(1, 10):
#     print()
#     for y in range(x, 10):
#         print("{0}*{1}={2}".format(x, y, x * y),end=" ")


print('\n'.join([' '.join(['%s*%s=%-2s' % (y, x, x * y) for y in range(1, x + 1)]) for x in range(1, 10)]))
