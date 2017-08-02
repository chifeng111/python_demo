# coding: utf-8
import threading
import time

class mythread(threading.Thread):
    num = 100   #静态变量的定义
    
    def __init__(self, threadname):
        threading.Thread.__init__(self, name=threadname)
        
    def run(self):
        while mythread.num>0: #静态变量的访问：类名.变量明
            lock.acquire()
            mythread.num -= 1
            time.sleep(0.002)
            print(mythread.num, self.getName())
            lock.release()



if __name__ == '__main__':
    lock = threading.RLock()
    aa = mythread("aa")
    bb = mythread("bb")
    aa.start()
    bb.start()            
        