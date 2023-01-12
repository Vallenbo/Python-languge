import math, sys

x = y = 1  # 链式赋值
x, y, z = 1, 2, '你好'  # 序列赋值
x, y = y, x  # 交换赋值
print(x, y)

a1 = input('请输入一个数字：')  # 默认为字符串类型
a = float(input(r'请输入一个数字:\n'))
b = int(input('请输入一个数字\n'))
a, b = input('请输入一个数字：'), input('请输入一个数字：')
print(a, b)

list1 = ['枯藤', '老树', '昏', '鸦']
for i in list1:
    print('\t' + i + '\t')

print('yes' if list1[0] == '枯藤' else 'no')  # 三元运算符

for i in range(10):  # for循环拓展结构
    print('\t', i, '\t')

print('数字过滤', [s for s in range(10) if s > 5])
