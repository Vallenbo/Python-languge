f5 = ('1', '2', '3', '4', 5) # 转化为=>[1,2,3,4]
new_f5= []
new1_f5 = []

for i in f5:
    new_f5.append(int (i))  #用for进行转化
print(new_f5)


print(list(map(int,f5))) #用map函数将元素转化为int类型

