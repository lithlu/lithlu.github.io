# Author:Lithlu
# 局部作用域和全局作用域的访问顺序
'''x = 0
def grandpa():
    # x = 1
    def dad():
        x = 2
        def son():
            x = 3
            print(x)
        son()
    dad()
grandpa()
'''
import time
# 装饰器 I
def timer(func): #timer(test1) func = test1
    def deco():
        start_time = time.time()
        func() # run test1()
        stop_time = time.time()
        print("the func run time is %s"%(stop_time-start_time ))
    return deco
# 装饰器II
# def timer():
#       def deco():
#           pass
@timer # test1 = timer(test1)
def test1():
    time.sleep(3)
    print("in the test1")
@timer # 装饰器3
def test2():
    time.sleep(3)
    print("in the test2")
test1()
test2()
# print(timer(test1))
#test1 = timer(test1)
#test1() # ----> deco
