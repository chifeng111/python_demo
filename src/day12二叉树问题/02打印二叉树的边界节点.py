# coding: utf-8
'''
给定一棵二叉树的头节点head，按照如下两种标准分别实现二叉树边界节点的逆时针
打印。
'''


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def getHeight(head, layer):
    if head == None:
        return layer
    return max(getHeight(head.left, layer + 1), getHeight(head.right, layer + 1))


def setEdgeMap(head, layer, edgeMap):
    if head == None:
        return
    if edgeMap[layer][0] == None:
        edgeMap[layer][0] = head
    edgeMap[layer][1] = head
    setEdgeMap(head.left, layer + 1, edgeMap)
    setEdgeMap(head.right, layer + 1, edgeMap)


def printLeafNotInMap(head, layer, edgeMap):
    if head == None:
        return
    if head.left == None and head.right == None and head != edgeMap[layer][0] \
            and head != edgeMap[layer][1]:
        print(head.value, end=" ")
    printLeafNotInMap(head.left, layer + 1, edgeMap)
    printLeafNotInMap(head.right, layer + 1, edgeMap)


def printEdge(head):
    if head == None:
        return
    height = getHeight(head, 0)
    edgeMap = [[None, None] for i in range(height)]
    setEdgeMap(head, 0, edgeMap)
    # 打印左边界
    for i in range(height):
        print(edgeMap[i][0].value, end=" ")
    # 打印既不是左边界，又不是右边界的叶子节点
    printLeafNotInMap(head, 0, edgeMap)
    # 打印右边界，逆序
    for i in range(height - 1, 0, -1):
        print(edgeMap[i][1].value, end=" ")


def preOrder(head):
    if head == None:
        return
    print(head.value, end=" ")
    preOrder(head.left)
    preOrder(head.right)


def buildBTree():
    _13, _14, _15, _16 = Node(13), Node(14), Node(15), Node(16)
    _11, _12 = Node(11, _13, _14), Node(12, _15, _16)
    _7, _8, _9, _10 = Node(7), Node(8, right=_11), Node(9, _12), Node(10)
    _4, _5, _6 = Node(4, _7, _8), Node(5, _9, _10), Node(6)
    _2, _3 = Node(2, right=_4), Node(3, _5, _6)
    _1 = Node(1, _2, _3)
    return _1


if __name__ == '__main__':
    head = buildBTree()
    print('先序遍历：', end=""), preOrder(head), print()
    print('逆时针打印边界节点：', end=""), printEdge(head), print()
