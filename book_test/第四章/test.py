from datetime import date  # 从模块包中导入模块

print(date.today())

print('标准内置函数', abs(-200))

a = '猪八戒'
a1 = ''
for i in reversed(a):
    a1 += i
print('原始字符串：', a)
print('反转字符串', a1)


def mltui_sum(*args):  # 定义可变参数
    s = 0
    for i in args:
        s += i
    return s, i


s = mltui_sum(3, 4, 5)  # 调用函数，传递一个实参列表
print(s)  # 多个返回值时，默认为元组类型
print('类似C语言的输出语句：%10d' % (3 + 10))



