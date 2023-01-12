class cart():
    color = '白色'
    _brand = '奥迪'       #受保护
    __pailiang = 2.4    #私有的

    def lahuo(self):
        print("小汽车能拉货")

cat = cart()
print(cat._brand)
# print(cat.__pailiang)

class aircarft():
    air = "天空"


class baoma(cart):  #继承父类的属性
    produce = "湖南"


class baoma_1(cart,aircarft):    #多继承
    def print_baoma1(self):
        print(f"这是多继承的子类,父的color:{super().color},母的air:{super().air}")

cat1 = baoma()
print(cat1.color)

print(hasattr(cart,'lahuo'))

baoma1 = baoma_1()
baoma1.print_baoma1()

