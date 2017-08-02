#coding:utf-8

def Selection_sort(l):
    for i in range(len(l)):
        temMin = i
        for j in range(i,len(l)):
            if l[j] < l[temMin]:
                temMin = j
        l[i], l[temMin] = l[temMin], l[i]
        
if __name__ == "__main__":
    print("请输入需要排序的数字，用空格相连：")
    l = input().split(" ")
    l = [int(i) for i in l]
    Selection_sort(l)
    print(l)