# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        a = b = 1
        sum = 0
        i = 3
        while i <= n:
            sum = a+b
            a, b = b, sum
            i += 1
        return sum
    
if __name__ == '__main__':
        s = Solution()
        for i in range(100):
            print(s.Fibonacci(i))