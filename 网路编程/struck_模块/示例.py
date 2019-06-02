# _*_ coding:utf-8 _*_
__author__ = "yangtuo"
__date__ = "2019/3/25 20:44"

import struct

st = struct('i16sf')
data = ["123", "abc", 123]

data = st.pack(data)
print(data)
st.unpack(data)

