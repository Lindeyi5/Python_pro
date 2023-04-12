# 开发时间：2023-03-27 11:02
# 开发人员：林坚洪
# encodeing "UTF-8"
import re
m=re.findall('\w','123_#-我爱Python')#匹配数字、字母、下划线、汉字
print(m)
m=re.findall('^[a-zA-Z]\d{1,3}OK$','a25OKf',)#表示以一个字母开头，中间1-3个数字，以OK结尾的字符
print(m)#[]匹配任意一个
