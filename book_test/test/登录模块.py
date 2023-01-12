from book_test.猫狗游戏.注册模块 import register

def login():
    print("这是登录")


while True:
    print("欢迎来到狗蛋网，请选择您要的功能:")
    print("0 注册")
    print("1 登录")
    print("3 退出")
    x = input("请输入操作:")
    if x == '0':
        register()
    elif x == '1':
        login()
    else:
        break


print("1")
