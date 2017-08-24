# coding: utf-8


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def preOrder(head, k, layer, hashMap, preSum, maxLength):
    if head == None:
        return maxLength
    curSum = preSum + head.value
    if curSum not in hashMap:
        hashMap[curSum] = layer
    if curSum - k in hashMap:
        maxLength = max(layer - hashMap[curSum - k], maxLength)
    maxLength = preOrder(head.left, k, layer + 1, hashMap, curSum, maxLength)
    maxLength = preOrder(head.right, k, layer + 1, hashMap, curSum, maxLength)
    if layer == hashMap[curSum]:
        hashMap.pop(curSum)
    return maxLength


def getMaxLength(head, k):
    hashMap = {}
    hashMap[0] = 0
    return preOrder(head, k, 1, hashMap, 0, 0)


def createBTree():
    _1, _6 = Node(1), Node(6)
    _01, _0, _2, _001 = Node(1), Node(0, _1, _6), Node(2), Node(1)
    _3, _9 = Node(3, _01, _0), Node(-9, _2, _001)
    _03 = Node(-3, _3, _9)
    return _03


if __name__ == '__main__':
    head, k = createBTree(), 6
    print(getMaxLength(head, k))
