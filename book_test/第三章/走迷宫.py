# 【定义迷宫路径】
my_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 2, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# 【精灵起点与迷宫出口】
x, y = 1, 2
end_x, end_y = 9, 4


# 【打印迷宫】
def print_map():
    for m in my_map:
        for n in m:
            if n == 1:
                print('■', end='')
            elif n == 0:
                print('  ', end='')
            else:
                print('☆', end='')
        print('')


print_map()

# 【游戏主循环】
while True:
    print('☆表示精灵当前位置')

    # 【检测玩家输入】
    key = input('请输入指令【w上, s下, a左，d右】：')

    # 【碰撞检测】
    if key == 'a':
        x = x - 1
        if my_map[y][x] == 1:
            print('囧，碰壁了，游戏结束！')
            break
        else:
            my_map[y][x], my_map[y][x + 1] = \
                my_map[y][x + 1], my_map[y][x]
            print_map()
    elif key == 's':
        y = y + 1
        if my_map[y][x] == 1:
            print('囧，碰壁了，游戏结束！')
            break
        else:
            my_map[y][x], my_map[y - 1][x] = \
                my_map[y - 1][x], my_map[y][x]
            print_map()
    elif key == 'd':
        x = x + 1
        if my_map[y][x] == 1:
            print('囧，碰壁了，游戏结束！')
            break
        else:
            my_map[y][x], my_map[y][x - 1] = \
                my_map[y][x - 1], my_map[y][x]
            print_map()
            if my_map[y][x] == my_map[end_y][end_x]:
                print('恭喜你，过关了！^_^')
                break
    elif key == 'w':
        y = y - 1
        if my_map[y][x] == 1:
            print('囧，碰壁了，游戏结束！')
            break
        else:
            my_map[y][x], my_map[y + 1][x] = \
                my_map[y + 1][x], my_map[y][x]
            print_map()

    # 【检测玩家输入错误】
    else:
        print('输入指令错误，请重新输入指令：')
        continue
