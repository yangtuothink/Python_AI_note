"""
找到所有大写字母开头的单词

找到其中所有数字,数字包含 整数, 小数, 分数, 百分数, 负数

将所有的日期格式 2019-1-23 变成 2019.1.23
"""
import re

s = """
sdSad sLdasd Csdafsg Ketdfml Sudon
DHAD slkjS_SD SSF_SDsd
1123 1.23 -1.5 -6 45% 1/2 dfa
2019-1-23 2019-8-31 2019-8-29-25 2019-8-2sdsda
2019-145-23 2019-45-23
"""

# 找到所有大写字母开头的单词
# p = r"\b[A-Z][a-z]*\b"
# a = re.findall(p, s)
# print(a)

# 找到其中所有数字,数字包含 整数, 小数, 分数, 百分数, 负数
# p = r"-?\d+/?\.?\d*%?"
# b = re.findall(p, s)
# print(b)

# 将所有的日期格式 2019-1-23 变成 2019.1.23
p = r"\d{4}-[1-2]?\d?-[1-3]?\d?\b"
# c = re.search(r"(\d{4}-[1-2]?\d-[1-3]?\d?){8,10}", s).group()
b = re.findall(r"[-0-9]{8,9}\b", s)
print(b)

# print(c)

d = re.sub(r"-", ".", '2019-1-23')
print(d)
# print(d)
# print(s)
