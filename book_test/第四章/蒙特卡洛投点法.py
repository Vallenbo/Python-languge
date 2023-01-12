from random import *
import time


def MC(n):
    k = 0
    for i in range(n):
        x = random()
        y = random
        if (x * x + y * y) <= 1:
            k = k + 1
    return 4 * k / n


n = int(input("请输入模拟次数，n="))
t0 = time.perf_counter()
print("蒙塔卡洛算法模拟的Pi值为：", MC(n))
t1 = time.perf_counter()
print("程序处理时间为：%。2fs" % (t1 - t0))
