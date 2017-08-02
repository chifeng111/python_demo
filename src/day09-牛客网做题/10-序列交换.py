# coding: utf-8
import sys

def f(n, l):
    count = 0
    for i in range(0, len(l)-1):
        for j in range(i+1, len(l)):
            if l[i] == l[j]:
                count += 1
    if count == 0:
        return n*(n-1)//2
    return n*(n-1)//2 - count + 1        

if __name__ == '__main__':
    s1 = int(sys.stdin.readline().strip())
    s2 = sys.stdin.readline().strip()
    l = s2.split(" ")
    print(f(s1, l))