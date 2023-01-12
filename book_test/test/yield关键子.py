a, b = 0, 0


def function():
    print("1")
    yield 1
    print("2")
    yield 2
    print("3")
    yield 3


tuple1 = function()  # generator生成器
print(tuple1)


# 斐波那契数列
def fibo(num):
    a, b, i = 0, 1, 0
    while i < num:
        print(b)
        a, b = b, a + b
        i+=1

fibo(6)


