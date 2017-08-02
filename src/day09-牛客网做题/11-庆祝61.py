# coding: utf-8
import sys

def f(l):
    s = sorted(l)
    new_l = []
    for inx, val in enumerate(s):
        if inx%2:
            new_l.append(val)
        else:
            new_l.insert(0, val)
    return new_l

def countDiff(l):
    smallest_diff = abs(l[0]-l[-1])
    for i in range(0, len(l)-1):
        smallest_diff = max(smallest_diff, abs(l[i]-l[i+1]))
    return smallest_diff
        

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    h_l = [int(i) for i in s.split(" ")]
    ordered_l = f(h_l)
#     print(ordered_l)
    print(countDiff(ordered_l))
    
    