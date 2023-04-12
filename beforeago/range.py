# 开发时间： 2022/7/15  8:41
# 开发人：林坚洪
'''r = range(1, 100, 3)
print(r)
print(list(r))

a = 0
s = 0
while a <= 4:
    s += a
    a += 1
print('和为'+str(s))

a = 0
s = 0
while a <= 100:
    if not bool(a%2):
       s += a
    a += 1
print('和为'+str(s))

for i in '人生苦短，及时行乐':
    print(i)

for _ in range(5):
    print('ddd')

for i in range(100, 1000):
    ge = i % 10
    shi = i // 10 % 10
    bai = i // 100
    if ge ** 3 + shi ** 3 + bai ** 3 == i:
        print(i)

for i in range(3):
    i = input('请输入密码')
    password = '6666'
    if i == password:
        print('密码正确')
        break
    else:
        print('密码不正确')

for _ in range(3):
    _ = '444'
    print(_)

k = 1
for i in range(1, 10):
    for j in range(k):
        print(i, '*', k, '=', i * k, end='\t')
    print()
    k += 1

for i in range(0, 9):
    for j in range(i+1):
        print(i+1, '*', j+1, '=', (i+1) * (j+1), end='\t')
    print()'''

for i in range(9):
    for j in range(9):
        if j%2==0:
            continue
        print('*')
    print()
