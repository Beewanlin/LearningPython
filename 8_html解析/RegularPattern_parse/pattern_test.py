import re

s = 'ab_cd100ef1 gh90'
# 正向零宽先行断言
RE_WORD1 = '[a-z]{1,}(?=\d+)'  # 目标字符按[a-z]{1,}匹配，其紧邻的右边必须要有\d+
RE_WORD2 = '\w+(?=\d+)'  # 目标字符按\w+匹配，其紧邻的右边必须要有\d+
RE_WORD3 = '\w+(?=\d{2})'  # 目标字符按\w+匹配，其紧邻的右边必须要有\d{2}
RE_WORD4 = '\w+?(?=\d+)'  # 目标字符按\w+的懒惰模式匹配，其紧邻的右边必须要有\d{2}
# 负向零宽先行断言
RE_WORD5 = '[a-z]{1,}(?!\d+)'  # 目标字符按[a-z]{1,}匹配，其紧邻的右边不能有\d+
RE_WORD6 = '\w+(?!\d+)'  # 目标字符按\w+匹配，其紧邻的右边不能有\d+
RE_WORD7 = '\w+?(?!\d+)'  # 目标字符按\w+的懒惰模式匹配，其紧邻的右边不能有\d+
# 正向零宽后发断言
RE_WORD8 = '(?<=\d{3}).+'  # 目标字符按.+ 匹配，其紧邻的左边必须是\d{3}
# 负向零宽后发断言
RE_WORD9 = '(?<!\d{3})[a-z]+'  # 目标字符按[a-z]+ 匹配，其紧邻的左边不能是\d{3}
"""
注意，在使用后发断言时，自定义的断言必须有固定的宽度，比如上例的\d{3}。
如果将上例中的\d{3}改为\d{2,}报如下错误： error: look-behind requires fixed-width pattern
"""
res1 = re.findall(RE_WORD1, s)  # 结果是 ['cd', 'ef', 'gh']
res2 = re.findall(RE_WORD2, s)  # 结果是 ['ab_cd100ef', 'gh9']
res3 = re.findall(RE_WORD3, s)  # 结果是 ['ab_cd1', 'gh']
res4 = re.findall(RE_WORD4, s)  # 结果是 ['ab_cd', '1', '0', '0ef', 'gh', '9']
res5 = re.findall(RE_WORD5, s)  # 结果是 ['ab', 'c', 'e', 'g']
res6 = re.findall(RE_WORD6, s)  # 结果是 ['ab_cd100ef1', 'gh90']
res7 = re.findall(RE_WORD7, s)  # 结果是 ['a', 'b', '_', 'c', 'd100', 'e', 'f1', 'g', 'h90']
res8 = re.findall(RE_WORD8, s)  # 结果是 ['ef1 gh90']
res9 = re.findall(RE_WORD9, s)  # 结果是 ['f', 'gh', 'cd', 'ab']
print(res1)
print(res2)
print(res3)
print(res4)
print(res5)
print(res6)
print(res7)
print(res8)
print(res9)
