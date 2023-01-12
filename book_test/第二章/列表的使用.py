list = ['你好', '世界', '!']  # 列表：多种类型可修改元素
# 定义：int基本类型
print(list)
print(list[0], list[1] + list[2])
print(list[1:])

list1 = [1, 2, 3]
print(list1[:-1])  # 输出：反向索引进行
print(list1[0], list1[1] + list1[2])
del list1[1]  # 删除：根据索引
print(bool(list1))  # 判断：非空判断
print(list1.index(1))  # 查找：根据索引输出内容，也可以根据内容输出索引

list2 = ['孙悟空', '猪八戒', '唐僧']
list2.append('沙和尚')  # 添加：只能添加一个元素
list2.append(['沙和尚', 1])  # []内为一个元素
print(list2)
list2.extend(['钢铁侠', '蜘蛛侠'])  # 添加：多个元素
print(list2[2:])
list1.extend(list2)  # 添加：合并列表
print(list1)
list2.insert(-1, '插入的元素')  # 插入：根据索引
print(list2)

list = [list1, list2]  # 添加：嵌套列表
print(list)

list3 = ['你','我','他','!']
list3.pop(1) #删除：通过索引
print(list3)
del list3[0] #删除：通过索引
print(list3)
list3.remove("!") #删除：第一个匹配到的元素内容
print(list3)
list3.clear() #删除：清除元素内容
print(list3)

list = [1,2,3,4]
print(list[::2])
