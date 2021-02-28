"""
https://leetcode-cn.com/problems/remove-k-digits/
https://leetcode-cn.com/problems/remove-k-digits/solution/yi-zhao-chi-bian-li-kou-si-dao-ti-ma-ma-zai-ye-b-5/
"""

# 该题是要求各个数字的相对的位置不变
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        if len(num) <= k:
            return '0'

        stack = []
        remain = len(num) - k

        for i, num in enumerate(num):

            while stack and k and stack[-1] > num:
                # 保持栈里的数都小于当前值
                # 若当前数小于栈顶的数，则弹出栈顶的数
                stack.pop()
                k = k - 1
            stack.append(num)
            if k < 0:
                break
            
        return ''.join(stack[:remain]).lstrip('0') or '0'