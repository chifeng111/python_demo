# coding: utf-8
'''
【题目】
给定无序数组arr，返回其中最长的连续序列的长度。
【举例】
arr=[100,4,200,1,3,2]，最长的连续序列为[1,2,3,4]，所以返回4。
'''


def num(arr):
    _max = 1
    m = {}
    for i in arr:
        if i not in m:
            m[i] = 1
            if i - 1 in m:
                _max = max(_max, merge(m, i - 1, i))
            if i + 1 in m:
                _max = max(_max, merge(m, i, i + 1))
    return _max


def merge(m, less, more):
    left = less - m.get(less) + 1
    right = more + m.get(more) - 1
    _len = right - left + 1
    m[left] = _len
    m[right] = _len
    return _len


if __name__ == '__main__':
    arr = [100, 4, 200, 1, 3, 2]
    print(num(arr))
