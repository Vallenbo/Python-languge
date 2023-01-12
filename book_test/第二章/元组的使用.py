tuple1 = ('张飞', '赵云', 3, 4, 5)  # 定义：元组可以没有括号
print(tuple1[1])  # 访问：通过下标访问

tuple2 = '你', '我', '他'
tuple2 += tuple1  # 连接
print(tuple2)

del tuple2  # 删除：不能删除单个元素
# print(tuple2)
print(tuple1[0] + tuple1[4])

# 元组不能添加删除元素
