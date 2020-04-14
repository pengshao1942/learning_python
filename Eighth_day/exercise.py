#练习
#1、将耗时间的任务放到线程中以获得更好的用户体验：避免占用进程导致其他按钮卡死
#tkinker是图像模块

import time
import tkinter
import tkinter.messagebox
from threading import Thread


def main():

    class DownloadTaskHandler(Thread):  #驼峰命名法
        def run(self):
            time.sleep(10)
            tkinter.messagebox.showinfo('提示', '下载完成')
            #启用下载按钮
            button1.config(state=tkinter.NORMAL)

    def download():
        #禁用下载按钮
        button1.config(state=tkinter.DISABLED)
        #通过daemon参数将线程设置为守护进程(主程序退出就不在保留执行)
        #在线程中处理耗时间的下载任务
        DownloadTaskHandler(daemon=True).start()



    def show_about():
        tkinter.messagebox.showinfo('关于', '作者: 骆昊(v1.0)')

    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


if __name__ == '__main__':
    main()

#计算密集型任务：单进程和多进程耗时区别
#单进程
from time import time


def main():
    total =0
    number_list = [x for x in range(1, 100000001)]
    start = time()
    for number in number_list:
        total += number
    print(total)
    end = time()
    print('Execution time: %.3fs' % (end - start))


if __name__ == "__main__":
    main()

#多进程：分解为8个进程，不考虑切片花费的时间
from multiprocessing import Process, Queue
from random import randint
from time import time


def task_handler(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)


def main():
    processes = []
    number_list = [x for x in range(1, 100000001)]
    result_queue = Queue()
    index = 0
    # 启动8个进程将数据切片后进行运算
    for _ in range(8):
        p = Process(target=task_handler,
                    args=(number_list[index:index + 12500000], result_queue))
        index += 12500000
        processes.append(p)
        p.start()
    # 开始记录所有进程执行完成花费的时间
    # 不考虑列表创建及切片操作花费的时间
    start = time()
    for p in processes:
        p.join()
    # 合并执行结果
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('Execution time: ', (end - start), 's', sep='')


if __name__ == "__main__":
    main()