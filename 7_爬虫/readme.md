爬虫，就是从一组初始待抓取的url中收集有用信息的同事，捕获新的待抓取的url，并不断往复这个过程，逐渐得到庞大的已/待抓取url列表并过滤有用信息。

学习爬虫，首先学习熟悉如何用python发出http请求，推荐使用的是requests模块。（urllib模块了解即可）

headers中的user-agent、referer有时用来反爬虫。
user-agent：有些服务器或者Proxy会通过该值来判断是否是浏览器发出的请求。
referer：表示你是从哪个网页来到这个网页的，服务器有时候用referer检查防盗链。
因此，在爬虫实现时需要设置一下headers里的 user-agent 和 referer 这两个参数。

headers中的content-type：
在使用REST接口时，服务器会检查这个值来确定该如何解析请求体内容。常用的值有：
（1）application/XML (在XML RPC，如RESTful/SOAP调用时使用)
（2）application/json（在json RPC中调用时使用）
（3）application/x-www-form-urlencoded（浏览器提交web表单时使用）


cookie的设置是很有必要的。一般首步登录时服务器会给当前用户分配一个cookie，之后请求时把cookie带上，系统才不会把当前用户当成非法用户。
使用session处理cookie