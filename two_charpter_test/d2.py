# 开发时间：2023-03-02 10:31
# 开发人员：林坚洪
# encodeing "UTF-8"
list1 = [2, 5, 8, 12, 35, 56, 9, 4, 12, 55]
index = 0
l2 = []
l3 = []
while index < len(list1):
    if list1[index] % 2 == 0:
        l2.append(list1[index])
    else:
        l3.append(list1[index])
    index += 1
print(l2, l3)

