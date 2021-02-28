"""
    https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/
    https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/solution/123-mai-mai-gu-piao-de-zui-jia-shi-ji-ii-zfh9/
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # 0:无操作 1:第一次买入 2:第一次卖出 3:第二次买入 4:第二次卖出
        dp = [[0] * 5 for _ in range(len(prices))]

        dp[0][1], dp[0][3] = -prices[0], -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = dp[i-1][0]
            # 维持上一个状态的第一次买入，或者买入股票
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            # 当前时刻卖出，则为上一个状态的买入状态加上当前价格
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
            dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])

        return dp[len(prices)-1][4]