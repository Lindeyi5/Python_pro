# 开发时间：2023-03-02 11:27
# 开发人员：林坚洪
# encodeing "UTF-8"
class Person:
    role = 'person'

    def __init__(self, name, sex, age, battle):
        self.name = name
        self.sex = sex
        self.age = age
        self.battle = battle

    def print_message(self):
        print('%s,%s,%s,战斗力为%s' % (self.name, self.sex, self.age, self.battle))

    def sneak_attack(self, person):
        self.battle += 200
        person.battle -= 200

    def self_practice(self):
        self.battle += 100

    def surrender(self, person):
        person.battle = person.battle + self.battle
        self.battle = 0


cjj = Person('仓井井', '女', '18', 1000)
dnm = Person('东尼木', '男', '20', 1800)
mdd = Person('美多多', '女', '19', 2500)

######################  开始游戏  #####################
print("-" * 20, '开始游戏', "-" * 20)
js = input('请输入参战人物')
if js == '仓井井':
    js = cjj
elif js == '东尼木':
    js = dnm
elif js == '美多多':
    js = mdd

print('人物状态：姓名%s,性别:%s,年龄：%s,当前战斗力：%s' % (js.name, js.sex, js.age, js.battle))
x = True
while x:
    xd = input('请选择你的行动? \na.偷袭  b.修炼  c.投降、\n')
    if xd == 'a':
        tx = input('请输入偷袭对象')
        if tx == '苍井井':
            dx = cjj
        elif tx == '东尼木':
            dx = dnm
        elif tx == '美多多':
            dx = mdd
        js.sneak_attack(dx)
        print('偷袭成功,当前人物状态：姓名%s,性别:%s,年龄：%s,当前战斗力：%s' % (js.name, js.sex, js.age, js.battle), '\n'
                                                                                                                   '偷袭对象人物状态：姓名%s,性别:%s,年龄：%s,当前战斗力：%s' % (
              dx.name, dx.sex, dx.age, dx.battle))
    if xd == 'b':
        js.self_practice()
        print('修炼成功')
        print('人物状态：姓名%s,性别:%s,年龄：%s,当前战斗力：%s' % (js.name, js.sex, js.age, js.battle))
    if xd == 'c':
        txg = input('请输入投降对象')
        if txg == '苍井井':
            dx = cjj
        elif txg == '东尼木':
            dx = dnm
        elif txg == '美多多':
            dx = mdd
        js.surrender(dx)
        print('您已投降，游戏结束\n'
              '敌人状态：姓名%s,性别:%s,年龄：%s,当前战斗力：%s' % (dx.name, dx.sex, dx.age, dx.battle))
        break
    sf = input('是否继续游戏?  1.是  2.否 ')
    if sf == '2':
        x = False
print('-' * 15, '游戏结束', '-' * 15)

