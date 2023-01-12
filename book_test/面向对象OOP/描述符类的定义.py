# class ScoreManage():    #第一种方式实现描述符类
#     def __get__(self, instance, owner):
#         pass
#     def __set__(self, instance, value):
#         pass
#     def __del__(self):
#         pass
#
# class Student():
#     score= ScoreManage()


# class Student():
#     def getscore(self):
#         pass
#     def setscore(self):
#         pass
#     def delscore(self):
#         pass
#
#     #第二种方法，通过property指定对应的三个描述符方法
#     score = property(getscore,setscore,delscore)

class Student():
    __score = None

    @property   #第三种描述符定义格式
    def score(self):
        print("get")
        return self.__score

    @score.setter
    def score(self,value):
        print("set")
        self.__score = value

    @score.deleter
    def score(self):
        print("del")
        del self.__score

