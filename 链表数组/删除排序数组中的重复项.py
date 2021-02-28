## https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/submissions/
## https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/solution/shuang-zhi-zhen-python3-by-zhao-si-1/
## https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/solution/reng-ran-shi-shuang-zhi-zhen-fa-by-wu-ming-shi-7/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        if len(nums) == 0:
            return 0
            
        for _ in range(len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            j += 1    
        return i + 1