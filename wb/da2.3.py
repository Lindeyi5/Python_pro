# 开发时间：2023-02-15 11:35
# 开发人员：林坚洪
# encodeing "UTF-8"
def s(x):
    if x==1:
        return "yes"
    else:
        return "no"
print(s(1))
print(s(2))
print(s(33))
print('\n')

ss=lambda x:"yes" if x==1 else "no"
print(s(1))
print(s(44))