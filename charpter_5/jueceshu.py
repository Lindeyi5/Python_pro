# 开发时间：2023-04-24 11:33
# 开发人员：林坚洪
# encodeing "UTF-8"
# 数据列分别代表 age,salary,isStudent,credit,isBuy
dataSet = [[1, 3, 0, 1, 'no'],
           [1, 3, 0, 2, 'no'],
           [2, 3, 0, 1, 'yes'],
           [3, 2, 0, 1, 'yes'],
           [3, 1, 1, 1, 'yes'],
           [3, 1, 1, 2, 'no'],
           [2, 1, 1, 2, 'yes'],
           [1, 2, 0, 1, 'no'],
           [1, 1, 1, 1, 'yes'],
           [3, 2, 1, 1, 'yes'],
           [1, 2, 1, 2, 'yes'],
           [2, 2, 0, 2, 'yes'],
           [2, 3, 0, 1, 'yes'],
           [3, 2, 0, 2, 'no']]
FeatureSet = []
Label = []
for i in dataSet:
    FeatureSet.append(i[:-1])
    Label.append(i[-1])
print(FeatureSet)
print(Label)
