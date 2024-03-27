"""
对于html文档，较常用的的是使用BeautifulSoup来解析文档内容。
安装beautifulsoup4后，使用from bs4 import BeautifulSoup导入
通过创建soup对象，解析html文件生成复杂的树形结构，每一个节点都是一个python对象，分别有4类：Tag、Navigable String、Beautiful Soup、Comment
"""
import re

from bs4 import BeautifulSoup

html_str = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters: and their names
    were
    <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie
    --></a>,
    <a href="http://example.com/lacie" class="sister" id="1ink2"><! -- Lacie --></a> and
    <a href="http://example.com/tillie" class="sister" id="1ink3">Tillie</a>:
    and thev lived at the bottom of a well.</p>
    <p class="story">...</p>
    """

# 新建soup对象，解析html文档并生成文档树
soup = BeautifulSoup(html_str, 'lxml')
# 打印soup内容并格式化输出
# print(soup.prettify())


"""
从文档树中抽取对象。
分为： 1）Tag对象、2）NavigableString对象、3）BeautifulSoup对象、4) Comment对象
"""
# # 1）Tag对象：标记里及其内容都是Tag对象，用soup.标记名 就可以抽取到对应的Tag对象。
# print(soup.head)
# # 【Tag】的两个重要属性：name 和 attributes
# print(soup.name)  # soup是特殊的Tag，其名称固定为document，其他tag的name就是其标签名
# print(soup.head.name)
# soup.head.name = 'myhead'  # 还可以直接给soup.tag.name赋值来更改该soup下所有原标记的名称
# # Tag对象对其属性的获取与修改等操作方法，与字典相同。例如<p class="story">，Tag对象p 有class属性，获取其属性可以通过soup.p.get("class")或者soup.p['class']
# print(soup.p['class'])
# # 2）NavigableString对象。
# # 通过在Tag对象p 后加.string来获取p标签内的文字，获得的是NavigableString对象，可以通过unicode()方法来转换象得到Unicode字符串。
# print(soup.p.string)
# # 3）BeautifulSoup对象，是一个文档的全部内容。可以将它作为一个特殊的Tag对象。
# # 4) Comment对象，a标签的内容就是注释，通过下列方式可以获取注释：
# print(soup.a.string)


"""
遍历文档树。
Tag对象的.content属性、.child属性与树的节点内容、子节点 结构对应。
Tag对象的第一个节点应该是head，注意字符串没有.contents属性。
遍历文档树主要是为了 1）获取子节点、2）获取节点的内容、3）获取父节点、4）获取兄弟节点、3）获取前后节点
"""
# print(soup.head.contents)  # soup.head.contents打印出来的是列表
# print(len(soup.head.contents))  # 可以对其进行列表操作
# # 1）获取子节点。 .children获取直接子节点
# for child in soup.head.children:  # soup.head.children包含的是head的直接子节点
#     print(child)
# for child in soup.head.descendants:  # .descendants属性可以对Tag对象 即head 对子孙节点进行递归循环
#     print(child)
# # 2）获取节点的内容：可以利用节点的3种属性 .string, .strings, .stripped_strings
# # .string属性可以获取标记内唯一的字符串，或获取标记内的唯一标记的字符串，若标记内有多个标记则返回0
# print(soup.head.string)
# print(soup.title.string)
# print(soup.html.string)
# # .strings属性可以获取标记内多个字符串
# for s in soup.strings:
#     print(s)
# # stripped_strings属性可以获取标记内除掉空格以外的多个字符串
# for s in soup.stripped_strings:
#     print(s)
# # 3）获取父节点。
# print(soup.title)
# print(soup.title.parent)
# # 4）获取兄弟节点。 注意空白和换行也是节点
# print(soup.p.next_sibling)
# print(soup.p.previous_sibling)
# # 5）获取前后节点（不区分层次）
# print(soup.title.next_element)
# print(soup.title.previous_element)


"""
搜索文档树。
这里以重点方法find_all(name, attrs, recursive, text, **kwargs)为例，解释参数的作用：
"""
# name参数。通过指定name参数，找到符合该名字的标签
print(soup.find_all('b'))  # 查找文档中所有的<b>标签，精准匹配
for tag in soup.find_all(re.compile('^b')):  # 查找文档中所有以b开头的标签，模糊匹配
    print(tag.name)
print(soup.find_all('a', 'b'))  # 查找文档中所有的<a>标签和<b>标签，精准匹配&精准匹配
print(soup.find_all(True))  # name参数还可以为True，则返回文档中所有的标签（但不包含内容），匹配所有

# **kwargs参数。该参数提供keyword=value的方式，查找符合条件的标签
print(soup.find_all(class_='sister'))  # 这里keyword后面加了下划线，因为class是python的关键词 很特殊。

# attrs参数。和 **kwargs差不多，通过attrs={keyword:value} 的方法来查找符合条件的标签。当不支持使用**kwargs参数时，可以用attrs，例如HTML5中的data-* 属性
print(soup.find_all(attrs={"data_foo": "value"}))

# text参数。该参数帮助查找匹配了查找条件的字符串
print(soup.find_all(text="Elsie"))
print(soup.find_all(text=["Tillie", "Elsie", "Lacie"]))
print(soup.find_all(text=re.compile("Dormouse")))
# 另外，text还可与其他关键词一起协同查找包含text字符串的标签
print(soup.find_all('a', text='Elsie'))

# limit参数。限制返回结果数量。因为find_all方法默认返回所有查询结果，用limit参数可限制返回结果的数量。
print(soup.find_all(id=True, limit=2))  # id=True指的是查找文档中所有id标签，limit为2 限制了只返回前2个结果

# recursice参数。True或False，指的是返回所有子孙节点、或只返回直接子节点。
print(soup.find_all('title', recursive=False))  # 只返回直接子节点

