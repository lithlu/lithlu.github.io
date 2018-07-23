# Author:Lithlu
import re
print(re.search("\w+","1245@asd"))
# <_sre.SRE_Match object; span=(0, 4), match='1245'>
# \w 匹配非特殊字符  如匹配到 a-z A-Z 或者是数字
# \W  是只匹配特殊字符
# \s 匹配空白字符 如 \t \n  \r


# 分组匹配

a = re.search("(?P<id>[0-9]+)(?P<name>[a-zA-Z]+)","123456lithlu").groupdict()
print(a)
b = re.search("(?P<province>[0-9](4))(?P<city>[0-9](2))(?P<birthday>[0-9](4))","371481199306143242").groupdict()
print(b)


# 分割 split
re.split("[0-9]","abc12de3fgh")
# ['abc', '', 'de', 'fgh']

# 替换 sub
re.sub("[0-9]+","|","abc12dfegh3sfjd")
# "[0-9]+" 匹配的值  "|"要用什么来替换
#  'abc|dfegh|sfjd'
re.sub("[0-9]+","|","abc12dfegh3sfjd",count = 2)
# count指匹配多少次
# 'abc|dfegh|sfjd'


# 反斜杠转义
re.search(r"\\","abcd\\125")
# abcd后面的反斜杠 \必须得转义，所以得两个 \\
# 匹配的反斜杠也是得转义
# 所以结果是只匹配到了一个反斜杠
# <_sre.SRE_Match object; span=(4, 5), match='\\'>


# flags = re.I 忽略大小写
re.search("[a-z]+","abcaSS",flags = re.I)
# <_sre.SRE_Match object; span=(0, 6), match='abcaSS'>

# flags = re.M 多行模式，改变^和$的行为
re.search(r"^a","\nabc\neeee",flags = re.M)
# <_sre.SRE_Match object; span=(1, 2), match='a'>

# re.S 匹配任意字符
re.search(r".+","\nabcs\nddd",flags = re.S)
# <_sre.SRE_Match object; span=(0, 9), match='\nabcs\nddd'>
