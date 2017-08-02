# coding: utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def makeList(l):
    if len(l) == 0:
        return None
    p = head = ListNode(l[0])
    for i in range(1,len(l)):
        p.next = ListNode(l[i])
        p = p.next
    return head

# 链表的双指针
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head == None or k == 0:
            return None
        pAhead = head
        for i in range(k-1):
            if pAhead.next != None:
                pAhead = pAhead.next
            else:
                return None
        pBehind = head
        while pAhead.next != None:
            pAhead = pAhead.next
            pBehind = pBehind.next
        return pBehind
                  

if __name__ == '__main__':
    a = makeList([1,2,3,4,5])
    s = Solution()
    print(s.FindKthToTail(a, 2))
    
