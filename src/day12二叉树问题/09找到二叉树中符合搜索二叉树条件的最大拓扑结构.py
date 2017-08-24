# coding: utf-8
class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return "Node_" + str(self.value)


def createBTree():
    _2, _5, _11, _15 = Node(2), Node(5), Node(11), Node(15)
    _4, _14, _20, _16 = Node(4, _2, _5), Node(14, _11, _15), Node(20), Node(16)
    _0, _3, _10, _13 = Node(0), Node(3), Node(10, _4, _14), Node(13, _20, _16)
    _1, _12 = Node(1, _0, _3), Node(12, _10, _13)
    _6 = Node(6, _1, _12)
    return _6


def isBSTNode(h, n, value):
    if h == None:
        return False
    if h == n:
        return True
    if h.value > value:
        return isBSTNode(h.left, n, value)
    else:
        return isBSTNode(h.right, n, value)


def maxTopo(head, n):
    if head == None or n == None:
        return 0
    if isBSTNode(head, n, n.value):
        return maxTopo(head, n.left) + maxTopo(head, n.right) + 1
    else:
        return 0


def fun(head):
    if head == None:
        return 0
    _max = maxTopo(head, head)
    _maxl = fun(head.left)
    _maxr = fun(head.right)
    _max = max(_max, _maxl, _maxr)
    return _max


if __name__ == '__main__':
    head = createBTree()
    print(fun(head))
