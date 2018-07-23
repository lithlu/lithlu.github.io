# Author:Lithlu
# [ i * 2 for i in range(10)]# 列表生成式
# 生成器只有在调用时才会生成相应的数据
# 只记录当前的位置


'''x = int(input("输入一个数字:"))
b = (i * 2 for i in range(x)) # 生成器
for i in b:
    print(i,end=" ")

# 取数据用 b.__next__()
'''
# 用函数来实现generator
# a,b = b, a + b ----> t = ( b , a + b),a = t[0],b = t[1]

