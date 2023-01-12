class cart():
    color = '白色'
    brand = '奥迪'
    pailiang = 2.4

    def lahuo(self):
        print("小汽车能拉货")

    def doufeng(self):
        print("小汽车能兜风")

    def bamei(self):
        print("把妹功能")

    def func():
        print("这个没有self形参")



class1 = cart() #创建对象

print(cart.color)
cart.bamei()
cart.func()


# del class1.brand
# print(class1.brand)


# class1.bamei()  #调用方法
# print(class1.color) #调用属性


# class1.color = '黑色' #修改对象的属性
# print(class1.color)
# class1.a = '1'  #给对象添加属性
# del class1.a    #删除外部添加的属性，class类定义的属性不能删除
# print(class1.a)



