# coding: utf-8
from collections import deque


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


def reconByLevelString(_str):
    values = deque(_str.split("!"))
    values.pop()
    for i in range(len(values)):
        if values[i] == "#":
            values[i] = None
        else:
            values[i] = Node(values[i])
    head = values.popleft()
    queue = deque()
    queue.insert(0, head)
    while queue:
        node = queue.pop()
        node.left = values.popleft()
        node.right = values.popleft()
        if node.left:
            queue.insert(0, node.left)
        if node.right:
            queue.insert(0, node.right)
    return head


if __name__ == '__main__':
    head = createBTree()
    res = serialByLevel(head)
    print("序列化：", end=""), print(res)
    print("反序列化：")
    h = reconByLevelString(res)
    print(h.value)
    print(h.left.value)
    print(h.right)
