"""
    https://leetcode-cn.com/problems/remove-duplicate-letters/
    
    https://leetcode-cn.com/problems/remove-duplicate-letters/solution/yi-kan-jiu-hui-jiu-chai-shou-ba-shou-jia-miqw/
    https://leetcode-cn.com/problems/remove-k-digits/solution/yi-zhao-chi-bian-li-kou-si-dao-ti-ma-ma-zai-ye-b-5/
    
    改题目的序指的是字母在字母表中的序，如‘a’的序就小于‘b’的序，序组成的数字最小
    
"""

class Solution:
    import collections
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        s_counter = collections.Counter(s)

        for c in s:
            if c not in stack:
                # 如果当前字母的序小于栈里的字母且栈里的字母在后续的字符串中还存在则弹出栈里的字母
                while stack and c < stack[-1] and s_counter[stack[-1]] > 0:
                        stack.pop()
                stack.append(c)
            # 每遍历一个字母这里计数减一，因此不需要在while里进行减少。
            s_counter[c] -= 1

        return ''.join(stack)