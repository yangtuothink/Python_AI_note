import sys

print(sys.argv)

"""
获取命令行参数 

输入 python3 sys.argv_demo.py 
输出: ['argv.py']

输入 python3 sys.argv_demo.py hello world
输出: ['argv.py','hello','world']

输入 python3 sys.argv_demo.py 'hello world'
输出: ['argv.py','hello world']

会收集命令行参数保存在列表中以字符串的形式 
如果有空格,则会被分成两个.可以用引号来注明一个整体
"""



