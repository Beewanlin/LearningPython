"""
lxml也是一个可以解析html文档的库，其实BeautifulSoup也可以选择lxml作为解析库。
xpath为xml语言，
lxml可以自动修正存在部分错误的html文档
"""
import csv

from lxml import etree
import requests
import re

# 先爬取网页，获取html文档
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/91.0.4472.101 Safari/537.36'}
target_url = "https://www.douguo.com/jingxuan/0"


def parse_byXpath(html_file):
    # 读取保存在本地的网页，进行xpath解析
    with open(html_file, 'r') as stream:
        html_content = stream.read()
        html = etree.HTML(html_content)
        # 按照xpath规则查找特定内容1-超链接：
        rule1_links = '//ul[@id="jxlist"]/li/a/@href'
        res1_links = html.xpath(rule1_links)
        print(res1_links)
        # 按照xpath规则查找特定内容2-图片：
        rule2_images = '//ul[@id="jxlist"]/li/a/img/@src'
        res2_images = html.xpath(rule2_images)
        # 按照xpath规则查找特定内容3-文本：
        rule2_text = '//ul[@id="jxlist"]/li/div/a[1]/text()'
        res3_text = html.xpath(rule2_text)
        pattern = re.compile(r"\n+|\s+", re.S)
        res3 = [pattern.sub('', res3_text[u]) for u in range(1, len(res3_text), 2)]
        print(res3)
        return zip(res1_links, res2_images, res3)


def save_parsed_content(contents):
    with open('parsed_content.csv', 'a') as stream:
        writer = csv.writer(stream)
        writer.writerows(contents)


if __name__ == "__main__":
    response = requests.get(url=target_url, headers=headers)
    # 将爬取到的html文件写入本地：
    html_file = 'test.html'
    with open(html_file, 'wb') as stream:
        stream.write(response.content)
    # 解析html文档：
    contents = parse_byXpath(html_file)
    # 存储解析好的内容：
    save_parsed_content(contents)