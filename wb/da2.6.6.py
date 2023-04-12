# 开发时间：2023-02-22 9:59
# 开发人员：林坚洪
# encodeing "UTF-8"
###fp=open('news.txt',encoding='UTF-8')
###a=fp.read()
###fp.close()
###print(a)
###print(a.count('China'))

import pandas as pd
pd.set_option('display.unicode.ambiguous_as_wide',True)
pd.set_option('display.unicode.east_asian_width',True)
x=pd.read_excel('mtpl.xls','Sheet1')
print(x.head())


print('-'*80)
import pandas as pd
pd.set_option('display.max_colwidth',100)
train=pd.read_csv('doubanpd.csv',encoding='gbk')
print(train['reviews'].head(8))