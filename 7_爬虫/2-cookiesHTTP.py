import http.cookiejar
import urllib.request

# 获取网站cookie
# 声明一个CookieJar对象实例来保存cookie
cookie = http.cookiejar.CookieJar()
# 利用HTTPCookieProcessor来构建一个Handler，作为cookie处理器
handler = urllib.request.HTTPCookieProcessor(cookie)
# 通过handler构建Opener
opener = urllib.request.build_opener(handler)


targeturl = 'https://www.baidu.com'
# 访问目标网页
response = opener.open(targeturl)
for item in cookie:
    print(item)


