"""
除了从访问网页后获取到cookies，还可以自定义cookie的值。
如果要自定义cookie的值，则可以在生成自定义opener之后，通过给addheaders添加属性来自定义cookie的值
"""

import by_urllib.request

opener = by_urllib.request.build_opener()
# 自定义cookies，并添加到请求头中
opener.addheaders.append(('Cookie', 'email=XXXXXXX@163.com'))
url = 'https://www.apple.com'
response = opener.open(url)
print(response.headers)
