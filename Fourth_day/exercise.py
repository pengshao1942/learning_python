#案例：奥特曼打小怪兽

from abc import ABCMeta, abstractmethod
from random import randint, randrange


class Fighter(object, metaclass=ABCMeta):  #定义父类Fighter为抽象类
    """战斗者"""

    __slots__ = ('_name', '_hp') #__solts__魔法限定对象可绑定的变量为名字和血量

    def __init__(self, name, hp): 
        """初始化方法

        :param name: 名字
        :param hp: 血量
        """
        self._name = name
        self._hp = hp

    @property  #访问器-getter
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter  #修改器-setter,因为血量是变化的
    def hp(self, hp):
        self._hp = hp if hp >=0 else 0

    @property
    def alive(self):  #是否存活
        return self._hp > 0

    @abstractmethod
    def attack(self, other):  #定义抽象方法
        """攻击
        :param other: 被攻击的对象
        """
        pass

class Altman(Fighter):  #继承Fighter类
    """奥特曼"""
    
    __slots__ = ('_name', '_hp', '_mp')  #__slots__魔法方法
    def __init__(self, name, hp, mp):   #继承父类Fighter
        """初始化方法

        :param name: 名字
        :param hp: 血量
        :param mp: 魔法量
        """
        super().__init__(name, hp)
        self._mp = mp
    
    def attack(self, other):
        other.hp -= randint(15, 25)
    
    def huge_attack(self, other):  #定义究极必杀技类
        """究极必杀技(打掉对方至少50点或四分之三的血)

        :param other: 被攻击的对象
        :return: 使用成功返回True,否则返回False
        """
        if self._mp >= 50:
            self._mp -=50
            injury = other.hp * 3 // 4  #定义究极必杀技的伤害量
            injury = injury if injury >=50 else 50 #定义究极必杀技的伤害量
            other.hp -= injury   #剩余的血量
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):  #others被攻击者对象群体
        """魔法攻击,群攻

        :param others：被攻击的群体
        :return: 使用成功返回True，否则返回False
        """
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:  #判断群体是否存活
                    temp.hp -= randint(10, 15) #魔法攻击随机打掉多少血
            return True
        else:  #否则魔法不够,使用魔法攻击失败
            return False

    def resume(self):   #定义恢复魔法值的方法
        """恢复魔法值"""
        incr_point = randint(1, 10)  #10以内随机恢复魔法值
        self._mp += incr_point
        return incr_point

    def __str__(self):  #定义角色出场时的信息显示方法,__str__魔法方法,打印实例化对象
        return '~~~%s奥特曼~~~\n' % self._name + \
            '生命值：%d\n' % self._hp + \
            '魔法值：%d\n' % self._mp


class Monster(Fighter):
    """怪兽类"""

    __slots__ = ('_name', '_hp')  #__slots__魔法限定怪兽类只可绑定2个属性

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '~~~%s怪兽~~~\n' % self._name + \
            '生命值: %d\n' % self._hp


def is_any_alive(monsters):
        """判断有没有小怪兽是活着的"""
        for monster in monsters:
            if monster.alive > 0:
                return True
        return False

def select_alive_one(monsters):
        """选中一只活着的小怪兽"""
        monsters_len = len(monsters)
        while True:
            index = randrange(monsters_len)
            monster = monsters[index]
            if monster.alive > 0:
                return monster

def display_info(altman, monsters):
        """显示奥特曼和小怪兽的信息"""
        print(altman)
        for monster in monsters:
            print(monster, end='')

def main():
    u = Altman('李东', 1000, 120)
    m1 = Monster('狄仁杰', 250)
    m2 = Monster('白元芳', 500)
    m3 = Monster('王大锤', 750)
    ms = [m1, m2, m3]  #怪兽群,列表
    fight_round = 1  #定义回合初始值为1
    while u.alive and is_any_alive(ms):
        print('=======第%02d回合======' % fight_round)
        m = select_alive_one(ms) #选中一只小怪兽
        skill = randint(1, 10) #通过随机数选择使用哪种技能
        if skill <=6: #60%的概率使用普通攻击
            print('%s使用普通攻击打了%s.' % (u.name, m.name))
            u.attack(m)
            print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        elif skill <=9: #30%的概率使用魔法攻击(可能因魔法值不足而失败)
            if u.magic_attack(ms):
                print('%s使用魔法攻击.' % u.name)
            else:
                print('%s使用魔法失败.' % u.name)
        else:  # 10%的概率使用究极必杀技(如果魔法值不足则使用普通攻击)
            if u.huge_attack(m):
                print('%s使用究极必杀技虐了%s.' % (u.name, m.name))
            else:
                print('%s使用普通攻击打了%s.' % (u.name, m.name))
                print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        if m.alive > 0: # 如果选中的小怪兽没有死就回击奥特曼
            print('%s回击了%s.' % (m.name, u.name))
            m.attack(u)
        display_info(u, ms) # 每个回合结束后显示奥特曼和小怪兽的信息
        fight_round +=1 
    print('\n========战斗结束!========\n')
    if u.alive > 0:
        print('%s奥特曼胜利!' % u.name)
    else:
        print('小怪兽胜利!')

