import greenlet


def func1():
    print("func1 start")
    f2.switch()
    print("func1 end")
    f2.switch()


def func2():
    print("func2 start")
    f1.switch()
    print("func2 end")
    f1.switch()


f1 = greenlet.greenlet(func1)
f2 = greenlet.greenlet(func2)

f1.switch()

"""
func1 start
func2 start
func1 end
func2 end
"""

"""
	gr1 = greenlet(func1)
	gr1.swich()
"""
