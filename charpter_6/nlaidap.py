# 开发时间：2023-04-12 10:59
# 开发人员：林坚洪
# encodeing "UTF-8"
from snownlp import SnowNLP
s=SnowNLP('这个东西很赞')
#分词
print(s.words)
print(list(s.tags))