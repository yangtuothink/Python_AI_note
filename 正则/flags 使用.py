import  re

# 只匹配ascii字符
# regex = re.compile(r'\w+',flags=re.A)

# 忽略字母大小写
# regex = re.compile(r'[A-Z]+',flags=re.I)

# . 可以匹配换行
# regex = re.compile(r'.+',flags=re.S)

# 匹配每一行开始位置
# regex = re.compile(r'^北京',flags=re.M)

# 为正则添加注释
pattern = r'''[A-Z][a-z]* #匹配第一个单词
\s+\w+\s+ #匹配空行和第二个单词
\w+ #匹配汉字
'''
regex = re.compile(pattern,flags=re.X)

s = '''Welcome to
北京
'''
l = regex.findall(s)
print(l)
