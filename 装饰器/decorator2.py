# Author:Lithlu
'''def bar():
    print("in the bar")
def foo():
    print("in the foo")
    bar()
foo()
'''

'''def foo():
    print("in the foo")
    bar()
def bar():
    print("in the bar")
foo()
'''
'''import time
def bar():
    time.sleep(3)
    print("in the bar")
def test1(func):
    star_time = time.time()
    func() # == run bar
    stop_time = time.time()
    print("the func run time is %s"%(stop_time-star_time))
test1(bar)
# --->
# func = bar
# func()'''
import time
def bar():
    time.sleep(3)
    print("in the bar")
def test2(func):
    print(func)
    return (func)
#print(test2(bar))
'''t = test2(bar)
t() # 表示运行bar()
'''
bar = test2(bar)
bar() # run bar