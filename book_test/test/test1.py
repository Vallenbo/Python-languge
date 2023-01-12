import re
text = '1+1=2 # 这是客观真理\n'\
 ' 1+1>2 # 这是团结的力量\n'\
 ' 1+1<2 # 这是内斗结果\n'
res = re.sub(r'#.*$', r'', text, 0, re.M)
print('源字符串为：\n', text)
print('删除注释后：\n', res)