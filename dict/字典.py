# Author:Lithlu
#key-value
#字典的特性：1.dict是无序的 2.key必须是唯一的，所以天生去重
info = {
    'stu01':'Tom',
    'stu02':'alex',
    'stu03':'lily',
    'stu04':'lamb'
}
# 查
print(info)
print(info['stu02'])
# 建议用这种模式 有就返回值 没有就None
print(info.get('stu2'))
print(info.get('stu02'))
#判断是否在字典中
print('stu02' in info)
#改
info['stu01'] = '汤姆'
info['stu05'] = 'elizabr'
print(info)
#del
del info['stu01']
info.pop('stu03') #指定删
info.popitem() # 随机删
print(info)
print(info.items()) #

b = {
    'stu01':"小明",
    'stu003':'老万',
    'stu004':'Mike'
}
info.update(b) # 更新 合并操作
print(info)
c = dict.fromkeys([61,45,22],'test') # 初始化新的字典
print(c)
d = dict.fromkeys([1,2,3,5],[0,{'name':'lithlu'},21])
print(d)
d[1][1]['name'] = "Jack"
# 四个key共享一个数据
# 修改一个全都变，类似列表的copy
print(d)
