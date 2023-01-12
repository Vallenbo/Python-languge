class base:
    name = ""
    HP = 0
    attack_power = 0
    armor = 0
    drugs = 0

class Other(base):
    def __init__(self, name, HP, attack_power, armor, drugs):
        self.name = name
        self.HP = HP  # 血量
        self.attack_power = attack_power  # 攻击力
        self.armor = armor  # 护甲
        self.drugs = drugs  # 药品

    def attack(self, dog):
        if self.attack_power > dog.armor:
            print("发起攻击")
            num = self.attack_power - dog.armor
            print(f"造成伤害:{num}")
            dog.HP -= num
        else:
            print("敌人护甲过高，攻击没有穿透！")

    def defense(self):  # 防御
        self.attack_power += 2
        self.armor += 2
        print(f"{self.name}当前处于防御状态,攻击力和防御值增加了2点")

    def treatment(self):  # 治疗
        if self.drugs > 0:
            self.HP += 100
            self.drugs -= 1
            print(f"{self.name}生命值增加了100点")
        else:
            print("没有药品可用！")


print("***欢迎来到猫狗游戏***")
cat = Other(input("请输入您的角色名字:"), 10, 3, 2, 1)
print(f"角色创建成功: {cat.name}")
dog = Other("dog", 4, 5, 3, 0)
print(f"敌人已生成: {dog.name}")

while True:
    for i in range(9):
        if i == 0 or i == 8:
            print("#" * 50)
        elif i == 2:
            print(" " * 5 + f"🐱{cat.name}" + " " * 20 + "🐶狗" + " ")
        elif i == 3:
            print(f"血量:{cat.HP},攻击力{cat.attack_power}" + " " * 22 + f"血量:{dog.HP},攻击力{dog.attack_power}")
        elif i == 4:
            print(f"护甲{cat.armor}, 携带药品{cat.drugs}" + " " * 22 + f"护甲{dog.armor}")
        elif i == 7:
            print("#" + " " * 6 + "1、攻击" + " " * 6 + "2、防御" + " " * 6 + "3、使用药包" + " " * 9 + "#")
        else:
            print("#" + " " * 48 + "#")

    if dog.HP <= 0:
        print(f"you win ,你的角色{cat.name}打败了敌人")
        break
    if cat.HP <= 0:
        print(f"you fail ,敌人打败了你的角色{cat.name}")
        break

    x = input("请输入你的操作（输入任意键退出）:")
    if x == "1":
        cat.attack(dog)
    elif x == "2":
        cat.defense()
    elif x == "3":
        cat.treatment()
    else:
        break
