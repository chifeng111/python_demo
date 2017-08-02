# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        oddList = []    #奇数
        evenList = []   #偶数
        for num in array:
            if num % 2 == 1:
                oddList.append(num)
            else:
                evenList.append(num)
        for j in evenList:
            oddList.append(j)
        return oddList
    
if __name__ == '__main__':
    s = Solution()
    a = [1,2,3,4,5,6,7,8,9]
    print(s.reOrderArray(a))