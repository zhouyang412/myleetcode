"""
    https://leetcode-cn.com/problems/jump-game-ii/
    https://leetcode-cn.com/problems/jump-game-ii/solution/tiao-yue-you-xi-ii-by-leetcode-solution/
    https://leetcode-cn.com/problems/jump-game-ii/solution/xiong-mao-shua-ti-python3-tan-xin-wei-hu-ke-da-d-4/

"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                # 更新最远距离
                maxPos = max(maxPos, i + nums[i])
                # 在第一次的跳跃的范围内，所有点中所能到达的最远位置来更新边界
                # 就是现在所保存的maxpos最远位置，是由上一次的所能跳跃的范围内的所有点的基础上跳跃而来
                # 更新后则为上一次跳跃范围内的点所能到达的最远位置
                if i == end:
                    end = maxPos
                    step += 1
        return step

