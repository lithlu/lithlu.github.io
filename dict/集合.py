# Author:Lithlu
#集合是无序的，不重复的数据集合，它的主要作用：
#去重，把一个列表变成集合，就自动去重了
#关系测试，测试两组数据之前的交集，差集，并集等关系

list01 = [1,4,5,8,2,7,5]
list01 = set(list01) # 把列表变成集合
list02 = set([2,5,7,5,3,1,8,2,38,6,4])
print(list01,list02)
# 取交集 print(list01.intersection(list02))
print(list01 & list02)
# 并集  print(list01.union(list02))
print(list02 | list01)
# 差集
print(list01.difference(list02))
print(list02.difference(list01))
print(list01 - list02) # in list01 but not in list02
# 取子集 subset
print(list01.issubset(list02))
# 父集 superset
print(list01.issuperset(list02))
# 对称差集(把他们两里面互相没有的都取出来)
print(list01.symmetric_difference(list02))
print(list01 ^ list02)
print("-----------------------")
# 两个列表如果有交集则返回False
print(list02.isdisjoint(list01))
print("-----------------------")
# 增
list01.add("9999") # 添加一项
print(list01)
list01.update("120","41","5","65") # 添加多项
print(list01)
# 删除
# print(list01.pop())
list01.discard(1)
print(list01)


