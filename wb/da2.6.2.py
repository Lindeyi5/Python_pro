# 开发时间：2023-02-16 10:51
# 开发人员：林坚洪
# encodeing "UTF-8"
str1='learn Python'
print(str1,str1[0],str1[-1])
print(str1[:9])
print(str1[4:])

print("E:\note\Python.doc")

print(r'E:\note\Python.doc')

str4='String\t'
str5='is powerful'
str4=str4+str5
print(str4)

format_str='There are 2 apples on the desk.'
format_str1='There are %d apples %s the desk.'
a_t=(2,'on')
print(format_str1 % a_t)
print('There are {0} apples {1} the desk.'.format(3,'on'))
print('There are %d apples %s the desk.'%(5,'on'))

str6="Zootopia"
print(str6.find('to'))
print(str6.split('t'))
str7="Z o o t o p i a"
print(str7.split())

print(' '.join(str7.split()))
print('-'*70)
str8='54321'
print('>'.join(str8))

st8='"Yes",I answered.'
print(st8.split(','))

str9='A apple'
print(str9.count('A'))
str9=str9.lower()
print(str9.count('a'))

print('--'*70)

str10='123456'
print(str10.isalnum())