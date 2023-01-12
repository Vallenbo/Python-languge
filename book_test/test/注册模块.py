userlist = []
passwd = []

with open('1.txt', 'a+', encoding='utf-8') as fp:
    fp.seek(0)
    data = fp.readlines()
    for i in data:
        i = i.split(":")
        userlist.append(i[0])
        passwd.append(i[1])


def register():
    account = input("Please enter account :")
    if account in userlist:
        print("Account already exists")
        return

    while True:
        password = input("Please enter password :")
        password1 = input("Please re-enter password :")
        if password == password1:
            break
        print("The two password is inconsistent,please re-enter password:")
    with open('1.txt', 'a+', encoding='utf-8') as fp:
        fp.write(f'{account}:{password}\n')
    print(f'registe is sccuess ,account :{account}')

register()