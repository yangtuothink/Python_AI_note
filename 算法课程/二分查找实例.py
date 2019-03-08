"""
1. 切分成两部分,取中间值来判断
2. 如何定义下一次的范围:
    大于中间值, 在左侧找
    小于中间值, 在右侧找
3. 查找失败情况: 中间值 小于左端 或者 中间值 大于 右端
"""

"""
扑克牌 只取 黑桃 13 张, 用 1-13 表示, 将牌从小到大排序, 反面向上排成一排, 找到黑桃 6 的位置
"""

"""
l   原始数据
k     待查找数据
left    首元素下标值
right   尾元素下标值
"""

"""
递归方式实现
"""


def func(l, k, left, right):
    # 递归退出条件
    if left > right:
        # 查找结束
        return -1
    # 获取中间元素对应下标值
    middle = (left + right) // 2
    # 对比中间元素 和 查找元素
    if l[middle] == k:
        return middle
    elif l[middle] > k:
        # 中间值 大于 查找值
        # 查找范围是 中分后的 左边部分
        # 左侧下标值不变, 右侧下标值变为 middle 前一位
        right = middle - 1
        return func(l, k, left, right)
    else:
        # 中间值 小于 查找值
        # 查找范围是 中分后的 右边部分
        # 左侧下标值变为 middle 后一位, 右侧下标值不变
        left = middle + 1
        return func(l, k, left, right)


"""
循环方式实现
"""



def foo(l, k):
    left = 0
    right = len(l) - 1
    while left <= right:
        mid = (left + right) // 2
        if l[mid] > k:
            right = mid - 1
        elif l[mid] < k:
            left = mid + 1
        elif l[mid] == k:
            return mid
        else:
            return -1


if __name__ == '__main__':
    # l = list(range(1, 14))
    # k = 8
    # right = len(l) - 1
    # res = func(l, k, 0, right)

    l = list(range(1, 14))
    k = 10
    right = len(l) - 1
    res = foo(l, k)
    if res == -1:
        print("查找失败")
    else:
        print("查找成功, 第 %d 张拿到" % res)
