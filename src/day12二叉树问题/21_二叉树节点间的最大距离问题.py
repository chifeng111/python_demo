# coding: utf-8
'''
分析：返回左子树层数+右子树层数+1
'''


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return "Node_" + str(self.value)


def createBTree():
    _4, _5, _6, _7 = Node(4), Node(5), Node(6), Node(7)
    _2, _3 = Node(2, _4, _5), Node(3, _6, _7)
    _1 = Node(1, _2, _3)
    return _1


def fun(head, layer):
    if head == None:
        layer[0] = 0
        return 0
    fun(head.left, layer)
    lLayer = layer[0]
    fun(head.right, layer)
    rLayer = layer[0]
    layer[0] = max(lLayer, rLayer) + 1
    return lLayer + rLayer + 1


def maxDistance(head):
    if head == None:
        return 0
    layer = [None]
    return fun(head, layer)


if __name__ == '__main__':
    head = createBTree()
    print(maxDistance(head))
