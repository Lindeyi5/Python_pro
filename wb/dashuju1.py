# 开发时间：2023-02-15 10:26
# 开发人员：林坚洪
import jieba
s=jieba.cut("我是一名江苏大学的大学生",cut_all=True)
print(u"全模式:"+"/".join(s))