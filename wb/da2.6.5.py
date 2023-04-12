# 开发时间：2023-02-22 10:42
# 开发人员：林坚洪
# encodeing "UTF-8"
set2 = [1, 2, 3]
set3 = set(set2)
print(set(set2))
set1 = {1, 4, 6}
set5={4,1}
print(set1, set3)
print('*'*99)
print(set3 - set1)
print(set3&set1)
print(set3^set1)
print(set3|set1)
print(set3>set1)
print(set3<set1)
print(set5<set1)