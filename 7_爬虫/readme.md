

headers中的user-agent、referer有时用来反爬虫。
user-agent：有些服务器或者Proxy会通过该值来判断是否是浏览器发出的请求。
referer：表示你是从哪个网页来到这个网页的，服务器有时候用referer检查防盗链。

headers中的content-type：
在使用REST接口时，