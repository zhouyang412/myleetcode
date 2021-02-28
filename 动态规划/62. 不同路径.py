"""
    https://leetcode-cn.com/problems/unique-paths/
    https://leetcode-cn.com/problems/unique-paths/solution/bu-tong-lu-jing-by-leetcode-solution-hzjf/
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        import numpy as np

        dp = np.zeros((n, m), dtype=np.int32)
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        # print(dp[1][2])
        # print(dp[n-1][m-1])
        return int(dp[n-1][m-1])