# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        if exponent < 0:
            return 1./self.Power(base, -exponent)
        result = self.Power(base, exponent//2)  #Python 2.7用/
        result *= result
        if exponent%2 == 1:
            result *= base
        return result
        

    
if __name__ == '__main__':
    s = Solution()
    print(s.Power(2.0, 4))