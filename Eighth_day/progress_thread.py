#Python既支持多进程又支持多线程
#使用Python实现并发编程主要有3种方式：多进程、多线程、多进程+多线程

#多进程模块：multiprocessing
#子进程模块：subprocess
#操作系统模块：os
#多线程模块：_thread 该模块过于底层，多线程开发推荐使用threading模块，该模块对多线程编程提供了更好的面向对象的封装


#单进程案例：
from random import randint
from time import time, sleep


def download_task(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    download_task('Python从入门到住院.pdf')
    download_task('Peking Hot.avi')
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()


#多进程案例：
from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    p1 = Process(target=download_task, args=('Python从入门到住院.pdf', ))
    p1.start()
    p2 = Process(target=download_task, args=('Peking Hot.avi', ))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()

"""
在上面的代码中，我们通过Process类创建了进程对象，通过target参数我们传入一个函数来表示进程启动后要执行的代码，后面的args是一个元组，
它代表了传递给函数的参数。Process对象的start方法用来启动进程，而join方法表示等待进程执行结束。运行上面的代码可以明显发现两个下载
任务“同时”启动了，而且程序的执行时间将大大缩短，不再是两个任务的时间总和。
"""


#多线程案例1： 多线程下载文件
#直接使用threading模块的Thread类来创建线程
from random import randint
from threading import Thread
from time import time, sleep


def download(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    t1 = Thread(target=download, args=('Python从入门到住院.pdf',))
    t1.start()
    t2 = Thread(target=download, args=('Peking Hot.avi',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.3f秒' % (end - start))


if __name__ == '__main__':
    main()


#多线程案例2： 多线程下载文件
#通过继承Thread类的方式来创建自定义的线程类，然后再创建线程对象并启动线程
from random import randint
from threading import Thread
from time import time, sleep


class DownloadTask(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成! 耗费了%d秒' % (self._filename, time_to_download))


def main():
    start = time()
    t1 = DownloadTask('Python从入门到住院.pdf')
    t1.start()
    t2 = DownloadTask('Peking Hot.avi')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()



"""
因为多个线程可以共享进程的内存空间，因此要实现多个线程间的通信相对简单，就是设置一个全局变量，多个线程共享这个全局变量即可
如果一个资源被多个线程竞争使用，那么我们通常称之为“临界资源”，对“临界资源”的访问需要加上保护，否则资源会处于“混乱”的状态
可以通过“锁”来保护“临界资源”，只有获得“锁”的线程才能访问“临界资源”，而其他没有得到“锁”的线程只能被阻塞起来，直到获得“锁”的线程释放了“锁”，
其他线程才有机会获得“锁”，进而访问被保护的“临界资源”

"""
#案例：多个线程向同一个银行账户转载1元,这里银行账户就是"临界资源"
from time import sleep
from threading import Thread, Lock  #多线程的锁Lock


class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        #先获取锁才能执行后续的代码
        self._lock.acquire()
        try:
            #计算存款后的余额
            new_balance = self._balance + money
            #模拟受理存款业务需要0.01秒的时间
            sleep(0.01)
            #修改账户余额
            self._balance = new_balance
        finally:
            #在finally中执行释放锁的操作保证正常和异常时锁都能释放
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    #创建100个存款的线程向同一个账户中存钱
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    #等所有存款的线程都执行完毕
    for t in threads:
        t.join()
    print('账户余额为: ￥%d元' % account.balance)


if __name__ == '__main__':
    main()


"""
Python的解释器有一个“全局解释器锁”（GIL）的东西
任何线程执行前必须先获得GIL锁，然后每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行，这是一个历史遗留问题
"""
"""
多任务一旦多到一个限度，反而会使得系统性能急剧下降;因为在任务间切换也需要时间
是否采用多任务的第二个考虑是任务的类型，可以把任务分为计算密集型和I/O密集型
1、计算密集型任务：消耗大量CPU资源,要进行大量计算，如：视频的编码解码或格式转换
2、其他的涉及到网络、存储介质I/O的任务都可以视为I/O密集型任务，这类任务的特点是CPU消耗很少，
   任务的大部分时间都在等待I/O操作完成（因为I/O的速度远远低于CPU和内存的速度）。
   对于I/O密集型任务，如果启动多任务，就可以减少I/O等待时间从而让CPU高效率的运转
"""

#Python中有嵌入C/C++代码的机制

#单线程+异步I/O
#充分利用操作系统提供的异步I/O支持，就可以用单进程单线程模型来执行多任务，这种全新的模型称为事件驱动模型
#Python中，单线程+异步I/O的编程模型称为协程;有了协程的支持，就可以基于事件驱动编写高效的多任务程序
"""协程的优势：
    1、极高的执行效率；因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销
    2、不需要多线程的锁机制：因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源(临界资源)不用加锁，只需要判断状态就好了，所以执行效率比多线程高很多
"""
#要充分利用CPU的多核特性，最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能
