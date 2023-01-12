f4 = ['唐僧', '孙悟空', '猪八戒', '沙和尚']
f5 = (1, 2, 3, 4, 5)

iter_f4 = iter(f4)  # 创建迭代对象
# 迭代器一定是一个可迭代对象，可迭代对象不一定是迭代器
print(next(iter_f4))  # next函数指向下一个元素

from collections.abc import Iterable, Iterator

print(isinstance(f4, list))  # isinstance函数检测数据是不是某一个类型
print(isinstance(iter_f4, Iterator))  # 也可用来检测是不是Iterator迭代器

for i in zip(f4, f5): #将每个容器内的相同下标的元素组成一个新的元组迭代器
    print(i)
