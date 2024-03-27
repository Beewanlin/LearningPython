import requests
from bs4 import BeautifulSoup


user_agent = 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; de-de)'
headers = {'User-Agent': user_agent}
url = 'https://book.douban.com'

r = requests.get(url=url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser', from_encoding='utf-8')
