# 开发时间：2023-04-03 9:59
# 开发人员：林坚洪
# encodeing "UTF-8"
import re

import nltk
sen="i love python"
token=nltk.word_tokenize(sen)
print(token)
# nltk.download()
sentence = "What you say is very funny. And he is not a very nice person."
sentence11=re.sub("[^a-zA-Z]"," ",sentence)
print(sentence11)
tokens = nltk.word_tokenize(sentence11)
print(tokens)
tagged=nltk.pos_tag(tokens)
print(tagged)

fdist1 = nltk.FreqDist(tokens)
print()
print(fdist1.items())
print()
list1=[]
list2=[]
for key, val in fdist1.items():
    list1.append(key)
    list2.append(val)
    print(key, val)

print(list1,list2)