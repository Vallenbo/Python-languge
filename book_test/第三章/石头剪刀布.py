import random

win = [[1, 2], [2, 3], [3, 1]]

while True:
    num = random.randint(1, 3)
    print(num)
    num1 = int(input('请输入【1、石头】【2、剪刀】【3、布】='))
    if num1 not in range(1, 4, 1):
        print('Enter error ,please enter again!!!')
    elif num == num1:
        print("It is draw")
    elif [num1, num] not in win:
        print('You are fail,please enter again!!!')
    else:
        print('You are win!!!')
        exit()
