"""
    https://leetcode-cn.com/problems/chou-shu-lcof/
    

"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        res = [1]
        i2, i3, i5 = 0, 0, 0
        count = 1

        while count < n:
            n2, n3, n5 = res[i2]*2, res[i3]*3, res[i5]*5
            min_n = min([n2, n3, n5])
            # 可能出现值相等的情况比如 2*3，3*2，因此不用if-else
            if min_n == n2:
                i2 += 1
            if min_n == n3:
                i3 += 1
            if min_n == n5:
                i5 += 1
                
            count += 1
            res.append(min_n)
            
        return res[-1]