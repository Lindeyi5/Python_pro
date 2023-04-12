# 开发时间： 2022/7/21  11:13
# 开发人：林坚洪

'''集合set'''
'''s={'dd',32422,'hjhj','明天会更好'}
print(s)
s2={'dd',33,33,22,33,22,33,32422,'hjhj','明天会更好'}
print(s2,type(s2))
s3=set([4,6,3,45,6,23])
s5=set('hdhjdbdd')
s4=set(range(8))
print(s3,s4,s5)
d1={}
d2=()
d3=[]
d4=set()
print(type(d1))
print(type(d2))
print(type(d3))
print(type(d4))

s2={'dd',33,33,22,33,22,33,32422,'hjhj','明天会更好'}
s2.add(3478)
print(s2)
s2.update({23478,'hf',389,609})
s2.update([23478,'hf',389,609])
s2.update((23478,'hf',389,609))
print(s2)
s2.remove(33)
print(2)
s2.discard()
s2.pop()
s2.clear()


s={1,2,3,4,5}
s2={2,5,4,1,3}
s3={1,2,3}
s4={2,1}
s5={4,5,6,7}
print(s==s2)
print(s3.issuperset(s))
print(s3.isdisjoint(s))
print(s3.issubset(s))

print(s & s5)
print(s.intersection(s5))

print(s | s5)
print(s.union(s5))

print(s-s5)
print(s.difference(s5))

print(s ^ s5)
print(s.symmetric_difference(s5))'''

s=[i*i for i in range(10)]
ss={i*i for i in range(10)}
print(s)
print(ss)
