# 开发时间：2023-03-02 10:59
# 开发人员：林坚洪
# encodeing "UTF-8"
fp = open('news.txt', encoding='UTF-8')
a = fp.read()
s = input("输入一个字符串统计频率")
print(a.count(s))
