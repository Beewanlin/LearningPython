import urllib.request

opener = urllib.request.build_opener()
opener.addheaders.append(('Cookie', 'email=XXXXXXX@163.com'))
url = 'https://www.apple.com'
response = opener.open(url)
print(response.headers)
