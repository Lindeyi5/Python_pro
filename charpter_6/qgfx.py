# 开发时间：2023-04-14 22:45
# 开发人员：林坚洪
# encodeing "UTF-8"
fs=open('bili.txt',encoding='utf-8')
s=fs.read()
from snownlp import SnowNLP
kk=SnowNLP(s)
print(kk.keywords(40))