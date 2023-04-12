# 开发时间：2023-03-01 10:01
# 开发人员：林坚洪
# encodeing "UTF-8"
import pandas as pd
import numpy as np

s = pd.Series([1, 2, 3, np.nan, 5, 6])
print(s)

print(s[0:3])

s = pd.Series([4, 'dadad', 523, 'wnicc', 23], index=[1, 2, 3, 'e', 't'])
print(s)

print(s['t'])

s = {"tom": 88, "sak": 87, "mary": 77, "car": None}
a = pd.Series(s)
print(a)

aa = pd.Series(s, index=['sak', 'mary', 'tom'])
print(aa)

print(aa['tom'])
print(aa[['tom', 'sak']])
print(aa['sak':'mary'])

num = pd.Series(np.random.random(5))
print(num)

print('-' * 70)
s = {"Xary": 67, "tom": 88, "sak": 87, "mary": 77, "car": None}
a = pd.Series(s)
print(a)

print('-' * 70)
data = {'id': ['Jack', 'Sarah', 'Mike'],
        'age': [33, 41, 27],
        'cash': [10.35, 23, 37]}
print(data)
df = pd.DataFrame(data)
print(df.sort_index(axis=1, ascending=True))

df['rich'] = df['cash'] > 20
print(df)

df2 = pd.DataFrame(data, columns=['id', 'cash', 'age'])
print(df2)

print(df2['id'])

print(df2.iloc[:, 0:2])

ind = ['w', 't', 's']
df3 = pd.DataFrame(data, index=ind)
print(df3)

print(df3.iloc[1:-1])
print(df3.iloc[0:, :-1])

print(df3.loc['w':'s', ['cash']])
