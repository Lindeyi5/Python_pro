# 开发时间：2023-03-30 22:02
# 开发人员：林坚洪
# encodeing "UTF-8"
import re

my_str = r'C:\number'

# print(my_str)
my_str2 = '梦想橡皮擦 good good'
pattern = r'橡皮擦'
ret = re.search(pattern, my_str2)
a = re.match('梦想', my_str2)
b=a.span()
print(ret, '\n',a)
print(b)
print(re.match('........',my_str2))
print(re.match('[梦]',my_str2))
print(re.match('.*',my_str2))
print('\n')
print(re.match('.+',my_str2))
print(re.match('o？',my_str2))
# import re
a = """aaatestaa
aaaa123"""
print(re.findall(r'test.*123',a))
print(re.findall(r'test.*123',a,re.S))
print('---------------------')
print(re.sub(r'test','a',a))
print(re.sub(r'\n',' ',a))