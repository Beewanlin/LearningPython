import http.cookiejar
import urllib.request

# 获取网站cookie
# 声明一个CookieJar对象实例来保存cookie
cookie = http.cookiejar.CookieJar()
# 利用HTTPCookieProcessor来构建一个Handler
handler = urllib.request.HTTPCookieProcessor(cookie)
# 利用build_opener()方法构建出Opener
opener = urllib.request.build_opener(handler)


targeturl = 'https://www.baidu.com'
# 访问目标网页
response = opener.open(targeturl)
for item in cookie:
    print(item)


