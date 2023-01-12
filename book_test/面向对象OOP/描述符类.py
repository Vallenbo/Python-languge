class Foo:      #Foo是新式类，它实现了三种方法，这个类就被称作一个描述符
    def __get__(self, instance, owner):
        pass
    def __set__(self, instance, value):
        pass
    def __delete__(self, instance):
        pass