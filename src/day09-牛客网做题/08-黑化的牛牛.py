# coding: utf-8
import sys

def f(s):
    if len(s) == 1:
        return 1
    pwd = []
    for i in range(len(s)):
        if i == 0:
            p = s[1:]
        elif i == len(s)-1:
            p = s[:len(s)-1]
        else:
            p = s[:i] + s[i+1:]
        if p not in pwd:
            pwd.append(p)
#     print(pwd)
    return len(pwd)

if __name__ == '__main__':
    s = sys.stdin.readline().strip()
    print(f(s))