# Mixin即实现多继承
# java中通过interface接口类实现多重继承
# python中本身就支持 多重继承

class vehicle():
    def huo(self):
        print('运输货物')

    def ren(self):
        print('搭载乘客')


class FlyingMixin(): #飞行器   Mixin类表示混入类，增加功能的类
    def fly(self):
        print('飞行器')


class car(vehicle):
    pass


class airplane(vehicle,FlyingMixin):
    pass
