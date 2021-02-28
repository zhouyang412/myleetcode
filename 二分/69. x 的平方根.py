"""
    https://leetcode-cn.com/problems/sqrtx/
    https://leetcode-cn.com/problems/sqrtx/solution/x-de-ping-fang-gen-by-leetcode-solution/
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        # y = x^2 在第一象限的时候单调递增，且具有上下界，下界为0，上界为x
        left, mid, right = 1, 0, x

        while left < right:
            mid = (left + right) // 2
            if (mid * mid) > x:
                right = mid - 1
            else:
                left = mid + 1

        return int(right)
