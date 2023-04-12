# 开发时间： 2022/7/21  16:48
# 开发人：林坚洪
'''
s='I am iron man,my name is lindeyi'
print(s.index('i'))
print(s.rindex('i'))
#抛异常

print(s.find('m'))
print(s.rfind('m'))
#不抛异常，返回-1


b='I am iron mAn,my naMe is lindeyi'
print(b.upper())
print(b.lower())
print(b.swapcase())
print(b.capitalize())
print(b.title())

c='I am iron man,my name is lindeyi'
#左右对齐
print(c.center(50,'*'))
print(c.ljust(40,'*'))
print(c.ljust(20,'*'))
print(c.rjust(40,'*'))
print(c.zfill(40))
print('-345793'.zfill(10))

s='I am iron man,my name is lindeyi'
print(s.split())
print(s.split(sep=','))
a='I,am iron,man,my name,is,lindeyi'
print(a.split())
print(a.split(sep=',',maxsplit=3))
print(a.rsplit(sep=',',maxsplit=3))

print('sdd'.isidentifier())
print('=ure'.isidentifier(),'\n')
print('837645'.isalnum())
print('3476hj'.isalnum(),'\n')
print('sdd'.isalpha())
print('8756'.isalpha(),'\n')
print('659'.isnumeric())
print('hjkli'.isnumeric(),'\n')
print('\n'.isspace())
print('7698'.isspace(),'\n')
print('3453'.isdecimal())
print('10010001'.isdecimal())

s = 'I am iron man,my name is lindeyi'
print(s.replace('man', 'woman'))
print(s.replace('m', 'M', 3))

listii = ['wihefef', '77345', '3874', 'odhff']
print('|'.join(listii))
print('*'.join(listii))

print('a'>'b')
print(chr(102))
print(ord('a'))
print('apple'>'apple')
print(ord('林'))
print(chr(26519))
print('apple'>'b')
# a==b 比较value值
# a is b 比较id'''

s='I am iron man,my name is lindeyi'
s1=s[:7]
s2=s[10:]
print(s1)
print(s2)
s3='!'
s4=s1+s2+s3
print(s4)
s6=s[3:20:2]
# start,end,step

print(s6)
print(s[-21:-1:1],'\n')
print(s[-1:-27:-1])
print(s[::-1])

