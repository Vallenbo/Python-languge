str = [5, 6, 7, 8]
list1 = [1, 2, 3, 4]

list1 = [int(i) * 2 for i in str]
print(list)

"""
list = [(x, y) for x in list for y in str if x != y]
print(list)
"""

list1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]

list1 = [[y[x] for y in list1] for x in range(4)]
print(list1)


#练习
#['user=admin','age=20']
set2 = {'user':'admin','age':'20','phone':'133'}
list2 = [y+'='+x for x in set2.values() for y in set2.keys()]
print(list2)


list3=['AAA','BBB','CCC','DDD']
list3= [ i.lower() for i in list3]
print(list3)

list4=[]
list4=[(x,y) for x in range(6) for y in range(6) if x%2==0 and y%2==1]
print(list4)

# 九九乘法表
list1= [f'{x}*{y}={x*y}' for x in range(1,10) for y in range(1,x+1)]
print(list1)

