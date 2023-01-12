class Student():
    def __init__(self, id, name, score):
        self.id = id
        self.name = name

    def retrunMe(self):
        info = f'''
        学员编号：{self.id}
        学员姓名：{self.name}
        学员分数：{self.score}
        '''
        print(info)

    def __setattr__(self, key, value):
        if key == 'score':
            if value >= 0 & value <= 100:
                object.__setattr__(self, key, value)
            else:
                print('分数不符合要求')
        else:
            object.__setattr__(self, key, value)


zs = Student(1011, '张三丰', 99)
zs.score = -20
zs.retrunMe()
