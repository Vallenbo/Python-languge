import requests

url = 'https://fanyi.baidu.com/sug'

#定义请求头信息
headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}

res = requests.get(url=url,headers=headers)
status_code = res.status_code

print(status_code)

if status_code == 200:
    with open('test.html','w',encoding='utf-8') as fp:
        fp.write(res.text)
