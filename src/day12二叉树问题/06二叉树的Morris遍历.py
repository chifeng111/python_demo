# coding: utf-8


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return "Node_" + str(self.value)


def morrisInOrder(head):
    if head == None:
        return
    cur = head
    while cur:
        cur2 = cur.left
        if cur2:
            while cur2.right and cur2.right != cur:
                cur2 = cur2.right
            if cur2.right == None:
                cur2.right = cur
                cur = cur.left
                continue
            else:
                cur2.right = None
        print(cur.value, end=" ")
        cur = cur.right
    print()


def buildBTree():
    _1, _3, _5, _7 = Node(1), Node(3), Node(5), Node(7)
    _2, _6 = Node(2, _1, _3), Node(6, _5, _7)
    _4 = Node(4, _2, _6)
    return _4


if __name__ == '__main__':
    head = buildBTree()
    print(head), print(head.left.left), print(head.left.left.left)
    morrisInOrder(head)
