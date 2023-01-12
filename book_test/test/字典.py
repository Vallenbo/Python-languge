dict1 = {1: 'a', 2: 'b', 3: 'c'}
dict2 = {'a': 1, 'b': 2, 'c': 3}
dict3 = {}

print(dict1.keys())
print(dict1.values())

print(dict1.items())

for x, y in dict1.items():  #键值交换
    dict2[y] = x

print(dict2)
print({y:x for x,y in dict1.items()}) #字典推导式

list1 = [y for x,y in dict2.items() if y%2==0]
print(list1) #字典推导式

