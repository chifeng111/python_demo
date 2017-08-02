# coding: utf-8

import sys

if __name__ == '__main__':
    s = sys.stdin.readline().strip()
    count = 0
    for i, v in enumerate(s):
        if i%2 and v == 'W':
            count += 1
        if not i%2 and v == 'B':
            count += 1
    count = min(count, len(s)-count)
    print(count)
        

