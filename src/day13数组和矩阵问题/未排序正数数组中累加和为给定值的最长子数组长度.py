# coding: utf-8
'''
【题目】
给定一个无序数组arr，其中元素可正、可负、可0，给定一个整数k。求arr 所有的子
数组中累加和为k 的最长子数组长度。
'''


def maxLength(arr, k):
    s = 0
    m = {}
    # m[key]=value ，key表示从arr最左边开始累加的过程中出现过的sum值，
    # 对应的value值则表示sum值最早出现的位置。
    m[0] = -1
    length = 0  # 记录和为k的子数组最大长度
    for i in range(len(arr)):
        s = s + arr[i]  # 表示从0到i的累加和
        if s - k in m:
            length = max(i - m[s - k], length)
        if s not in m:
            m[s] = i
    return length


if __name__ == '__main__':
    arr, k = [1, 2, 3, 3, -3, 1], 6
    print(maxLength(arr, k))
