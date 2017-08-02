#-*- coding:utf-8 -*-
import sys

def change_num(s): 
    if len(s) == 1:
        return 1
    tem = 1
    for i in s:
        tem = tem * int(i)
    return str(tem)

if __name__ == "__main__":
    num = sys.stdin.readline().strip()
    count = 0
    while len(num) != 1:
        num = change_num(num)
        count += 1
    print(count)
