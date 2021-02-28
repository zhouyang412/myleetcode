"""
    https://leetcode-cn.com/problems/longest-common-subsequence/
    https://leetcode-cn.com/problems/longest-common-subsequence/solution/ni-de-yi-fu-wo-ba-liao-zui-chang-gong-gong-zi-xu-2/
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m = len(text1)
        n = len(text2)

        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            i_c = text2[i-1]
            for j in range(1, m+1):
                j_c = text1[j-1]
                if i_c == j_c:
                    
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]