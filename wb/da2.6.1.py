# 开发时间：2023-02-16 10:51
# 开发人员：林坚洪
# encodeing "UTF-8"
List1=['Python',5,0.2]
print(List1[0])
print(List1[0:2])

print(List1[0:-1])
print(List1[-1])

List2=['T','Love','Python']
print(List2[1],List2[-1])
print(List2[:],List2[0:2])

List1.append(3.1)
print(List1)
List1.insert(1,'really')
print(List1)
List1.remove('Python')
print(List1)

print(List1.index(5),List2.count(5))

List2.extend(List1)
print(List2)
List2.reverse()
print(List2)
List3=[1,3,2,5,6,4]
List3.sort()
print(List3)
List3.sort(reverse=False)
print(List3)
List3.sort(reverse=True)
print(List3)