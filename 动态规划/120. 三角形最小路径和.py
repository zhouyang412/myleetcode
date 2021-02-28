"""
    https://leetcode-cn.com/problems/triangle/
    https://leetcode-cn.com/problems/triangle/discuss/38735/Python-easy-to-understand-solutions-(top-down-bottom-up)/?utm_source=LCUS&utm_medium=ip_redirect&utm_campaign=transfer2china
    
    自底向上，比如2的最小路径和就是从小到上3，4的路径和的较小值加上2本身。
    在计算的过程中，以原数值初始化dp的值矩阵，遍历到某个值得时候，直接本身加上下一层相应的值得最小值。
"""
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1: return triangle[0][0]

        dp = triangle.copy()
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] = dp[i][j] + min(dp[i+1][j], dp[i+1][j+1])

        return dp[0][0]


