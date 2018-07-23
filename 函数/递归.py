# Author:Lithlu
#自己调用自己
#1.必须有一个明确的结束条件
#2.每次进入更深一层递归时，问题规模相比上次递归都应该有所减少
#3.递归效率不高，递归层次过多会导致栈溢出

'''def calc(n):
    print(n)
    return  calc(n+1)
calc(0)
# 最多调用自己999次
'''
def calc(n):
    print(n)
    if int( n / 2 )> 0 :
        return calc(int(n/2))
    print("--->",n)
calc(10)