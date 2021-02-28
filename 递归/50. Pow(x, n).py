"""
    https://leetcode-cn.com/problems/powx-n/
    https://leetcode-cn.com/problems/powx-n/solution/50-powx-n-kuai-su-mi-qing-xi-tu-jie-by-jyd/
    
    x^n --> x^10 --> (x^5)^2 --> (x*(x^2)^2)^2 = x^2 * ((x^2)^2)^2
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.0: return 0.0
        res = 1
        if n < 0: x, n = 1 / x, -n
        while n:
            if n & 1: res *= x
            x *= x
            n >>= 1
        return res

class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0: return 1
        
        if n < 0:
            x, n = 1/x, -n

        sub_re = self.myPow(x, n//2)
        if n % 2 == 1:
            res = sub_re * sub_re * x
        else:
            res = sub_re * sub_re
        return res


