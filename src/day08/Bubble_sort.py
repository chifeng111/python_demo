# -*- coding:utf-8 -*-

def BubbleSort(l):
    for i in range(len(l), 1,-1):
        for j in range(1, i):
            if l[j] < l[j-1]:
                l[j], l[j-1] = l[j-1], l[j]
                
if __name__ == "__main__":
    print("请输入需要排序的数字，用空格相连：")
    l = input().split(" ")
    l = [int(i) for i in l]
    BubbleSort(l)
    print(l)