"""
urllib3提供线程安全的连接池、文件post上传等强大的功能。

有些服务器会针对headers检查user_agent、content-type、referer。
user-agent：
content-type： 表示请求体的类型。对于REST接口，服务器会检查该值以确定该如何解析内容；对于RESTful或SOAP服务，如果该值设置错误，服务器会拒绝访问。
常用的值有：
（1）application/XML (在XML RPC，如RESTful/SOAP调用时使用)
（2）application/json（在json RPC中调用时使用）
（3）application/x-www-form-urlencoded（浏览器提交web表单时使用）
（注：RPC指的是远程过程调用，指两个应用分别在两台服务器上，不在同一个内存空间而不能直接调用，通过网络来调用）
referer：表示是从哪个网站发起的请求，该参数通常会出现在网页跳转场景的请求中

"""

import urllib3

# 先建立一个PoolManger对象，用于管理连接池
pool_manager = urllib3.PoolManager()

# 定义请求头。
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 ' \
             'Safari/537.36 '
referer = 'https://www.sina.com.cn'
headers = {'User-Agent': user_agent, 'referer': referer}

url1 = 'https://www.baidu.com'
url2 = 'https://www.zhihu.com'
url3 = 'https://www.apple.com'

req1 = pool_manager.request('GET', url1, headers=headers)
req2 = pool_manager.request('GET', url2, headers=headers)
req3 = pool_manager.request('GET', url3, headers=headers)

res1 = urllib3.PoolManager.urlopen(req1)
res2 = urllib3.PoolManager.urlopen(req2)
res3 = urllib3.PoolManager.urlopen(req3)