if __name__ == "__main__":
    main()




#案例：扑克游戏
import random

class Card(object):
    """一张牌"""

    def __init__(self, suite, face):
        self._suite = suite
        self._face = face

    @property
    def face(self):
        return self._face

    @property
    def suite(self):
        return self._suite

    def __str__(self):
        if self._face == 1:
            face_str = 'A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        return '%s%s' % (self._suite, face_str)
    
    def __repr__(self):
        return self.__str__()


class Poker(object):
    """一副牌"""

    def __init__(self):
        self._cards = [Card(suite, face) 
                       for suite in '♠♥♣♦'
                       for face in range(1, 14)]  #列表的生成式语法生成牌的列表
        self._current = 0

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        """洗牌(随机乱序)"""
        self._current = 0
        random.shuffle(self._cards)

    @property
    def next(self):
        """发牌"""
        card = self._cards[self._current]
        self._current += 1
        return card

    @property
    def has_next(self):
        """还有没有牌"""
        return self._current < len(self._cards)


class Player(object):
    """玩家"""

    def __init__(self, name):
        self._name = name
        self._cards_on_hand = []

    @property
    def name(self):
        return self._name

    @property
    def cards_on_hand(self):
        return self._cards_on_hand

    def get(self, card):
        """摸牌"""
        self._cards_on_hand.append(card)

    def arrange(self, card_key):
        """玩家整理手上的牌"""
        self._cards_on_hand.sort(key=card_key)

def get_key(card):
    return (card.suite, card.face)

def main():
    p = Poker()
    p.shuffle()
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    for _ in range(13):
        for player in players:
            player.get(p.next)
    for player in players:
        print(player.name + ':', end=' ')
        player.arrange(get_key)
        print(player._cards_on_hand)


if __name__ == "__main__":
    main()



#案例：工资结算系统：
"""
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""

from abc import ABCMeta, abstractmethod


class Employee(object, metaclass=ABCMeta):  #雇员，元类
    """员工"""

    def __init__(self, name):
        """
        初始化方法

        :param name: 姓名
        """
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod  #抽象方法关键字
    def get_salary(self):  #定义月薪的抽象方法
        """
        获得月薪

        :return: 月薪
        """
        pass  


class Manager(Employee):
    """部门经理"""

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """程序员"""

    def __init__(self, name, working_hour=0):  #初始化方法
        super().__init__(name)
        self._working_hour = working_hour

    @property
    def working_hour(self):
        return self._working_hour

    @working_hour.setter
    def working_hour(self, working_hour):
        self._working_hour = working_hour if working_hour > 0 else 0

    def get_salary(self):  #子类使用抽象方法,再自定义
        return 150.0 * self._working_hour


class Salesman(Employee):
    """销售员"""

    def __init__(self, name, sales=0):
        super().__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def get_salary(self):
        return 1200.0 + self._sales * 0.05


def main():
    emps = [
        Manager('刘备'), Programmer('诸葛亮'),
        Manager('曹操'), Salesman('荀彧'),
        Salesman('吕布'), Programmer('张辽'),
        Programmer('赵云')
    ]
    for emp in emps:
        if isinstance(emp, Programmer): 
            emp.working_hour = int(input('请输入%s本月工作时间: ' % emp.name))  #使用working_hour方法来定义工作时间变量
        elif isinstance(emp, Salesman):
            emp.sales = float(input('请输入%s本月销售额: ' % emp.name)) #销售额可能不是整数,所以用float
        # 同样是接收get_salary这个消息但是不同的员工表现出了不同的行为(多态)
        print('%s本月工资为: ￥%s元' %
              (emp.name, emp.get_salary()))  


if __name__ == '__main__':
    main()





