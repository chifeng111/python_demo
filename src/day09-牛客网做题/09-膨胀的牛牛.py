# coding: utf-8
import sys

def f(size, l):
    for i in l:
        if size == i:
            size += i
    return size

if __name__ == '__main__':
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()
    n, size = int(s1.split(" ")[0]), int(s1.split(" ")[1])
    gras_list = [int(i) for i in s2.split(" ")]
    print(f(size, gras_list))
