import pickle,json

var1 = [{'name': 'admin'}]

res = json.dumps(var1)
print(res)
print(json.loads(res))

with open('../test/1.txt', 'w+') as dp:
    json.dump(var1, dp)
    dp.seek(0)
    x = json.load(dp)




print(x)
"""
var = 'i love you'
res = pickle.dumps(var) #序列化
print(res)

print(pickle.loads(res)) #反序列化

with open('1.txt','wb+') as dp:
    dp.write(res)
    dp.seek(0)
    dp.read()
    pickle.dump(var,dp) #将python对象以二进制形式写入open文件对象中
"""
