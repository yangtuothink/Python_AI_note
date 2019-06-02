# _*_ coding:utf-8 _*_
__author__ = "yangtuo"
__date__ = "2019/4/1 9:26"

_map_data = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

map_labels = []  # 保存显示数字的 label


def fill2():
    """此函数将想 _map_data 中添加一个2到空位置"""
    blank_count = get_space_conunt()  # 得到地图上的空白位置
    if 0 == blank_count:
        print("地图已满, 不添加")
        return
    import random
    pos = random.randrange(0, blank_count)  # 生成随机位置
    offset = 0  # 记录当前走到的位置
    for line in _map_data:  # line 绑定一行的列表
        for c in range(4):  # c 为行的索引
            if 0 == line[c]:
                if offset == pos:
                    line[c] = 2  # 在此位置添加 2
                    return
                offset += 1


def get_space_conunt():
    """此方法返回地图中的 0 的个数"""
    count = 0
    for line in _map_data:
        count += line.count(0)
    return count


def main():
    import tkinter
    root = tkinter.Tk()

    # 键盘按下处理函数
    def on_key_down(event):
        if event.keysym in ('Left', 'a'):
            left()
            fill2()
        elif event.keysym in ('Right', 'd'):
            right()
            fill2()
        elif event.keysym in ('Up', 'w'):
            up()
            fill2()
        elif event.keysym in ('Down', 's'):
            down()
            fill2()
        update_ui()  # 更新界面

    root.bind('<KeyPress>', on_key_down)

    # 移动数字
    def _left_move_number(line):
        for _ in range(3):
            for i in range(3):
                if line[i] == 0:  # 右侧过来条虫
                    line[i], line[i + 1] = line[i + 1], 0

    # 合并相邻数字
    def _left_merge_number(line):
        for i in range(3):
            if line[i] == line[i + 1]:
                line[i], line[i + 1] = line[i] + line[i + 1], 0

    def _left_move_aline(line):
        """
            例如:  [2,0,2,8] ==> [4,8,0,0]
        """
        # 第一步 让左侧有0 的数字左移
        _left_move_number(line)  # [2,0,2,8] ==> [2,2,8,0]
        # 第二步 让左侧相邻的数合并
        _left_merge_number(line)
        # 第三部 让左侧数字在左移
        _left_move_number(line)

    def left():
        for line in _map_data:
            _left_move_aline(line)

    def right():
        for line in _map_data:
            line.reverse()
            _left_move_aline(line)
            line.reverse()

    def up():
        for c in range(4):  # c 列索引
            line = [0, 0, 0, 0]  # 初始化一个列表
            for r in range(4):
                line[r] = _map_data[r][c]
            # 移动
            _left_move_aline(line)
            # 重新放回值
            for r in range(4):
                _map_data[r][c] = line[r]

    def down():
        _map_data.reverse()
        up()
        _map_data.reverse()

    # 根据地图数据, 重新设置 UI 中的 Label 中数字, 颜色等信息
    def update_ui():
        for r in range(4):  # r 行索引
            for c in range(4):  # c 列索引
                number = _map_data[r][c]  # 获取数字
                label = map_labels[r][c]  # 获取数字对应的标签
                label['text'] = str(number) if number > 0 else ''

    # 添加两个 2
    fill2()
    fill2()

    # 创建 2048 地图
    for r in range(4):
        row = []  # 创建一个新的列表, 用来绑定一行 label
        for c in range(4):
            number = _map_data[r][c]
            txt = str(number) if number > 0 else ''
            label = tkinter.Label(root, text=txt,
                                  width=4, height=2, bg='#cdc1b4',
                                  font=('黑体', 30, 'bold'))
            label.grid(row=r, column=c, padx=5, pady=5)
            row.append(label)  # 小循环: 每个 label 加入到一行的列表中
        map_labels.append(row)  # 大循环: 加入一行 label
    root.mainloop()


if __name__ == '__main__':
    main()
