# coding: utf-8
class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def createBTree():
    _8 = Node(8)
    _4, _5, _6, _7 = Node(4, right=_8), Node(5), Node(6), Node(7)
    _2, _3 = Node(2, _4, _5), Node(3)
    _1 = Node(1, _2, _3)
    return _1


def check(head, flag):
    if head == None:
        flag[0] = True
        return 0
    lH = check(head.left, flag)
    lflag = flag[0]
    rH = check(head.right, flag)
    rflag = flag[0]
    if lflag and rflag and abs(lH - rH) <= 1:
        flag[0] = True
    else:
        flag[0] = False
    return max(rH, lH) + 1


def isBalanceBT(head):
    flag = [False]
    check(head, flag)
    return flag[0]


if __name__ == '__main__':
    head = createBTree()
    print(isBalanceBT(head))
