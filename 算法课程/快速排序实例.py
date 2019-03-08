# 快速排序
import random


def quick(l):
    # 递归退出条件
    # 仅剩一个元素无需继续分组
    if len(l) < 2:
        return l
        # 设置关键数据
    a = l[0]
    # 找出所有比 a 大的数据
    big = [x for x in l if x > a]
    # 找出所有比 a 小的数据
    small = [x for x in l if x < a]
    # 找出所有与 a 相等的数据
    same = [x for x in l if x == a]
    # 拼接数据排序的结果
    return quick(small) + same + quick(big)


if __name__ == '__main__':
    l = list(range(1, 25))
    random.shuffle(l)
    l = quick(l)
    print(l)

