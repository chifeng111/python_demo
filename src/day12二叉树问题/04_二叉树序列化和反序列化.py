# coding: utf-8
from collections import deque


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def serialByPre(head):
    if head == None:
        return "#!"
    res = str(head.value) + "!"
    res += serialByPre(head.left)
    res += serialByPre(head.right)
    return res


def reconPreOrder(queue):
    value = queue.popleft()
    if value == "#":
        return None
    head = Node(value)
    head.left = reconPreOrder(queue)
    head.right = reconPreOrder(queue)
    return head


def reconByPreString(_str):
    strValue = _str.split("!")
    queue = deque(strValue)
    queue.pop()
    return reconPreOrder(queue)


def createBTree():
    _3 = Node(3)
    _12 = Node(12, _3)
    return _12


if __name__ == '__main__':
    head = createBTree()
    _str = serialByPre(head)
    print(_str), print("=====================")
    head = reconByPreString(_str)
    print("反序列化")
    print(head.value)
    print(head.left.value)
    print(head.right)
