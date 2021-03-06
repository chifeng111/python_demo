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


def printByLevel(head):
    queue = list()
    queue.insert(0, head)
    queue.insert(0, None)
    print("Level 1 : ", end='')
    level = 2
    while queue:
        h = queue.pop()
        if h:
            print(h.value, end=" ")
            if h.left:
                queue.insert(0, h.left)
            if h.right:
                queue.insert(0, h.right)
        else:
            if not queue:
                break
            print("\nLevel {} : ".format(level), end='')
            level += 1
            queue.insert(0, None)
#     print()


if __name__ == '__main__':
    head = createBTree()
    printByLevel(head)
