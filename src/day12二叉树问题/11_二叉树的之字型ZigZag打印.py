# coding: utf-8
from collections import deque


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


def printByZigZag(head):
    queue = deque()
    queue.insert(0, None)
    queue.insert(0, head)
    top = True  # true代表从头进从头出，false代表从尾进从尾出
    print("Level 1 from left to right: ", end="")
    level = 2
    while queue:
        if top:
            h = queue.popleft()
            if h:
                print(h.value, end=" ")
                if h.right:
                    queue.append(h.left)
                if h.left:
                    queue.append(h.right)
            else:
                if queue:
                    queue.insert(0, None)
                    print("\nLevel {} from right to left: ".format(level), end="")
                    top = False
                    level += 1
                else:
                    break
        else:
            h = queue.pop()
            if h:
                print(h.value, end=" ")
                if h.left:
                    queue.insert(0, h.right)
                if h.right:
                    queue.insert(0, h.left)
            else:
                if queue:
                    queue.append(None)
                    print("\nLevel {} from left to right: ".format(level), end="")
                    top = True
                    level += 1
                else:
                    break


if __name__ == '__main__':
    head = createBTree()
    printByZigZag(head)
