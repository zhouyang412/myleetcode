"""
   https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
   https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/solution/hui-su-dui-lie-tu-jie-by-ml-zimingmeng/
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        num2chars = {'2':'abc',
                    '3':'def',
                    '4':'ghi',
                    '5':'jkl',
                    '6':'mno',
                    '7':'pqrs',
                    '8':'tuv',
                    '9':'wxyz'}
        self.res = []
        self.dfs('', digits, 0, self.res, num2chars)
        return self.res

    def dfs(self,s, digits, i, res, num2chars):
        if i == len(digits):
            self.res.append(s)
            return

        chars = num2chars[digits[i]]
        for j in range(len(chars)):
            self.dfs(s+chars[j], digits, i+1, res, num2chars)