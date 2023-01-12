l1 = [2, 4, 3]
l2 = [5, 6, 4]

if len(l1) >len(l2):
    min1 = len(l2)
    max1 = len(l1)
else:
    min1 = len(l1)
    max1 = len(l2)

l = []

for i in range(3):
    if 9 < l1[i]+l2[i]:
        l.append(l1[i]+l2[i]%10)


print(l)
