switch_dicts = {}


def deco(data):
    def wrapper(func):
        if data not in switch_dicts.keys():
            switch_dicts[data] = func

        def wrapper1(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper1
    return wrapper


@deco(1)
def case1(*args, **kwargs):
    print("case1")


@deco(2)
def case1(*args, **kwargs):
    print("case2")


@deco(3)
def case1(*args, **kwargs):
    print("case3")


# 装饰器自动运行时，会自动将1，2，3装入字典中
print(switch_dicts)
#调用字典中key为1所指向的函数
print(switch_dicts[1]())
