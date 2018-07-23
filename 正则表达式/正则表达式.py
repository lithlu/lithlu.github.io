# Author:Lithlu
# 只要有返回就是匹配到了，没返回就是没匹配到
import re
re.match("^Chen","Chenjunzhe")
# 结果为 <_sre.SRE_Match object; span=(0, 4), match='Chen'>
res = re.match("^Chen","Chenjunzhe")
print(res)
print(res.group()) # ----->Chen

res = re.match("^Chen\d+","Chen123junzhe54")
print(res.group()) # "\d"代表一个数字，若要代表多个数字则用"\d+"

