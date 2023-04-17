# 开发时间：2023-04-17 10:03
# 开发人员：林坚洪
# encodeing "UTF-8"
import re

# pattern = '\d+(.*)'  # 模式：\d 匹配数字,+表示 1 或多个,()代表组,.代表任意字符,*表示 0 或多个
# text = '12334444fffff'  # 文本
# title_text = re.match(pattern, text)
# print(title_text)
# print(title_text.group(0))
# print(title_text.group(1))
#
#
# line = 'ujs_zdh@163.com'
# line2 = ['ujs_zdh@163.com','ajdioanwdkda.adsd']
# pattern = '^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.[a-z]+'
# res_match = re.search(pattern, line)
# print(res_match)

# pattern = r'.+[^123]+'
# line = '1s2342164oifhe'
# res_match = re.search(pattern, line)
# print(res_match)
#
#
# pattern = '[^123]+'
# line = '12356kkssk'
# res_match = re.search(pattern, line)
# print(res_match)
#
# pattern = r'h.{2,3}h'
# tresd = 'hadah823udshashaksmd92lshdjhaisdkow'
# akddw = re.findall(pattern, tresd)
# print(akddw)
# print(' '.join(akddw))
#
# # pattern = r'4+[123]+.+[123]+'
# # line = '4123w13232164oifhe'
# # res_match = re.match(pattern, line)
# # print(res_match.group(0))
#
#
# pattern = '[a-zA-Z-]+'
# line = 'I want to eat fengmi da-chang.'
# res_match = re.findall(pattern, line)
# print(res_match)

#
# pattern = '[^a-zA-Z-]+'
# line = 'I want to123 eat%#fengmi da-chang.'
# res_match = re.findall(pattern, line)
# print(res_match)
#
# # res_match = re.finditer(pattern, line)
# # for item in res_match:
# #     print(item.group(0))
#
# pattern = '[a-zA-Z-]+'
# pat = re.compile(pattern)
# print(pat)
# lines = ['I want to ',
#          'we want to ',
#          'yu want to ',
#          'Idd want to ']
# for line in lines:
#     res_match = pat.search(line)
#     print(res_match)
#
# pattern = '[a-zA-Z-]+'
# pat = re.compile(pattern)
# print(pat)
# lines = ['I want to ',
#          'we want to ',
#          'yu want to ',
#          'Idd want to ']
# for line in lines:
#     res_match = re.search(pattern,line)
#     print(res_match.group(0))


# pattern = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
# pattern1 = '(^((2[0-4]\d.)|(25[0-5].)|(1\d{2}.)|(\d{1,2}.))((2[0-5]{2}.)|(1\d{2}.)|(\d{1,2}.){2})((1\d{2})|(2[0-5]{2})|(\d{1,2})))'
# line = '1.32.42.231'
# res_match = re.findall(pattern1, line)
# print(res_match)


a = re.search(r"(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])", "202.5.69.199")
print(a)


a = re.search(r"(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])", "202.5.69.199")
print(a)
