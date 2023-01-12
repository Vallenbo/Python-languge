from flask import Flask, render_template, request
import pymysql, time
import requests

app = Flask(__name__)


# 封装SQL语句函数
def mysql_conn(sql, m='r'):
    conn = pymysql.connect(host='127.0.0.1',
                           user='root',
                           password='123456',
                           db='python_test',
                           charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)  # 设置数据类型，这里为dict字典类型
    cursor = conn.cursor()  # 创建游标
    try:
        cursor.execute(sql)  # 执行sql语句
        if m == 'r':
            data = cursor.fetchall()  # 去除全部数据
        elif m == 'w':
            conn.commit()
            data = cursor.rowcount  # 打印行数
    except:
        data = False
        conn.rollback()
        print('输入失败，已进行回滚！')
    conn.close()
    return data


# 首页,将mysql中表的值读出并传到首页----查
@app.route('/')
def index():
    data = mysql_conn('select * from stu')
    return render_template('txl.html', userlist=data)


# 返回到添加操作的界面
@app.route("/add/")
def add():
    return render_template('add.html')


# 接受添加的数据,写入数据库----增
@app.route("/adds/", methods=["POST"])  # post大写,因为post是通过form.data传数据所以下面用request.form
def adds():
    data = dict(request.form)
    print(data)
    sql = "insert into stu values ('{id}','{name}','{age}','{sex}','{class}','{tel_num}','{adds}')".format(**data)
    res = mysql_conn(sql, m='w')
    if res:
        return '<script>alert("添加成功");location.href="/";</script>'  # script注入成功，重定向至根
    else:
        return '<script>alert("添加失败");location.href="/";</script>'


# 返回到更改界面
@app.route('/change')
def ch():
    idd = request.args.get('id')
    data = mysql_conn(f'select * from stu where id={idd}')
    return render_template('change.html', userlist=data)


# 检察更改的数据并更新数据库----改
@app.route('/chas', methods=["POST"])
def chas():
    data = dict(request.form)
    res = mysql_conn("update stu set name='{name}',age='{age}',sex='{sex}',class='{class}',"
                     "tel_num='{tel_num}',adds='{adds}' where id={id}".format(**data), m='w')
    if res:
        return '<script>alert("更新成功");location.href="/";</script>'
    else:
        return '<script>alert("未更新");location.href="/";</script>'


# 删除数据----删
@app.route('/del')
def de():
    __id = request.args.get('id')
    res = mysql_conn(f'delete from stu where id={__id}', m='w')
    if res:
        return '<script>alert("删除成功");location.href="/";</script>'
    else:
        return '<script>alert("删除失败");location.href="/";</script>'


@app.route('/lyb')
def lyb():
    data = mysql_conn('select * from lyb')
    return render_template('lyb.html', lyb=data)


@app.route("/insert")
def insert():
    return render_template('lybadd.html')


@app.route("/lybadd", methods=["POST"])  # post大写,因为post是通过form.data传数据所以下面用request.form
def lybadd():
    data = request.form.to_dict()
    print(data)
    data['date'] = time.strftime('%Y-%m-%d %H:%I:%S')
    sql = f"insert into lyb values(null,'{data['name']}','{data['info']}','{data['date']}')"
    print(sql)
    res = mysql_conn(sql, m='w')
    if res:
        return '<script>alert("添加成功");location.href="/lyb";</script>'  # script注入成功，重定向至根
    else:
        return '<script>alert("添加失败");location.href="/lyb";</script>'


@app.route('/translate')
def trans():
    recode = {'info':'请输入翻译内容'}
    return render_template('translate.html',recode= recode)


@app.route('/translates', methods=["POST"])
def translate():
    url = 'https://fanyi.baidu.com/sug'
    # 定义请求头信息
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    }
    # post发送的数据
    recode = request.form.to_dict()
    data = {'kw': recode['info']}
    # 发送请求
    res = requests.post(url=url, headers=headers, data=data)
    # 接受返回数据
    code = res.status_code
    if code == 200:
        print(f'请求成功:{code}k')
        data = res.json()
        if len(data['data']):
            print('响应成功')
            print(res.json())
            return render_template('translate.html', data=data['data'],recode = recode)
        else:
            return f'<script>alert("翻译失败");location.href="/translate";</script>'  # script注入成功，重定向至根


# 运行
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='8080')
