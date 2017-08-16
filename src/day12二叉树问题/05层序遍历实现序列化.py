# coding: utf-8
from _collections import deque


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def createBTree():
    _3 = Node(3)
    _12 = Node(12, _3)
    return _12


def serialByLevel(head):
    if head == None:
        return "#!"
    res = ""
    queue = deque()
    queue.insert(0, head)
    while queue:
        h = queue.pop()
        if h == None:
            res += "#!"
        else:
            res += str(h.value) + "!"
            queue.insert(0, h.left)
            queue.insert(0, h.right)
    return res


if __name__ == '__main__':
    head = createBTree()
    res = serialByLevel(head)
    print(res)
