"""
在requests库中，cookie的处理。
以及重定向。
"""
import requests

user_agent = 'Mozilla/4.0 (compatible;MSIE 5.5,Windows NT)'
headers = {'User-Agent': user_agent}

# 方式1：如果响应体中包含了cookie，则可以从response.cookies中获取到。
r = requests.get('http://www.baidu.com', headers=headers)
for cookie in r.cookies.keys():
    print('cookie:'+r.cookies.get(cookie))

# 方式2：自定义cookie的值
cookies = dict(name='qiye', age='10')
r = requests.get('http://www.baidu.com', headers=headers, cookies=cookies)
print(r.text)

# 方式3：不关心cookie值是多少，只希望访问url时程序能自动把cookie值给带上。采用session的方式。
s = requests.session()
# 首先get访问登录页面，以游客身份，服务器会分配一个cookie
r = s.get('https://www.zhihu.com/signin', allow_redirects=True)  # allow_redirects参数，是否允许请求页面返回重定向。如果允许的话， r.history会返回所有跳转的信息。
datas = {'name': 'qiye', 'passwd': 'qiye'}
# 再次post访问登录页面，带上用户名密码和cookie，游客身份转换为会员身份
r = s.post('https://www.zhihu.com/signin', datas, allow_redirects=True)
print(r.text)

