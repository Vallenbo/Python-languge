"""
#1、打开文件
fp = open('1.txt','r',encoding='utf-8')
print(fp,type(fp))
#2、读写操作
#fp.write('hello world!')
res = fp.read()
print(res)
#3、关闭文件
fp.close()
"""
# 高级写法
with open('1.txt', 'r+', encoding='utf-8') as fp:
    fp.read(3)
    print(fp.tell())
    fp.write('abc')
    print(fp.tell())


