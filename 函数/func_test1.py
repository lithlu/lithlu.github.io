# Author:Lithlu
#面向对象 --->类 ----->class
#面向过程 --->过程---->def (没有返回值）但是在Python中，过程被当成函数

#函数式编程-->函数---->def

#函数
def func1():
    '''testing 定义函数'''
    print("in the func1")
    return 0
#过程
def func2():
    '''testing 定义过程'''
    print("in the func2")
x = func1()
y = func2()
print(x)
print(y)