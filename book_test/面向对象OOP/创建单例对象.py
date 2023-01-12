#我们都知道创建的多个对象时，对象地址是不一样的
#通过创建单例对象可以使地址一样

class Demo():
    __obj = None #定义私有属性

    def __new__(cls, *args, **kwargs):
        if cls.__obj:   #判断创建对象过程中，是否已经有对象，有则返回
            return cls.__obj
        else:           #没有则创建并返回
            obj = object.__new__(cls)
            cls.__obj = obj
            return obj

a = Demo()
b = Demo()
print(a,b)


