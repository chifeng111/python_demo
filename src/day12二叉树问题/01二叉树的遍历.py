# coding: utf-8


def createBTree():
    D, E, F = Node('D'), Node('E'), Node('F')
    B, C = Node('B', D, E), Node('C', F)
    A = Node('A', B, C)
    return A


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def preOrder(head):
    if head == None:
        return
    print(head.value, end=" ")
    preOrder(head.left)
    preOrder(head.right)


def inOrder(head):
    if head == None:
        return
    inOrder(head.left)
    print(head.value, end=" ")
    inOrder(head.right)


def posOrder(head):
    if head == None:
        return
    posOrder(head.left)
    posOrder(head.right)
    print(head.value, end=" ")


if __name__ == '__main__':
    head = createBTree()
    print('先序遍历：', end=""), preOrder(head), print('')
    print('中序遍历：', end=""), inOrder(head), print('')
    print('后序遍历：', end=""), posOrder(head), print('')
