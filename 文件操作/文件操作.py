# Author:Lithlu
# 打开文件 ---> 操作---->关闭
# 不规范 data = open("readme",encoding = "UTF-8").read()
# r 是只能读   w 是创建一个文件 覆盖掉原文件
# a 表示追加，在文件最后添加 不覆盖原文件，不能读
# r+ 表示读写 在原有文件的基础之上进行 在最后追加
# w+ 表示写读 新建文件执行写读
# b是改变处理文件的方法
# f = open("readme",'r+',encoding = "utf-8") # 文件句柄
#f.write(" ")
# f.readline()表示一行一行的读
# print(f.readline())
'''for index,line in enumerate(f.readlines()):
    if index == 3:
        print("------------")
        continue
    print(line.strip())
f.close()

# 读一行删一行，可以用于大文件
# 建议用这种方式
count = 0
for line in f:
    if count == 2:
        print("-----我是分割线------")
        count += 1
        continue
    print(line)
    count += 1 
'''
'''
#将文件句柄的指针打印出来 f.tell()按字符计数
print(f.tell())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.tell())
f.seek(0) # 光标回到指定位置
print(f.readline())
print(f.encoding)
print(f.fileno()) # 输出文件编号
print(f.flush()) # 刷新
'''
'''f.seek(10) # 移光标
f.truncate(20) # 截断
'''
f = open("readme1",'wb') # 文件句柄 二进制文件
# 网络传输只能用二进制
f.write("hello binary\n".encode())

f.close()