"""
    https://leetcode-cn.com/problems/maximum-subarray/
    https://leetcode-cn.com/problems/maximum-subarray/solution/zui-da-zi-xu-he-by-leetcode-solution/
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        pre = float('-inf')
        max_value = float('-inf')

        for num in nums:
            pre = max(pre + num, num)
            max_value = max(max_value, pre)
        return max_value
