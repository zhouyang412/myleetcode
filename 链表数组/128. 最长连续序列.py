"""
    https://leetcode-cn.com/problems/longest-consecutive-sequence/
    https://leetcode-cn.com/problems/longest-consecutive-sequence/solution/zui-chang-lian-xu-xu-lie-by-leetcode-solution/

"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = {i:i for i in nums}
        max_len = 0

        for num in nums:
            cur_len = 1
            
            # 较小的数将遍历可能属于它的连续序列，假设序列存在则必包含序列中比它大的数为起始的序列
            # 因此若存在比它小的数，可以直接略过
            if num - 1 in nums:
                continue
            # 持续查找当属于当前数字的连续序列
            while num + 1 in nums:
                cur_len += 1
                num = num + 1
            if cur_len > max_len:
                max_len = cur_len
        return max_len