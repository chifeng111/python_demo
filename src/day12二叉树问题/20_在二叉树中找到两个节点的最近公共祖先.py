# coding: utf-8
'''
分析：如果以该节点为头节点的树同时包含node1和node2，且该节点的左子树和右子树都不能同时包含node1和node2。
那么该节点就是node1和node2的最近公共祖先。
'''


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return "Node_" + str(self.value)


def createBTree():
    _8 = Node(8)
    _4, _5, _6, _7 = Node(4), Node(5), Node(6), Node(7, _8)
    _2, _3 = Node(2, _4, _5), Node(3, _6, _7)
    _1 = Node(1, _2, _3)
    return _1


def contain(head, node1, node2):
    flag1 = flag2 = False
    queue = list()
    while queue or head:
        if head:
            queue.append(head)
            head = head.left
        elif queue:
            head = queue.pop()
            if head.value == node1.value:
                flag1 = True
            if head.value == node2.value:
                flag2 = True
            if flag1 and flag2:
                return True
            head = head.right
    return False


def nearestAncestor(head, node1, node2):
    queue = list()
    while queue or head:
        if head:
            queue.append(head)
            head = head.left
        elif queue:
            head = queue.pop()
            if contain(head, node1, node2) and not contain(head.left, node1, node2) and not contain(head.right, node1, node2):
                return head
            head = head.right


if __name__ == '__main__':
    head = createBTree()
    node1, node2 = Node(2), Node(5)
#     print(contain(head, node1, node2))
    print(nearestAncestor(head, node1, node2))
