# _*_ coding:utf-8 _*_
__author__ = "yangtuo"
__date__ = "2019/4/28 16:43"

import re

# s = "A B C D"
# # p1 = re.compile("\w+\s+\w+")
# # print(p1.findall(s)) # ['A B', 'C D']
#
# p1 = re.compile("(\w+)\s+\w+")
# print(p1.findall(s))
# # 第一步 ['A B','C D']
# # 第二步 ['A','C']
#
# p1 = re.compile("(\w+)\s+(\w+)")
# print(p1.findall(s))
# # 第一步 ['A B','C D']
# # 第二步 [('A','B'),('C','D')]


s = "sda123.65ascs681.58sda156871sdad"
p1 = re.compile("(\d+)\.+(\d+)")
print(p1.findall(s))


s = "!?.18)dajdlj$12.365sdd.sdasd3514.168nsda$15.6sdwal.sdadw123.156s"
p1 = re.compile("(\w+)\.(\w+)((\d+)\.+\d+)")
print(p1.findall(s))

s = "!?.18)dajdlj$12.365sdd13514.168nsda$15.6sdwals"
p1 = re.compile("(\w+)\$+(\d+\.+(\d+))")
print(p1.findall(s))