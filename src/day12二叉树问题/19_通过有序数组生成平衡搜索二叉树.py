# coding: utf-8
'''
分析：用有序数组的中间数生成搜索二叉树的头结点。然后递归的生成左子树和右子树。
'''


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def fun(arr, start, end):
    if start > end:
        return None
    if start == end:
        return Node(arr[start])
    m_index = start + int((end - start + 1) / 2)
    node = Node(arr[m_index])
    node.left = fun(arr, start, m_index - 1)
    node.right = fun(arr, m_index + 1, end)
    return node


def createBSBT(arr):
    if len(arr) == 0:
        return None
    return fun(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    head = createBSBT(arr)
