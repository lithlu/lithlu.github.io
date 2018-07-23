# Author:Lithlu
# 若要在def里面修改全局变量 则要用关键字 global
# 不提倡

'''
school = '0012'
def change_name():
    name = 'alex' #作用域 只能在函数内部调用

    global school #不提倡
    school = "0013"
    print(name+":"+school)
print(school)
change_name()
print(school)
'''
 # 若函数外部没有全局变量，而函数内部使用了global关键字，
 # 则函数内部的global声明的那个变量则是全局变量

 # 不提倡
'''def change_name():
     global name
     name = "alex"
     print(name)
change_name()
'''
school = "01112"
names = ["Alex","jack","Rain"]
# 字符串和整数是不能改
# 列表，字典，集合都是可以在局部里面改全局的
def change_name():
    names[0] ="金角大王"
    print("insides func",names)
change_name()
print(names)