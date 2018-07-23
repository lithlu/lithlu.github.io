# Author:Lithlu
# f = open("readme","r",encoding = "utf-8")
with open("readme","r",encoding = "utf-8") as f:
    for line in f:
        print(line)
# 自动关闭文件