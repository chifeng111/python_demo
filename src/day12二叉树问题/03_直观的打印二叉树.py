# coding: utf-8


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def printInOrder(head, height, to, _len):
    if head == None:
        return
    printInOrder(head.right, height + 1, "v", _len)
    val = to + str(head.value) + to
    val = "{0: ^17}".format(val)  # 将val固定17位长度
    print(" " * height * _len + val)
    printInOrder(head.left, height + 1, "^", _len)


def printBTree(head):
    print("Binary Tree:")
    printInOrder(head, 0, "H", 17)


def buildBTree():
    _13, _14, _15, _16 = Node(13), Node(14), Node(15), Node(16)
    _11, _12 = Node(11, _13, _14), Node(12, _15, _16)
    _7, _8, _9, _10 = Node(7), Node(8, right=_11), Node(9, _12), Node(10)
    _4, _5, _6 = Node(4, _7, _8), Node(5, _9, _10), Node(6)
    _2, _3 = Node(2, right=_4), Node(3, _5, _6)
    _1 = Node(1, _2, _3)
    return _1


if __name__ == '__main__':
    head = buildBTree()
    printBTree(head)
