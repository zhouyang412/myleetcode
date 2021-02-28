"""
    https://leetcode-cn.com/problems/coin-change/
    https://leetcode-cn.com/problems/coin-change/solution/322-ling-qian-dui-huan-dong-tai-gui-hua-7d5ec/
    类似于爬楼梯，每一个金额都是从i-coin + coin得到则选择其中较小的值
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp
        if amount < 0:
            return -1
        res = [0] + [amount+1] * amount  # 用amount+1初始化各子问题对应的硬币数量，因为找零数量不可能超过amount
        for i in range(1, len(res)):
            for coin in coins:
                if i < coin:
                    continue
                # 若之前已经有方案次数小，则保留
                # 否则可以理解为从i-coin凑上当前值的coin到i数值的个数
                res[i] = min(res[i], 1+res[i-coin])
        return res[-1] if res[-1] != amount+1 else -1      # 如果结果等于初始值，说明无法正常找零
