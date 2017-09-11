# coding: utf-8
'''
完全二叉树：按照层序遍历，若有右孩子而没左孩子返回false，
若有左孩子没右孩子，以后的节点若不是叶子节点，也返回false。
遍历结束后返回true。
'''
from _collections import deque


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def createBTree():
    _1, _3, _5, _7 = Node(1), Node(3), Node(5), Node(7)
    _2, _6 = Node(2, _1, _3), Node(6, _7)
    _4 = Node(4, _2, _6)
    return _4


def isCBT(head):
    if head == None:
        return True
    queue = deque()
    queue.append(head)
    flag = False
    while queue:
        node = queue.popleft()
        if flag and (node.left or node.right):
            return False
        if node.right and not node.left:
            return False
        if node.left and not node.right:
            flag = True
#         print(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return True


if __name__ == '__main__':
    head = createBTree()
    print(isCBT(head))
