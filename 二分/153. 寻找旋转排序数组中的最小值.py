"""
    https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/
    https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/solution/er-fen-cha-zhao-wei-shi-yao-zuo-you-bu-dui-cheng-z/
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:         
                left = mid + 1
            else:                               
                right = mid
        return nums[left]

