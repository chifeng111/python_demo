# coding: utf-8
class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def serialByPre(head):
    pass


def createBTree():
    D, E, F = Node('D'), Node('E'), Node('F')
    B, C = Node('B', D, E), Node('C', F)
    A = Node('A', B, C)
    return A


if __name__ == '__main__':
    head = createBTree()
    serialByPre(head)
