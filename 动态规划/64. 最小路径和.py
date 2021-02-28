"""
    https://leetcode-cn.com/problems/minimum-path-sum/
    https://leetcode-cn.com/problems/minimum-path-sum/solution/zui-xiao-lu-jing-he-by-leetcode-solution/
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        if m == n and m == 1:
            return grid[0][0]
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for row in range(m):
            for col in range(n):
                if row == 0:
                    dp[row][col] = dp[row][col-1]  + grid[row][col]
                elif col == 0:
                    dp[row][col] = dp[row-1][col] + grid[row][col]
                else:
                    dp[row][col] = min(dp[row-1][col], dp[row][col-1]) + grid[row][col]
        # print(dp[m - 1][n - 1], dp[-1][-1])
        return  dp[-1][-1]