print(len('孙悟空')) #字符串的长度
print(len('孙悟空')*2)

num = None #空值
print(num)

num1='猪八戒'
print(num1 * 2)
print(num1[1])
print(num1[1:])
print(num1[1:3]) #输出的内容不包括尾索引（即尾索引前一个）

num1 = r"你好\n" #r表示输出原字符
print(num1)

num2 = num1.replace('你','我') #原字符串不能进行修改，只能进行赋值修改
print(num2)
