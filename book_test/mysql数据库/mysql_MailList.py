import MySQLdb


class mysql_manager(object):
    def __init__(self):
        try:
            self.conn = MySQLdb.connect(host='localhost', db='python_test', user='root', password='123456')
        except Exception as e:
            print(e)
        else:
            print('!!!MYSQL数据库连接成功!!!')
            self.cur = self.conn.cursor()  # 创建游标

    def show_data(self):
        sql = 'select * from txl'
        self.cur.execute(sql)
        res = self.cur.fetchall()
        print(f"语句为{sql}")
        for i in res:
            print(i)

    def add(self):
        self.__id = input('请输入id：')
        self.__name = input('请输入name：')
        self.__tel_num = input('请输入tel_num：')
        self.__email = input('请输入email：')
        self.__adds = input('请输入adds：')
        sql = f"insert into txl values ({self.__id},'{self.__name}','{self.__tel_num}','{self.__email}','{self.__adds}')"
        res = self.cur.execute(sql)
        if res:
            self.conn.commit()
            print("插入成功！！！")
        else:
            res.rollback()

    def delete(self):
        self.__id = input('请输入需要删除的id：')
        sql = f"DELETE FROM txl where id={self.__id}"
        res = self.cur.execute(sql)
        if res:
            self.conn.commit()
            print("删除成功！！！")
        else:
            self.conn.rollback()
        print(res)

    def modify(self):
        self.__id = input('请输入需要修改的id：')
        sql = "select COLUMN_NAME from information_schema.COLUMNS where table_name = 'txl'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        print("表中字段：", res)
        self.field = input('请输入需要修改的字段名：')
        self.x = input('请输入该字段名的数据：')
        sql = f"UPDATE txl SET {self.field}='{self.x}' where id={self.__id}"
        res = self.cur.execute(sql)
        if res:
            self.conn.commit()
            print("修改成功！！！")
        else:
            self.conn.rollback()

    def find(self):
        self.__id = input('请输入需要查找的id：')
        sql = f"select * from txl where id = {self.__id}"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print(i)
        if not res:
            print('查询id不存在！！')

    def close(self):
        self.cur.close()
        self.conn.close()


connect1 = mysql_manager()

while True:
    print('#########MYSQL同学通讯录#########')
    print('1、显示记录')
    print('2、添加记录')
    print('3、删除记录')
    print('4、查询记录')
    print('5、修改记录')
    print('---按任意键退出程序---')

    i = input("请输入你的操作:")
    if i == "1":
        connect1.show_data()
    elif i == "2":
        connect1.add()
    elif i == "3":
        connect1.delete()
    elif i == "4":
        connect1.find()
    elif i == "5":
        connect1.modify()
    else:
        connect1.close()
        break
