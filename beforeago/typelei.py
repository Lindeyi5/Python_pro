# 开发时间： 2022/7/23  18:56
# 开发人：林坚洪
'''
name='法外狂徒张三'
age=99
print('老子是%s,芳龄%d岁' % (name,age))
print('老子是{0},芳龄{1}岁'.format(name,age))
print(f'老子是{name},芳龄{age}岁')

print('{0}'.format(3.14159))
print('{0:.3}'.format(3.14159))
print('{0:.3f}'.format(3.14159))
print('{0:10.3}'.format(3.14159))
print('----------')
print('%10d' % 3.566)
print('%3f' % 3.566)
print('%.3f' % 3.566)
print('%10.3f' % 3.566)'''

s='言念君子，温其如玉。'
print(s.encode(encoding='GBK'))
print(s.encode(encoding='UTF-8'))
bi=s.encode(encoding='GBK')
bi2=s.encode(encoding='UTF-8')
print(bi.decode(encoding='GBK'))
print(bi2.decode(encoding='UTF-8'))
