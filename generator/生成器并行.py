# Author:Lithlu
import time
# 生产包子和吃包子
def consumer(name): # 消费者
    print("%s 准备吃包子啦！"%name)
    while True:
        baozi = yield # yield没有返回值就是返回空
        # next 只是调用（唤醒）yield不会传值
        # send 不只是调用（唤醒），还会传值
        print("包子[%s]来了，被[%s]吃了！"%(baozi,name))
#c.consumer("lithlu")# 只是把它变成生成器，next一下才会继续往下
#c.__next__()
def producer(name): # 生产者
    # 准备消费者
    c = consumer("A")
    c1 = consumer("B")
    # 初始化
    c.__next__()
    c1.__next__()
    print("我要开始做包子了")
    # 生产者循环十次，每次生产一个包子
    for i in range(10):
        time.sleep(1)
        print("做了一个包子")
        c.send(i)
        c1.send(i)
producer("lithlu")
