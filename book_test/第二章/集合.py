set1 = {1, 2, 3, 4, 5}  # 集合:就是只有键的字典

set2 = set(('长江', '黄河'))  # 转换：将元组转换为集合
print(set2)
set1.add('赵云')  # 添加:元素
print(set1)
set1.remove(1)  # 删除：根据元素内容
print(set1)

print(set1 & set2)  # 集合的运算
print(set1 | set2)
print(set1 ^ set2)

print(set1 < set2)  # 判断：是否有子集关系
print(set1 == set2)  # 判断：是否相等
