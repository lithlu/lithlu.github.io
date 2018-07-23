# Author:Lithlu
name = "My name is \tlithlu"
print(name.capitalize())  #首字母大写
print(name.count('a')) #查询有多少个a
print(name.center(50,"-"))  #打印50个字符，
                           # 不够的用-填充
print(name.encode()) # 将字符串转换成二进制
print(name.endswith("ex")) # 以 ex 结尾
print(name.expandtabs(tabsize = 30)) # 将\t转换为30个空格
print(name.find("y")) # 取该字母所在的位置
print(name[name.find("name"):]) # 字符串也可以切片 跟列表一样
name1 = "My name is {name},and age is {age}"
print(name1.format(name = "lithlu",age =21 )) #format 可以格式化
print(name1.format_map({'name':'alex','age':21}))
print('abc234'.isalnum()) # 判断是否包含数字 但是不能有特殊字符
print("Name".isalpha())  # 判断是否全部为字母 无论大小写
print("1AF".isdecimal()) #判断是否是二进制
print("1A".isidentifier()) #判断是否是一个合法的标识符
print("name Is ".islower()) #判断是否全部为小写
print('  '.isspace()) # 判断是否是空格
print("My Name Is".istitle()) #判断是否是标题
print("My Name Is".isupper()) #判断是否全部为大写
# print("My Name Is".join("--"))
print(' '
      '+ '.join(['1','2','3'])
)
print('+'.join(['1','2','3','5']))
print(name.ljust(50,'*')) # 字符串长50，不够的用*在末尾补充
print(name.rjust(50,'*'))
print("\nLithlu")
print("\nLithlu\n".strip()) # 去左边lstrip 去右边rstrip
print("****************")
p = str.maketrans("ajliu",'12345')
print('lithlu'.translate(p))
print("lithlu".replace('l','L',1))
print('lithlu'.rfind('i')) # 从左边开始查找，等于1
print('li th lu'.split()) # 把字符串按照空格分成一个列表
print("1+2+3+4+5+6".split('+')) # .splitlines()按照换行来分割
print("Lithlu".swapcase()) # 大写转换为小写，小写转换为大写
print("Lithlu".title())
print("lithlu".zfill(20)) # 不够的自动用0填充
