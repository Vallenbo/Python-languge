import abc


# 抽象类需要导包并进行继承
# 抽象类无法创建对象

class Writecode(metaclass=abc.ABCMeta):
    # 抽象方法需要使用装饰器abstractmethod进行装饰
    @abc.abstractmethod
    def write_php(self):
        pass

    @staticmethod
    def write_java(self):
        print('实现了 java代码的开发')

    def write_python(self):
        print('实现了 python代码的开发')

# 抽象类需要定义子类继承抽象类，并实现抽象方法
