"""
https://leetcode-cn.com/problems/daily-temperatures/submissions/
https://leetcode-cn.com/problems/daily-temperatures/solution/mei-ri-wen-du-by-leetcode-solution/

"""
class Solution:
    #[73,74,75,71,69,72,76,73]
    def dailyTemperatures(self, T: List[int]) -> List[int]:

        T_len = len(T)
        ans = [0] * T_len
        stack = []

        for i in range(T_len):
            t = T[i]
            while stack and T[stack[-1]] < t:
                tmp = stack.pop()
                ans[tmp] = i - tmp
            stack.append(i)
        return ans