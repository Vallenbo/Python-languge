from numpy import *

A = zeros((3, 3), dtype=float)
f = open(r'E:\Project\Python\book_test\第五章\test.txt')
lines = f.readlines()
A_row = 0
for line in lines:
    list = line.strip('\n').split(' ')
    A[A_row:] = list[0:3]
    A_row += 1
    print(line)
print(A)
