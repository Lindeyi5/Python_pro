# 开发时间：2023-02-22 10:42
# 开发人员：林坚洪
# encodeing "UTF-8"
x = {10: 'c', 20: 'd'}
print(x)
print(x[20])
x[44] = 'f'
print(x[44])
print(x)

tm = {'a': 'an', 'ap': 'apple'}
print(tm['ap'])
word = 'I buy {a} {ap} for you'
tword = word.format(**tm)
print(tword)
