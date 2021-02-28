"""
    https://leetcode-cn.com/problems/find-all-duplicates-in-an-array/
    

"""
# 1
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return []

        nums = sorted(nums)
        nums_len = len(nums)
        i = 0

        for j in range(1, nums_len):
            if nums[j] == nums[j-1]:
                nums[i] = nums[j]
                i = i + 1
        return nums[:i]
    
# 2

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        rst = []
        for num in nums:
            # 因为我们是直接原地修改元素为负值来标记是否访问过，因此这里的num一定要取绝对值
            index = abs(num) - 1
            val = nums[index]
            if val < 0:
                # 如果元素值为负数，说明之前存在同一个索引为num的元素
                rst.append(abs(num))
            # 原地修改访问标志
            nums[index] = -nums[index]
        return rst