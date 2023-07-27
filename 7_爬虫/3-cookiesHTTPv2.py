import urllib.request

"""
如果要自定义cookie的值，则可以在生成自定义opener之后，通过给addheaders添加属性来自定义cookie的值
"""
opener = urllib.request.build_opener()
opener.addheaders.append(('Cookie', 'email=XXXXXXX@163.com'))
url = 'https://www.apple.com'
response = opener.open(url)
print(response.headers)
