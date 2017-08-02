# coding: utf-8

import threading
import time
import os

num = 100
def a():
    global num 
    while num:
        num -= 1
        time.sleep(0.01)
        print(num)
    
aa = threading.Thread(target=a, name='aa') 
bb = threading.Thread(target=a, name='bb') 

aa.start()
bb.start()
    

    