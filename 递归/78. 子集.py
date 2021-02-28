"""
    https://leetcode-cn.com/problems/subsets/
    https://leetcode-cn.com/problems/subsets/solution/hot-100-78zi-ji-python3-hui-su-liang-chong-jie-ti-/
每一个数字都可选或者可不选
这里的p，需要进行改变是因为,p为递归函数中的一个参数，他会随着递归的改变而改变，不是本层的本地变量
每一层是隔开，参数上的变量，这里改变后会影响前后层。
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums_len  = len(nums)
    
        res = []
        if not nums:
            return []
        self.dfs(res, nums, p=[], idx=0)
        return res


    def dfs(self, res, nums, p, idx):
        # p中存储的是中间结果
        if idx == self.nums_len:
            res.append(p)
            return 

        # 如果当前数字不选中的话
        self.dfs(res, nums, p.copy(), idx+1)
        # 如果当前数字选中，添加并继续下传
        p.append(nums[idx]) 
        self.dfs(res, nums, p.copy(), idx+1)

        # # p的数值不仅限于当前层会影响前后层这里需要去掉
        # p.remove(p[len(p)-1])


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums_len  = len(nums)
    
        self.res = []
        if not nums:
            return []
        self.dfs([], nums, idx=0)
        return self.res


    def dfs(self, res, nums, idx):
        # p中存储的是中间结果
        if idx == self.nums_len:
            self.res.append(res)
            return 
        # 如果当前数字不选中的话
        self.dfs(res+[nums[idx]], nums,idx+1)
        # 如果当前数字选中，添加并继续下传
        self.dfs(res, nums, idx+1)

        
# 迭代

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = [[]]
        for num in nums:
            sub_res = []
            for r in res:
                sub_res.append(r + [num])
            res.extend(sub_res)
        return res