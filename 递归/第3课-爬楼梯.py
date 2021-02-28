"""
    https://leetcode-cn.com/problems/climbing-stairs/
    https://leetcode-cn.com/problems/climbing-stairs/solution/70zhong-quan-chu-ji-python3hui-ji-liao-ti-jie-qu-w/
 第n个楼梯就是由 在第n-2的楼梯的方法+2或者第n-1阶的楼梯方法
 寻找最近的重复子问题

"""

class Solution:
    def climbStairs(self, n: int) -> int:
        dp_0 = 1
        dp_1 = 1
        if n < 2:
            return 1
        
        for i in range(2, n+1):
            dp_n = dp_0 + dp_1
            dp_0 = dp_1
            dp_1 = dp_n

        return dp_n
    
    
class Solution:

    @functools.lru_cache(100)  # 缓存装饰器
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)