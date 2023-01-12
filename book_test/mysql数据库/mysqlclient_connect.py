import MySQLdb

conn = MySQLdb.connect(host='localhost', db='python_test', user='root', password='123456')

try:
    cur = conn.cursor()
    sql = 'select * from txl'
    sql1 = "insert into txl values (1,'李白','123','123@qq.com','长沙')"

    res = cur.execute(sql1)
    if res:
        conn.commit()
        print("插入成功！！！")
    else:
        conn.rollback()

    # res = cur.fetchall()
    # for i in res:
    #     print(f"语句为{sql},结果为：", i)

finally:
    cur.close()
    conn.close()
