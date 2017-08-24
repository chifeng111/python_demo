import threading
import time


def demo1():
    lock = threading.RLock()
    t1 = []
    for i in range(10):
        t = mythread(str(i))
        t1.append(t)

    x = 0
    for i in t1:
        i.start()


class mythread(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name=threadname)

    def run(self):
        global x
        lock.acquire()
        for i in range(3):
            x = x + 1

        time.sleep(1)
        print(self.name, x)
        lock.release()


def myfun():
    global x
    for i in range(3):
        x += 1
    time.sleep(1)
    print(x)


if __name__ == '__main__':
    #     demo1()
    x = 0
    threads = []
    for i in range(10):
        t = threading.Thread(target=myfun, args=())
        threads.append(t)
    for i in threads:
        i.start()
