# coding: utf-8
class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def createBTree1():
    _8, _9 = Node(8), Node(9)
    _4, _5, _6, _7 = Node(4, right=_8), Node(5, _9), Node(6), Node(7)
    _2, _3 = Node(2, _4, _5), Node(3, _6, _7)
    _1 = Node(1, _2, _3)
    return _1


def createBTree2():
    _8, _9 = Node(8), Node(9)
    _4, _5 = Node(4, right=_8), Node(5, _9)
    _2 = Node(2, _4, _5)
    return _2


def check(t1, t2):
    if t1 == None and t2 == None:
        return True
    if t1 == None or t2 == None:
        return False
    if t1.value == t2.value:
        return check(t1.left, t2.left) and check(t1.right, t2.right)
    else:
        return False


def t2IsSubTreeOfT1(t1, t2):
    if t1 == None:
        return False
    if t1.value == t2.value:
        return check(t1, t2)
    return t2IsSubTreeOfT1(t1.left, t2) or t2IsSubTreeOfT1(t1.right, t2)


if __name__ == '__main__':
    t1 = createBTree1()
    t2 = createBTree2()
    print(t2IsSubTreeOfT1(t1, t2))
