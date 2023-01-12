import string

arr = [-9,10,1,5,3,-2]
arr1= ['a','b','c','d']
a = "A"

print(ord(a))

print(sorted(arr,reverse=True))

print(sorted(arr,key=abs)) #将arr容器内的元素单个传入key对应的函数处理后进行排序

print(list(map(lambda x:x*2,arr)))


print(list(map(ord,arr1)))
arr[-2:]='a'
print(arr)



