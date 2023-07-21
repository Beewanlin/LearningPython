

import urllib3


pool_manager = urllib3.PoolManager()


url1 = 'https://www.baidu.com'
url2 = 'https://www.zhihu.com'
url3 = 'https://www.apple.com'

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 ' \
             'Safari/537.36 '
referer = 'https://www.sina.com.cn'
headers = {'User-Agent': user_agent, 'referer': referer}

req1 = pool_manager.request('GET', url1, headers=headers)
req2 = pool_manager.request('GET', url2, headers=headers)
req3 = pool_manager.request('GET', url3, headers=headers)

res1 = urllib3.PoolManager.urlopen(req1)
res2 = urllib3.PoolManager.urlopen(req2)
res3 = urllib3.PoolManager.urlopen(req3)

