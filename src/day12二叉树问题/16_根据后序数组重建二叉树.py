# coding: utf-8
'''
题目：如果整型数组arr 中没有重复值，且已知是一棵搜索二叉树的后序遍历结果，通
过数组arr 重构二叉树。
'''


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return "Node_" + str(self.value)


def fun(arr, start, end):
    if start > end:
        return None
    head = Node(arr[end])
    medium = -1
    for i in range(start, end):
        if arr[i] > arr[end]:
            medium = i
            break
    if medium == -1:
        medium = end
    head.left = fun(arr, start, medium - 1)
    head.right = fun(arr, medium, end - 1)
    return head


def posArrayToSBT(arr):
    if len(arr) == 0:
        return None
    return fun(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    arr = [1, 3, 2, 5, 7, 6, 4]
#     arr = [1, 3, 2]
    head = posArrayToSBT(arr)
    print(head)
    print(head.left)
    print(head.right)
    print(head.left.left)
