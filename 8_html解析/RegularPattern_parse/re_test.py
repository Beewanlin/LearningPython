"""
本例说明re模块中各常用的方法。（可以直接使用pattern对象调用，传参可省去第一个pattern参数。）
"""
import re

# 创建Pattern对象，编译正则表达式
pattern = re.compile(r'\d+')

"""
re.match(pattern, s[, flags]) 只有在string起始位置匹配成功的时候才有返回，如果不是开始位置匹配成功的话，match()就返回None
"""
# 需要使用result.group()打印re.match()的匹配结果
def printmatchresult(result):
    if result:
        print(result.group())
    else:
        print('匹配失败')
result1 = re.match(pattern, '192abc')
printmatchresult(result1)
result2 = re.match(pattern,'abc192')
printmatchresult(result2)
"""
re.search(pattern, s[, flags]) 与match方法相似，区别在于search是在整个字符串中查找匹配，即使一开始的位置没有匹配成功，也会继续扫描匹配。
"""
result3 = re.search(pattern, 'abc192')
printmatchresult(result3)


"""
re.split(pattern, s[, maxsplit]) 按照能够匹配的子串将string分割后返回列表。参数maxsplit指定最大分割次数。
"""
result4 = re.split(pattern, 'A1B2c3d4')
print(result4)


"""
re.findall(pattern, string[, flags]) 搜索整个string，以列表形式返回能匹配的全部子串。
"""
result5 = re.findall(pattern, 'A1B2c3d4')
print(result5)


"""
re.finditer(pattern, string[, flags]) 与findall类似，不过返回的是一个可迭代对象而不是直接返回一个列表。
"""
result6 = re.findall(pattern, 'A1B2c3d4')
for e in result6:
    print(e)


"""
re.sub(pattern, repl, string[, count]) 使用repl替换string中每一个匹配的子串后返回替换后的字符串。
repl可以是一个字符串，
repl也可以是一个可调用方法（该方法只有一个参数-match对象（包含了很多匹配信息的匹配结果）），然后返回一个用于替换的字符串
"""
s = 'i say, hello world!'
p1 = re.compile(r'(?P<word1>\w+) (?P<word2>\w+)')  # 给分组命名word1、word2，格式为 ?P<name>exp，两个分组之间有空格
# 当repl是一个字符串
result7 = re.sub(p1, r'\g<word2> \g<word1>', s)    # 这里repl是一个字符串。引用分组word1、word2，使用\g<name>引用。
print(result7)
p2 = re.compile(r'(\w+) (\w+)')  # 分组
result8 = p2.sub(r'\2 \1', s)  # 引用分组，使用编号
print(result8)
# 当repl是一个方法
def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()  # 该方法作用：将单词首字母转换为大写
print(p2.sub(func, s))  # 等同于print(re.sub(p2, func, s))

"""
re.subn(pattern, repl, string[, count]) 与re.sub相似，区别在于本方法是返回一个元组，除了替换后的字符串，还会多返回替换次数count
"""
result9 = re.subn(p1, r'\g<word2> \g<word1>', s)
print(result9)


"""
match对象的属性和方法。
属性包括：
方法包括：
group() 获得1个或多个分组截获的字符串。无参数时返回全部结果，参数为整数1、2、...表示指定第几个分组截获的字符串，0表示整个结果。
groups() 
groupdict()
start()
end()
span()
expand(template)
"""

pattern = re.compile(r'(\w+) (\w+) (?P<word>.*)')
match = pattern.match('I Love Chocolate')

print("match.string:", match.string)
print("match.re:", match.re)
print("match.pos:", match.pos)
print("match.endpos:", match.endpos)
print("match.lastindex:", match.lastindex)
print("match.lastgroup:", match.lastgroup)

print("match.group(1,2):", match.group(1, 2))
print("match.groups():", match.groups())
print("match.groupdict():", match.groupdict())
print("match.start(2):", match.start(2))
print("match.end(2):", match.end(2))
print("match.span(2):", match.span(2))
print(r"match.expand(r'\2 \1 \3'):", match.expand(r'\2 \1 \3'))
