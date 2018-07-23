# Author:Lithlu
search_engine = {
    #尽量不要写中文，有可能出现编码问题
    '国外':
        {
        'www.google.com':['搜索面较广','可视东西多'],
        'www.bing.com':['简洁','有求必应']
        },
    '国内':
        {
        'www.baidu.com':['莆田系广告多','很难在搜索第一页找到官网'],
        'www.360.com':['流氓软件','类似百度']
        }
}
#search_engine['国内']['www.baidu.com'][0] = '可以严查'
#print(search_engine)
print(search_engine.values()) # 打印所有的值
search_engine.setdefault('Opera',{'www.opera.com':[0,1,2,3]})
# .setdefault()表示先到字典里查找是否存在这个key
# 若这个key存在，则取出，不存在则新建
print(search_engine)
for i in search_engine:
    # print(i) 打印key
   # print(search_engine.values())
   print(i, search_engine[i]) # 建议使用
for k,v in search_engine.items():
    print(k,v) # 数据量小的时候可以使用

