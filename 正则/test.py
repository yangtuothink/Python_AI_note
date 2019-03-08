import re

# s = """
# zhang email: zhang@qq.com
# li email: li@163.com
# wang email: wang@sina.com.cn
# """
# pattern = "(\w+@\w+(\.com)?(\.cn)?)"
# a = re.findall(pattern, s)
# print(a)

# 首字母大写的单词
# s = "I sdjaaAcsjl Zabcaaas ZN  ZN090 Z_SDAS"
# pattern = "[A-Z]+[-_0-9A-Za-z]*"
# print(re.findall(pattern, s))
# ['I', 'Acsjl', 'Zabcaaas', 'ZN', 'ZN090', 'Z_SDAS']

# s = "I sdjaaAcsjl 1.75 ZN  ZN 090 Z_SD 456.  175.69km 68.2kg.454 AS"
# # pattern = "\d+\.?\d*"     # 找出所有数字
# pattern = "[1-9]+\d\d"      # 找出三位数
# print(re.findall(pattern, s))

# 6-8 位字符串内部为 数字 字母 下划线
# s = "sda_Sss sda78_Ss "
# pattern = "[_0-9a-zA-Z]{6,8}"
# print(re.findall(pattern, s))

# s = "13160035872 13160035872sd"
# pattern = "1\d{10}"
# print(re.findall(pattern, s))

# r""
# s = "\\hello"
# print(re.findall("\\\\\\w+", s))
# print(re.findall(r'\\\w+', s))

"""
python 字符串      --> 正则      --> 目标字符串
"\\$\\d+"           \$\d+           "$100"
r"\$\d+"            \$\d+           "$100"
* 为避免特殊字符串在字符串中使用时转义的麻烦, 使用 raw 字符串来表达正则表达式
"""

# 非贪婪匹配的运用
# s = "ashb, asjdlab, asdadb"
# print(re.findall(r"a.*b", s))   # ['ashb, asjdlab,asdadb']
# print(re.findall(r"a.*?b", s))  # ['ashb', 'asjdlab', 'asdadb']


# s = "https://abc.com http://abc.cn"
# print(re.search(r"(http|https|ftp|file)://\S+", s).group(1))


s = "371302199506011810"
res = re.search(r"\d{17}(\d|x)", s).group()
print(res)
