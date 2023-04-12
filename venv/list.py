# 开发时间： 2022/7/17  15:12
# 开发人：林坚洪
'''
list3=['11','hello','jjjjj']
print(list3)
list2=list(['11','hello','jjjjj'])
print(list2)
list3=['11','hello','jjjjj']
print(list3)

list2=list(['11','hello','jjjjj'])
print(list2)
print(list2[0])
print(list2.index('11',0,2))
liyy=list2[1:2:1]
print(id(list2),id(liyy),liyy)

list=[1,2,3,4,5,6,7,8,9]

print(list)
print(list[1::])
print(list[2::])
print(list[:2:])
print(list[::3])
print('--------负号-----------')
print(list[1::-1])
print(list[2::-1])
print(list[:2:-1])
print(list[::-3])
print(10 in list)
for item in list:
    print(list)
    print('--------打印item------')
    print(item)

list.append('njs')
list3=['11','hello','jjjjj']
print(list)
list.extend(list3)
print(list)
list.insert(1,898)
print(list)
list[2:]=list3
print(list)

list=[1,2,3,4,5,6,7,8,9]
print(list)
list.pop()
print(list)
list.pop(2)
print(list)
list.remove(7)
print(list)
print('-------删除就是用另一个列表进行替换----------')
list2=list[2:5]
print(list2)
list[3:5]=[]
print(list)
print()
list.clear()
print(list)
del list2
print(list2)

list2=[1,2,3,4,5,6,7,8,9]
list2[3]=789
list2[6]=78
print(list2)
list2.sort(reverse=True)
print(list2)
list2.sort(reverse=False)
print(list2)
print('----------')
lisoo=sorted(list2,reverse=True)
lisoo1=sorted(list2)
lisoo2=sorted(list2,reverse=False)
print(lisoo,lisoo1,lisoo2)'''

lis1=[i*i for i in range(1,10)]
print(lis1)
