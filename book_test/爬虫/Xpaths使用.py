from lxml import etree

text = '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>标题</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="css/style.css" rel="stylesheet">
    </head>
    <body>
        <form method="get" action='/registuser'>
            <label>用户名：<input type="text" name="user" value=""></label>
            <label>密码：<input type="password" name="password" value=""></label>
            <input type="submit" value="注册">
        </form>
    </body>
</html>

'''

# 使用etree解析html字符串
html = etree.HTML(text)

# 提取数据,文档节点/元素子节点/属性节点/基本值
r = html.xpath('/html/head/title/text()')
print(r)
