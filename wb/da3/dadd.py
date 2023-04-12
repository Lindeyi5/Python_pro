# 开发时间：2023-03-08 10:54
# 开发人员：林坚洪
# encodeing "UTF-8"
import pandas as pd
import matplotlib.pyplot as plt
one=pd.read_csv('data.csv')
s_date=pd.DataFrame(one,columns=['a','b','c','d','e'])
print(s_date)
x=[0,1,2,3,4]
#print(s_date,['a','b','c','d','e'])
a=s_date['a']
b=s_date['b']
c=s_date['c']
d=s_date['d']
e=s_date['e']

plt.show()