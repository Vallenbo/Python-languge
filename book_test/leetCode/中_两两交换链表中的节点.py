l1 = [1, 2, 3, 4]

for i in range(len(l1)):
    if i % 2 == 0 and len(l1) != 1:
        x = l1[i]
        l1[i] = l1[i + 1]
        l1[i + 1] = x

print(l1)
