# 开发时间：2023-04-14 22:45
# 开发人员：林坚洪
# encodeing "UTF-8"
from snownlp.seg import seg

fs = open('bili_small.txt', encoding='utf-8')
s = fs.read()


from snownlp import SnowNLP, normal
#
# kk = SnowNLP(s)
# print(kk.keywords(40))
import jieba
import jieba.analyse
from snownlp import sentiment
def handle(self, doc):  # 在 sentiment 中
    words = seg.seg(doc)  # seg 是 snownlp 的分词方法
    words = normal.filter_stop(words)  # 过滤停用词
    return words

sent = sentiment.Sentiment()
words_list = sentiment.Sentiment.handle(sent, s)


text = ' '.join(words_list)
tags = jieba.analyse.extract_tags(text, topK=20)
print(tags)
