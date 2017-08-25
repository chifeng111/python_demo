# coding: utf-8
class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return "Node_" + str(self.value)


def createBTree():
    _1, _3, _5, _7 = Node(1), Node(3), Node(5), Node(7)
    _2, _4 = Node(2, _1, _3), Node(4, _5, _7)
    _6 = Node(6, _2, _4)
    return _6


def getTwoErrNodes(head):
    errs = [None, None]
    if head == None:
        return errs
    stack = list()
    pre = None
    while stack or head:
        if head:
            stack.append(head)
            head = head.left
        else:
            head = stack.pop()
#             print(head, end=" ")
            if pre and pre.value > head.value:
                if errs[0] == None:
                    errs[0], errs[1] = pre, head
                else:
                    errs[1] = head
            pre = head
            head = head.right
    return errs


if __name__ == '__main__':
    head = createBTree()
    errs = getTwoErrNodes(head)
    print([str(i) for i in errs])
