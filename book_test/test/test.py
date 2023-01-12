import random
import time

l1 = [1, 2, 3, 4]
l2 = [[]]
print(l1.__len__())

for i in range(l1.__len__()):
    l2.append(i)

print(__name__)


# a = 100
# b = False
#
# print(a * b)

# print (chr(65))
# print(eval("1"+"1"))
#

# print(eval("'Hello'"))


# print(random.uniform(1,2))
# print(random.seed(1))
# print(time.time())
#
# Python =1

# print(1 or 2)

#
# print(max(['11','2','3']))
# print(min(['11','2','3']))
# print(type(pow(3,0.5)*pow(3,0.5)))
# print(pow(3,0.5)*pow(3,0.5) == 3)
# print(0.1+0.2)
# print(type(0.1+0.2))


# w = input('请输入数字和字母构成的字符串：')
# for x in w:
#     if '0' <= x <= '9':
#         continue
#     else:
#         w.replace(x, '')
# print(w)

# k = 0
# while True:
#     s = input('请输入 q 退出：')
#     if s == 'q':
#         k += 1
#         continue
#     else:
#         k += 2
#         break
# print(k)

#
# num = input("从键盘输入五个数:").split(',')
# print(num)
# for i in num:
#     print("{:>10}".format(i), end="")


# L2 = [1, 2, 3, 4]
# L3 = L2.reverse()
# print(L3)

# x = { 200, 'flg', 20.3}
# print(x)
# x = {'flg': 20.3}
# print(x)
# ds = {'av': 2, 'vr': 4, 'ls': 9, 'path': 6}
# print(ds.popitem())
# print(len(ds))
# for i in range(5):
#     print(i)

# ls = [2, 0, 6]
# x = 100
# try:
#     for i in ls:
#         y = 100 // i
#     print(y)
# except:
#     print('error')


# s="〇一二三四五六七八九"
# a = eval(input("请输入数字："))
# print(s[a-1])


# n=random.randint(96,97)
# print(n)


# while True:
#     s = input("请输入不带数字的文本:")
#     i = 0
#     for p in s:
#         if "0" <= p <= "9":
#             i = i + 1
#     if i == 0:
#         break
# print(len(s))


# for i in range(1000):
#     if i<100:
#         continue
#     s = 0
#     a = int(i//100)
#     b = int(i//10%10)
#     c = int(i%10)
#     s = a**3+b**3+c**3
#     if s == i:
#         print("{} 是水仙花数".format(i))

# s =input()
# print("倒序为：",s[::-1],"字符数为：",len(s),end="")


# s = input("请输入文本:")
# i = j = 0
# for p in s:
#     if "0" <= p <= "9":
#         i = i + 1
#     if p.isalpha():
#         j = j + 1
#
# print(f"数字为{i}个，字母为{j}个")

# sen = "abc,123,4,789,mnp"
# a = ''
# for i in sen:
#     if i != ',':
#         a += i
# sen = a
# print(sen)

def reverse_dict(dic):
    out = dict(zip(dic.values(), dic.keys()))
    return out


dic = eval(input("请输入一个字典："))
dic = reverse_dict(dic)
print(dic)
