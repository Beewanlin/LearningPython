"""
在Python中，通过CookieJar函数来实现对cookie的处理。即：先获取，再保存，之后请求时带上。
该脚本的目的是获取访问目标网页的cookies，通过urllib自动获取。

在Python3中，需要先引入http.cookiejar模块，再调用其模块内的函数。

"""

import http.cookiejar
import by_urllib.request

# 获取网站cookie
# 声明一个CookieJar对象实例来保存cookie
cookie = http.cookiejar.CookieJar()
# 利用HTTPCookieProcessor来构建一个Handler，作为cookie处理器
handler = by_urllib.request.HTTPCookieProcessor(cookie)
# 通过handler构建Opener
opener = by_urllib.request.build_opener(handler)
# 访问目标网页，cookie会由opener自动获取并存到之前创建的CookieJar对象实例中
targeturl = 'https://www.baidu.com'
response = opener.open(targeturl)
# 打印获取到的cookie
for item in cookie:
    print(item)


