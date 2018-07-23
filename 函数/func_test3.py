# Author:Lithlu
def test1():
    print("in the test1")
    return  # 无论后面写了什么，都不运行
    print("test end")
def test2():
    print("in the test2")
    return 0
def test3():
        print("in the test3")
        return 1,'hello',['lithlu','python']
x = test1()
x1 = test2()
x2 = test3()
print(x)
print(x1)
print(x2)
# 为什么要有返回值
# 后面的程序要1个执行结果 来继续操作