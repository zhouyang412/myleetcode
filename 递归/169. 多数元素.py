"""
    https://leetcode-cn.com/problems/majority-element/
    https://leetcode-cn.com/problems/majority-element/solution/tu-jie-mo-er-tou-piao-fa-python-go-by-jalan/
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = 0
        count = 0
        
        for n in nums:
            # 计数为0，则更新major为当前数值
            if count == 0:
                major = n    
            # 若当前值等于major,count+1，否则count-1
            if n == major:
                count = count + 1
            else:
                count = count - 1

        return major