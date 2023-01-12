x = int(input("请输入数字"))
y = 1
num = str()
if x > x > 2 ** 31 - 1 or x < -2 ** 31 - 1 or x == 0:
    print(0)

else:
    if x < 0:
        y = -1
        x = x * -1
        x = str(x)

    for i in x:
        num = i + num

    print(int(num) * y)
