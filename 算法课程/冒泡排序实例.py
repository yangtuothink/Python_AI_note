"""
入学后, 第一次上体育课, 体育老师要求大家排队, 按照身高从低到高排队
获取全班 10 名同学的身高
"""

"""
外层循环
    大循环控制总循环次数                    
内层循环
    小循环控制如歌得出这个最大值
        计算大小, 然后彼此交换

"""

import random

"""
基础版
"""



sorted()

def func(l):
    # 外层循环: 走访数据的次数
    for i in range(len(l) - 1):
        # 内层循环: 每次走访数据时, 相邻对比次数
        for j in range(len(l) - i - 1):
            # 要求从低到高
            # 如次序有误就交换
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]

    # 遍历次数
    print("走访次数:", i + 1)


"""
升级版
"""


def foo(l):
    # 外层循环: 走访数据的次数
    for i in range(len(l) - 1):
        # 设置是否交换标志位
        flag = False
        # 内层循环: 每次走访数据时, 相邻对比次数
        for j in range(len(l) - i - 1):
            # 要求从低到高
            # 如次序有误就交换
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                # 发生了数据交换
                flag = True
        # 如果未发生交换数据, 则说明后续数据均有序
        if flag == False:
            break  # 跳出数据走访
    # 遍历次数
    print("走访次数:", i + 1)


if __name__ == '__main__':
    l = list(range(1, 11))
    random.shuffle(l)
    print("排序前:", l)
    # func(l)
    foo(l)
    print("排序后:", l)
