# Author:Lithlu
#生成器
x = int(input("请输入一个数字："))
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        # print(b)
        yield b
        a, b = b, a+b #---->t = (b,a + b) a = t[0],b = t[1]
        n = n + 1
    return "done" # 用了下面的for循环， done不会打印
f = fib(x)
print("-----------")
print(f.__next__())
print(f.__next__())
print(f.__next__())
print("======== start for loop:=========")
for i in f:
    print(i)

# 把这个函数改成生成器，只要把while里的print()
# 改为yield i