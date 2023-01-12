from flask import Flask, render_template
import pymysql

app = Flask(__name__)


@app.route("/show")
def index():
    data = model('select * from lyb')
    print(data)
    return render_template('index.html', data=data)


@app.route("/txl")  # 通讯录接口
def txl():
    data = model('select * from txl')
    print(data)
    return render_template('txl.html', data=data)


@app.route('/love')
def love():
    return 'i love you '


def model(sql):
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='123456',
                           db='python_test',
                           charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)  # 设置数据类型，这里为dict字典类型
    try:
        cursor = conn.cursor()
        row = cursor.execute(sql)
        conn.commit()
        data = cursor.fetchall()  # 提取所有结果
        if data:
            return data
        else:
            return row
    except:
        conn.rollback()
    finally:
        # 6关闭数据库连接
        cursor.close()  # 关闭游标
        conn.close()  # 关闭连接


# 获取登录参数及处理
@app.route('/login')
def getLoginRequest():
    # 查询用户名及密码是否匹配及存在
    # 连接数据库,此前在数据库中创建数据库TESTDB
    db = pymysql.connect("localhost", "root", "123456", "TESTDB")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = "select * from user where user=" + request.args.get('user') + " and password=" + request.args.get(
        'password') + ""
    try:
        # 执行sql语句
        cursor.execute(sql)
        results = cursor.fetchall()
        print(len(results))
        if len(results) == 1:
            return '登录成功'
        else:
            return '用户名或密码不正确'
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        traceback.print_exc()
        db.rollback()
    # 关闭数据库连接
    db.close()



if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='8080')
