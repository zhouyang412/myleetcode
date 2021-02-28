'''
  https://leetcode-cn.com/problems/valid-parentheses/
  https://leetcode-cn.com/problems/valid-parentheses/solution/zhu-bu-fen-xi-tu-jie-zhan-zhan-shi-zui-biao-zhun-d/
  因此我们考虑使用栈，当遇到匹配的最小括号对时，我们将这对括号从栈中删除（即出栈），如果最后栈为空，那么它是有效的括号，反之不是。
  
  1.暴力求解：反复循环，每次替换前后idx为一个括号的括号为空 -->O(N^2)
  2.栈ß
'''
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(',']':'[','}':'{'}
        stack = []
        if not s:
            return False
        if s[0] in dic:
            return False
        
        for i in s:
            # stack不为空，且i为后面的括号，则检查前一个是不是其对应的前面的括号
            # 如果是，则弹出其前面的符号，并继续。
            if stack and i in dic:
                if stack[-1] == dic[i]: stack.pop()
                else: return False
            # 如果当前stack为空，且i为前面的括号则推入栈
            else: stack.append(i)
            
        return not stack