# 开发时间：2023-04-12 11:28
# 开发人员：林坚洪
# encodeing "UTF-8"
from snownlp import SnowNLP
s=SnowNLP('这个东西很赞')
#分词
print(s.words)
print(list(s.tags)) #词性标注
# 结果显示：[('这个', 'r'), ('东西', 'n'), ('很', 'd'), ('赞', 'Vg')]。
print(s.sentiments) #情感分析