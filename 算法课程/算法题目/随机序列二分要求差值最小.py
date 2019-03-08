"""
算法题：
    提供一个序列，完成对这个序列的分割。要求分割后的两个序列彼此差值最小
    实现函数，返回两个序列
"""


def func(i):
    i.sort()
    if not i:
        return (([], []))

    max_num = i[-1]
    max_two_num = i[-2]
    max_list, min_list = func(i[:-2])
    max_list.append(max_two_num)
    min_list.append(max_num)

    if sum(max_list) > sum(min_list):
        return ((max_list, min_list))
    else:
        return ((min_list, max_list))


l = [1, 46, 3, 8, 6, 4561, 4642, 45, 8, 9, 155, 1784]
print(len(l))
l1, l2 = func(l)
print(l1, l2)
