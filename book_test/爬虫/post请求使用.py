import requests
url = 'https://fanyi.baidu.com/sug'

# 定义请求头信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}

# post发送的数据
data = {'kw': ''}
data['kw'] = input('请输入需要翻译的数据:')

# 发送请求
res = requests.post(url=url, headers=headers, data=data)

# 接受返回数据
code = res.status_code
if code == 200:
    print(f'请求成功:{code}k')
    data = res.json()
    if data['errno'] == 0:
        print('响应成功')
        for i in data['data']:
            print(i['k'],i['v'])
print(res.json())
