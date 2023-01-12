import pymysql

# 1链接mysql数据库
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='python_test',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)  # 设置数据类型，这里为dict字典类型

# 2创建游标对象
cursor = connection.cursor()

# 3准备sql
sql = 'select * from txl'

# 4用游标对象执行sql
cursor.execute(sql)

# 5提取结果，fetchall()提取所有结果，fetone()提取一条结果
row = cursor.fetchall()  # 提取所有结果
print(f"{sql}", row[0].keys())
# 6关闭数据库连接
cursor.close()  # 关闭游标
connection.close()  # 关闭连接
