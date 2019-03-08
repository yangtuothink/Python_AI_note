"""
扑克牌只取红桃花色 13 张, 用数字表示 1-13 表示
洗牌后, 牌面反面向上排成一排, 找出 红桃 8
要求: 若未找到输出 "查找失败"
若找到: 输出 "查找成功, 是第 x 牌"

"""

"""
原始数据: data
被查询数字: key
"""
import random


def linear(data, key):
    random.shuffle(data)
    for i in range(len(data)):
        # 对比当前数据与 待查找数据
        if data[i] == key:
            # 查找成功, 返回下标值
            return i + 1
    else:
        # 遍历完, 仍未找到数据
        return -1


if __name__ == '__main__':
    # 原始数据
    value = list(range(1, 14))
    # 带查找数据
    key = 8
    # 获取返回结果并输出
    res = linear(value, key)
    if res == -1:
        print("打印失败")
    else:
        print("查找成功. 是第 %d 张" % res)
