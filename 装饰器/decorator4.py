# Author:Lithlu
import time
def timer(func): # time(test1) func = test1
    def deco(*args,**kvargs): # 装饰器的参数不固定的时候则用*args 和**kvargs  非固定参数
        start_time = time.time()
        func(*args,**kvargs)# run test1()
        stop_time = time.time()
        print("the func run time is %s"%(stop_time-start_time))
    return deco
@timer # test1 = timer(test1) 这一步就是运行操作
def test1():
    time.sleep(1)
    print("in the test1")
@timer
def test2(name,age):
    time.sleep(1)
    print("test2:",name,age)
test1()
test2("lithlu",21)