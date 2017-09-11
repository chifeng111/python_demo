# coding: utf-8
'''
思路：搜索二叉树的中序遍历为递增序列
'''


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def createBTree():
    _1, _3, _5, _7 = Node(1), Node(3), Node(5), Node(7)
    _2, _6 = Node(2, _1, _3), Node(6, _5, _7)
    _4 = Node(4, _2, _6)
    return _4


def isBST(head):
    pre = None
    stack = list()
    while stack or head:
        if head:
            stack.append(head)
            head = head.left
        elif stack:
            head = stack.pop()
            if pre and pre.value > head.value:
                return False
            pre = head  # 记住当前值，用于和下一次对比
#             print(node.value)
            head = head.right
    return True


if __name__ == '__main__':
    head = createBTree()
    print(isBST(head))
