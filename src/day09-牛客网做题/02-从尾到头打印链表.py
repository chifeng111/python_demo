# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def printListFromTailToHead(self, listNode):
        # write code here
        new_list = []
        while listNode.next != None:
            new_list.append(listNode.val)
            listNode = listNode.next
        new_list.append(listNode.val)
        new_list.reverse()
        print(new_list)


if __name__ == '__main__':
        a = ListNode(1)
        b = ListNode(2)
        c = ListNode(3)     
        a.next = b
        b.next = c
        s = Solution()
        s.printListFromTailToHead(a)