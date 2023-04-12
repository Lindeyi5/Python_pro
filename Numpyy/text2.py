# 开发时间：2023-03-01 10:56
# 开发人员：林坚洪
# encodeing "UTF-8"
import pandas as pd
df=pd.read_csv('titanic.csv')
#print(df.head().to_string())
#print(df.describe().to_string())
#print(df.describe(include='all').to_string())
print('-'*88)
print(df['age'])
print(df['age'].isnull())
print('-'*88)
new_df=df.dropna(subset=['age'])
print(new_df.describe().to_string())
print(new_df['age'].isnull())
print('-'*88)

x=round(df['age'].mean(),2)
print(x)
df['age'].fillna(x,inplace=True)
print(df.head().to_string())
print('-'*88)
print('\n')
data={'data':['2020/12/01','2020/11/01','20201221'],
      'age':[31,34,56]}
df=pd.DataFrame(data,index=['day1','day2','day3'])
print(df.to_string())

df['data']=pd.to_datetime(df['data'])
print(df.to_string())
print('-'*88)
#person={
#    'name':['d','da','did'],
#    'age':[33,45,12342]
#}
#df=pd.DataFrame(person)
#print(df)
#df.loc[1,'did']=49
#print(df)
#if df.loc[person,'age']>20:
#    df.drop(x,inplace=True)
#df.duplicated(())
#df.drop_duplicates(inplace=True)
