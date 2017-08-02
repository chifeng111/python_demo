# coding: utf-8

import threading
import time


def test(p):
    time.sleep(0.001)
    print(p)
    

ts = []
for i in range(15):
    th = threading.Thread(target=test, args=[i])
    th.start()
    ts.append(th)

        
print('==============')