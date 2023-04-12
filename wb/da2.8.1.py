# 开发时间：2023-02-26 15:41
# 开发人员：林坚洪
# encodeing "UTF-8"
num=1
print(id(num))
num=2
print(id(num))
print('-' * 88)

def add(list):
    list.append(33)
list1=[1,2]
print(id(list1))
add(list1)
print(list1)
print(id(list1))
print('-' * 88)

list3=[1,2,3,[2,3,4,'a','b']]
list4=list3
print(list4,list3,end='\n')
print(id(list4),id(list3))
print('-' * 88)

import copy
list5=copy.copy(list3)
list6=copy.deepcopy(list3)
##list5=list3[3].append('d')
##list6=list3[3].append('f')
list3.append(3)
list3[3].append('f')
print(list5)
print(list6)

def xx():
    x=2
x=1
xx()
print(x)

def xx():
    global x
    x = 2
x=1
xx()
print(x)

