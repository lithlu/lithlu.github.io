# Author:Lithlu

def test(x,y):
    print(x)
    print(y)
test(1,2) # 位置参数跟形参一一对应
#关键字参数 test(x 1 , y = 2) 与位置无关
# 既有位置参数又有关键字调用 会执行位置参数
#关键字参数，不能写在位置参数前面
#默认参数特点,调用函数的时候，默认参数非必须传递

#针对形参不固定的情况下可以用到参数组
#参数组一定要往后放
#1. *代表功能，形参接受的变量是不固定的
# *args接受N个“位置”参数，转换成元祖的形式
def test1(*args):
    print(args)
test1(1,2,5,3,58,57,96,33)
#2.
'''def test2(*args2):
    print(args2)
test2(*[1,2,3,4,5,6]) # *args =tuple([1,2,3,4,5,6])

#参数组和位置参数的合用
def test3(x,*args3):
    print(x)
    print(*args3)
test3(1,2,44,5,9,2,1,5,6,2)

# 形式参数是字典的形式
#**kvargs:把N个"关键字"参数，转换成字典的形式
def test4(**kvargs):
    print(kvargs)
    print(kvargs['china'])
    print(kvargs['American'])

test4(china=["北京","上海","天津","深圳"],American=["洛杉矶","加利福尼亚"])
# test4(**{'name':'lithlu','age':21})
'''
def logger(source):
    print("from %s"%source)
def test5(name,age=21,*args,**kvargs):
    print(name)
    print(age)
    print(args)
    print(kvargs)
    logger("test5")
test5("lithlu",sex ="F",hobaby = "learn")
