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


def posOrder(head, record):
    if head == None:
        record[0], record[1], record[2] = 0, 10000000, -10000000
        return None
    value = head.value
    left = head.left
    right = head.right
    # 获取左子树中最大搜索二叉树的头节点，叶子数，最小值，最大值
    lBST = posOrder(left, record)
    lSize, lMin, lMax = record[0], record[1], record[2]
    # 获取右子树中最大搜索二叉树的头节点，叶子数，最小值，最大值
    rBST = posOrder(right, record)
    rSize, rMin, rMax = record[0], record[1], record[2]
    # 更新当前二叉树的最小值，最大值
    record[1], record[2] = min(lMin, value), max(rMax, value)
    # 如果满足条件，则当前二叉树为搜索二叉树，返回头节点，并更新二叉数的叶节点数，
    if left == lBST and right == rBST and lMax < value < rMin:
        record[0] = lSize + rSize + 1
        return head
    # 否则返回左右二叉搜索树中叶子节点数最多的。
    record[0] = max(lSize, rSize)
    if lSize > rSize:
        record[1], record[2] = lMin, lMax
        return lBST
    else:
        record[1], record[2] = rMin, rMax
        return rBST


def biggestSubBST(head):
    record = [0] * 3
    return posOrder(head, record)


if __name__ == '__main__':
    head = createBTree()
    h = biggestSubBST(head)
    print(h)
