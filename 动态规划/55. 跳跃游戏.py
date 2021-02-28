"""
    https://leetcode-cn.com/problems/jump-game/
    https://leetcode-cn.com/problems/jump-game/solution/tiao-yue-you-xi-tan-xin-suan-fa-you-hua-zvka2/
    https://leetcode-cn.com/problems/jump-game/solution/pythonji-bai-97kan-bu-dong-ni-chui-wo-by-mo-lan-4/
    
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums is None: return False
        tmp = len(nums) - 1
        for i in range(len(nums)-1, -1 , -1):# 从后往前遍历
            if i + nums[i] >= tmp: # 遍历到的点是可以到达当前保存的tmp的，则更新tmp，就是从i可以达到tmp点
                tmp = i

        return tmp == 0
    
    

class Solution:
    def canJump(self, nums) :
        max_i = 0       #初始化当前能到达最远的位置
        for i, jump in enumerate(nums):   #i为当前位置，jump是当前位置的跳数
            if max_i>=i and i+jump>max_i:  #如果当前位置能到达，并且当前位置+跳数>最远位置  
                max_i = i+jump  #更新最远能到达位置
        return max_i>=i

    
