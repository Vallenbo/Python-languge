import requests

# 定义请求的url
url = 'http://www.baidu.com'

# 发起get请求
res = requests.get(url=url)

# 获取响应结果
print(res) #返回状态对象<Response [200]>
print(res.content) #返回内容，二进制文本流 b'<
print(res.text) #直接获取响应内容
print(res.request.headers) #请求头信息
print(res.headers) #响应头信息
print(res.status_code) #响应状态码，200是ok
print(res.url) #请求的url地址
