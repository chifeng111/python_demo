# coding: utf-8
'''
【题目】
给定数组arr，arr[i]==k 代表可以从位置i 向右跳1~k 个距离。比如，arr[2]==3，代表
从位置2 可以跳到位置3、位置4 或位置5。如果从位置0 出发，返回最少跳几次能跳到
arr 最后的位置上。
【举例】
arr=[3,2,3,1,1,4]。
arr[0]==3，选择跳到位置2；arr[2]==3，可以跳到最后的位置。所以返回2。
'''


def jump(arr):
    p = [0 for i in range(len(arr))]
    for i in range(len(arr) - 2, -1, -1):
        if i + arr[i] >= len(arr) - 1:
            p[i] = 1
        else:
            p[i] = min(p[i + 1:i + arr[i] + 1]) + 1
#     return p
    return p[0]


if __name__ == '__main__':
    arr = [3, 2, 3, 1, 1, 4]
    print(jump(arr))
