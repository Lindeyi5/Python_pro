# 开发时间：2023-04-07 11:28
# 开发人员：林坚洪
# encodeing "UTF-8"
import pandas as pd
import nltk

sentence = "What you say is very funny. And he is not a very nice person."
tokens = nltk.word_tokenize(sentence)
train = pd.read_csv("movieReviews.tsv", header=0, delimiter='\t', quoting=3)
fdist1 = nltk.FreqDist(tokens)
print(fdist1)
print()
# print(fdist1.)
print(fdist1.items())
for key, val in fdist1.items():
    print(key, val)
