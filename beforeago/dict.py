# 开发时间： 2022/7/19  10:06
# 开发人：林坚洪
'''scores={'张三':88,'张lisa':8438}
print(scores)
print(type(scores))

stud=dict(name='jjj',age=80)
print(stud)

print(scores['张三'])
print(scores.get('张lisa','呜呜呜我找不到'))
print(scores.get('张lia','呜呜呜我找不到'))

scores={'张三':88,'张lisa':8438}

print('张三' in scores)
print('张三' not in scores)
scores['张三']=267
print(scores)
del scores['张三']
print(scores)
scores.clear()
print(scores)
kk=scores.keys()
vv=scores.values()
kkvv=scores.items()
print(kk,vv,kkvv)
print(list(kk))
print(list(kkvv))

for items in scores:
    print(items,scores.get(items))'''

name=['fmif','sndfiwo','hfduwisf','nffci']
price=[345,453,234,344]
d={name.upper():price for name,price in zip(name,price)}
print(d)