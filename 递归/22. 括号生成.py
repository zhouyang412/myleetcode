"""
    https://leetcode-cn.com/problems/generate-parentheses/
    https://leetcode-cn.com/problems/generate-parentheses/solution/gou-zao-di-tui-gong-shi-si-lu-jian-dan-xing-neng-j/

"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n < 1:
            return []

        res = ['()', ]
        # 初始化时就是第一步的结果
        for _ in range(n-1):
            cur = set()
            for r in res:
                r_len = len(r)
                for idx in range(r_len):
                    cur.add(r[:idx] + '()' + r[idx:])
            res = list(cur)
        return res
    
    
    
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.dfs(res, n, n, '')
        return res
        
    def dfs(self, res, left, right, path):
        if left == 0 and right == 0:
            res.append(path)
            return
        if left > 0:
            self.dfs(res, left - 1, right, path + '(')
        if left < right:
            self.dfs(res, left, right - 1, path + ')')