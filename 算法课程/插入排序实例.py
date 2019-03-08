"""


"""
import random


def func(l):
    # 外层循环: 对应遍历所有的无序数据
    for i in range(1, len(l)):
        # 备份 取出数据
        temp = l[i]
        # 记录取出来的下标值
        pos = i
        # 内层循环: 对应从后往前扫描所有有序数据
        """
        i - 1 - >   从最后一个有序数据开始, 即无序数据前一位
        -1 - >   扫描到下标 0 为止, 要包括第一个, 因此设置 -1 往后推一位
        -1 - >   从后往前扫描
        """
        for j in range(i - 1, -1, -1):
            # 若有序数据 大于 取出数据
            if l[j] > temp:
                # 有序数据后移
                l[j + 1] = l[j]
                # 更新数据的插入位置
                pos = j  # 对应所有有序数据比取出数据大的情况
                # 若有序数据 小于/等于  取出数据
            else:
                pos = j + 1
                break
        # 在指定位置插入数据
        l[pos] = temp


if __name__ == '__main__':
    l = list(range(1, 13))
    random.shuffle(l)
    func(l)
    print(l)