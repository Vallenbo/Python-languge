from lxml import etree

# 读取一个html文件并解析
html = etree.parse('E:\\Project\\Python\\book_test\\flask\\templates\\login.html', etree.HTMLParser())
print(html)

# 转成二进制文本流
r = html.xpath('//title/text()')  # 直接找到所有title标题
r = html.xpath('//title[@class="teacher"]/text()')  # 查找元素中class=teacher的title标题
print(r)
