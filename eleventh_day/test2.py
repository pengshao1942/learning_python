#控制台超时购物系统
repository = dict()
shop_list = []

def init_repository():
    goods1 = ('10001', 'Python讲义', 88.0)
    goods2 = ('10002', 'Java讲义', 69.0)
    goods3 = ('10003', 'Ruby讲义', 59.0)
    goods4 = ('10004', 'Swift讲义', 109.0)
    goods5 = ('10005', 'Android讲义', 108.0)
    goods6 = ('10006', 'ios讲义', 77.0)
    repository[goods1[0]] = goods1
    repository[goods2[0]] = goods2
    repository[goods3[0]] = goods3
    repository[goods4[0]] = goods4
    repository[goods5[0]] = goods5
    repository[goods6[0]] = goods6

def show_goods():
    print("欢迎光临!")
    print("商品清单如下：")
    print("%13s%40s%10s" % ("条码", "商品名称", "单价"))
    for goods in repository.values():
        print("%15s%40s%12s" % goods)

def show_list():
    print("=" * 100)
    if not shop_list:
        print("还未购买商品")
    else:
        title = "%-5s|%15s|%40s|%10s|%4s|%10s" % \
            ("ID", "条码", "商品名称", "单价", "数量", "小计")
        print(title)
        print("-" * 100)
        sum = 0
        for i, item in enumerate(shop_list):
            id = i + 1
            code = item[0]
            name = repository[code][1]
            price = repository[code][2]
            number = item[1]
            amount = price * number
            sum = sum + amount
            line = "%-5s|%17s|%40s|%12s|%6s|%12s" % \
            (id, code, name, price, number, amount)
            print( line )
        print("-" * 100)
        print("                         总计：", sum)
    print("=" * 100)

def add():
    code = input("请输入商品的条码：\n")
    if code not in repository:
        print("条码错误，请重新输入：")
        return
    #goods = repository[code]
    number = input("请输入购买数量：\n")
    shop_list.append([code, int(number)])


def edit():
    id = input("请输入要修改的购物明细项的ID：\n")
    index = int(id) - 1
    item = shop_list[index]
    number = input("请输入新的购买数量: \n")
    item[1] = int(number)

def delete():
    id = input("请输入要删除的购物明细项的ID： ")
    index = int(id) - 1
    del shop_list[index]

def payment():
    show_list()
    print('\n' * 3)
    print("欢迎下次光临")
    import os
    os._exit(0)

cmd_dict = {'a':add, 'e':edit, 'd':delete, 'p':payment, 's':show_goods}

def show_command():
    cmd = input("请输入操作指令： \n" + 
        "   添加(a) 修改(e) 删除(d) 结算(p) 超市商品(s)\n")
    if  cmd not in cmd_dict:
        print("不要玩，好不好!")
    else:
        cmd_dict[cmd]()

init_repository()
show_goods()
while True:
    show_list
    show_command()
