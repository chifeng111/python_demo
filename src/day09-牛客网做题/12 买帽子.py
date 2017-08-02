# coding: utf-8
import sys 

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    s = list(set(s.split(" ")))
    l = [int(i) for i in s]
    l = sorted(l)
    if len(l) < 3:
        print(-1)
    else:
        print(l[2])