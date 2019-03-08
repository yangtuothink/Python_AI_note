

"""
网络电子词典

用户可以登录和注册
    用户名 密码
    注册必须要写 用户名和密码 .其他自定
    用户名不能重复
    用户信息可以长期保存
通过基本的图形界面 print 提示客户端输入
    程序分为服务端客户端
    服务端负责数据处理
    启动服务端后应满足多个客户端同时操作
启动后进入一级界面
    登录  注册  退出
    登陆成功进入二级界面
    注册成功返回一级界面,或者直接使用注册用户进入二级界面
    退出后退出软件
二级界面
    查单词   历史记录   注销
    查单词 循环输入单词.得到单词解释,输入特殊符号退出查询状态
    历史记录  查询当前用户的查词记录 要求记录包含 name  word time
              可以查看所有记录,或者只显示前10条
单词库
    特点
        每个单词占一行
        单词按照从小到大顺序排列
        单词和解释之间一定有空格
    查词
        直接使用单词本查询.(文本操作)
        现将单词本存入数据库查询.通过数据库查询


确定并发方案,套接字,
    协程 ,tcp_socket

建立数据库,表结构

结构设计
    函数封装
    客户端启动--> 进入一级菜单---> 登录---> 二级界面--->具体请求--->展示内容
    服务端接受请求--->处理请求--->数据发送客户端
    功能模块: 登录,注册,查询单词.历史记录,

分析具体通能,逐个模块实现
"""



"""
表结构设计

table  user 
-----------------------
 id | username |  pwd | 
-----------------------


table user_hist
--------------------------
 id | user_id |  hist_id | 
--------------------------


table  user_history
-----------------------------
id | use_id | dict_id | time  
-----------------------------


table dict_hist
---------------------------
 id | dict_id |  hist_id | 
---------------------------


table  e_dict.txt 
-----------------
id | word | val 
-----------------

"""























