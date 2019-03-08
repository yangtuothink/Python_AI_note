"""
算法题：
    提供一个序列，完成对这个序列的分割。要求分割后的两个序列彼此差值最小
    实现函数，返回两个序列
"""


def func(i):
    if not i:
        return ([], [])
    elif len(i) == 2:
        return (i[1:], i[0:])
    elif len(i) == 1:
        return (i[0:], [])
    else:
        max_num = i[-1]

        max_two_num = i[-2]

        max_list, min_list = func(i[:-2])
        max_list.append(max_two_num)
        min_list.append(max_num)

        if sum(max_list) > sum(min_list):
            return (max_list, min_list)
        return (min_list, max_list)


# tests = [
#     [1, 2, 3, 5, 6, 7, 8],
#     [15446, 13, 165468, 113216, 1654613, 11, 132, 135416, 54],
#     range(1, 10)]

# for i in tests:
#     i.sort()
#     list_max, list_min = func(i)

l = [1, 46, 3, 8, 6, 4654, 45, 456546, 1313, 1321, 8, 9, 155]
l.sort()
print(len(l))
l1, l2 = func(l)
print(l1, l2)
print(sum(l1), sum(l2))
