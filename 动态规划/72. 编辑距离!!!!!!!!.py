"""
    https://leetcode-cn.com/problems/edit-distance/
    https://leetcode-cn.com/problems/edit-distance/solution/bian-ji-ju-chi-by-leetcode-solution/
    
    dp[i][j]代表的是word1中的第i个字符前的字符换与word2中第j个字符前的字符串的编辑距离
    
    word1删除 等价于 word2插入
    word2删除 等价于 word1插入
    word1替换 等价于 word2替换
    
    一共有三种操作：插入，删除，替换
    假设有word1 --> i，word2 --> j
    插入：相当于在word1中插入word2[j],此时相当于最后一个字符相等,编辑距离为word1[i]与word2[:j-1]的编辑距离+1
    删除：相当于将word1[i]给删除，计算word1[:i-1]与word2的编辑距离+1
    
    替换：将word1的最后一个字符串替换成word2的最后一个字符串,此时计算word1[:i-1]与word2[:j-1]的编辑距离+1,
        若最后一个字符相等，增直接各自删除而不需要进行替换操作。
    
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        # if not word1 or not word2:return 0

        m = len(word1) + 1
        n = len(word2) + 1

        dp = [[0] * n for _ in range(m)]

        for col in range(n):
            dp[0][col] = col
        
        for row in range(m):
            dp[row][0] = row

        # 这里需要加1！负责遍历不到最后一个字符因为这里添加了一行一列
        for i in range(1, m):
            for j in range(1, n):
                insert = dp[i][j-1] + 1
                remove = dp[i-1][j] + 1
                replace = dp[i-1][j-1]
                if word1[i-1] != word2[j-1]:
                    replace += 1

                dp[i][j] = min(insert, remove, replace)

        return dp[m-1][n-1]


