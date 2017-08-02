# -*- coding:utf-8 -*-

def InsertingSort(l):
    for i in range(1, len(l)):
        for j in range(i):
            if l[i] < l[j]:
                tem = l[i]
                for k in range(i, j,-1):
                    l[k] = l[k-1]
                l[j] = tem
                break
            
if __name__ == "__main__":
    print("请输入需要排序的数字，用空格相连：")
    l = input().split(" ")
    l = [int(i) for i in l]
    InsertingSort(l)
    print(l)