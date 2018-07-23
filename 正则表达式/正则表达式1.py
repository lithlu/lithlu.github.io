# Author:Lithlu
# “.”表示匹配了一个字符
import re
# >>> re.match("^Chen","Chenjunzhe")
# <_sre.SRE_Match object; span=(0, 4), match='Chen'>
# >>> re.match("^.+\d+","Chen123junzhe122")
# <_sre.SRE_Match object; span=(0, 16), match='Chen123junzhe122'>

# “.+"表示匹配任意字符，后面的\d+没用上
# re.mactch 是从字符串开头往后。

# 若要从中间开始则应该用 re.search()从整个文件搜索
# re.search("j.+e","Chen123junzhe122")
# <_sre.SRE_Match object; span=(7, 13), match='junzhe'>
# re.search("j.+e$","Chen123junzhe122")  $表示必须要e结尾的字符串
# re.search("j[a-z]+e","Chen123junzhe123")
# [a-z]表示只匹配一个字符 "+e"表示匹配到e
# re.search("j[a-zA-Z]+e","Chen123junAzhe123")
# re.search("#.+#","15#hello#")
# <_sre.SRE_Match object; span=(2, 9), match='#hello#'>

# >>> re.search("a?","lithlua")
# <_sre.SRE_Match object; span=(0, 0), match=''>
# >>> re.search("a?","alithlua")
# <_sre.SRE_Match object; span=(0, 1), match='a'>

# “?”表示匹配问号前面的字符一次或零次，不能匹配多次
# 若前面字符满足则后面一个可有可无
re.search("uuu?","uulithluu")
# _sre.SRE_Match object; span=(0, 2), match='uu'

# re.search("uul?","uuithluu")
# <_sre.SRE_Match object; span=(0, 2), match='uu'>
#  re.search("uul?","uulithluu")
# <_sre.SRE_Match object; span=(0, 3), match='uul'>

# >>> re.search("uuu?","uulithluu")
# <_sre.SRE_Match object; span=(5, 7), match='uu'>
# >>> re.search("uu?","uulithluu")
# <_sre.SRE_Match object; span=(0, 2), match='uu'>

# " {m}"匹配多少个数字
# >>> re.search("[0-9]{3}","Chenjun1z23h458e4787")
# <_sre.SRE_Match object; span=(12, 15), match='458'>
# >>> re.search("[0-9]{3}","Chenjun1z23h48e4787")
# <_sre.SRE_Match object; span=(15, 18), match='478'>

# >>> re.findall("[0-9]{1,3}","Chenjun1z23h458e4787")
# ['1', '23', '458', '478', '7']

re.search("(abc){2}(\|\|=){2}","alexabcabc||=||=") # 记得转义和分组
# _sre.SRE_Match object; span=(4, 16), match='abcabc||=||='>
re.search("\A[0-9]+[a-z]\Z","123a")
#<_sre.SRE_Match object; span=(0, 4), match='123a'>

re.search("\D+\D+","1245#$ @@lithlu!") # \D匹配非数字
# <_sre.SRE_Match object; span=(4, 16), match='#$ @@lithlu!'>


