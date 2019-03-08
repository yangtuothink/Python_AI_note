import gevent
from gevent import monkey;monkey.patch_all()
import time


def func1():
    print("func1 start")
    time.sleep(2)
    print("func1 end")


def func2():
    print("func2 start")
    time.sleep(2)
    print("func2 end")


f1 = gevent.spawn(func1)
f2 = gevent.spawn(func2)

gevent.joinall([f1, f2])

"""
func1 start
func2 start
func1 end
func2 end
"""

"""
	gevent.spawn(func.argv)
		功能:生成协程对象
		参数：
			func:　协程函数
			argv:　协程函数的参数（不定参）
	
	gevent.joinall(list.[timeout])
	    功能：让程序拥有阻塞等待协程执行完毕的能力
	    参数：
	        list 协程对象列表
	        timeout　超时时间
	
	gevent.sleep(2)
	    功能:睡眠阻塞　
	    参数:睡眠时间
	
	from gevent import monkey;monkey.patch_all()
	    功能:实现让 gevent 能够识别到其他的阻塞 
	    注意点: 猴子必须要写在对应模块导入前执行
"""
