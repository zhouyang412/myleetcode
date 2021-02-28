"""
    https://leetcode-cn.com/problems/lemonade-change/
    
"""

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        have = {5:0, 10:0, 20:0}

        for bill in bills:
            if bill == 5:
                have[5] += 1
                continue
            elif bill == 10:
                if have[5] < 1:
                    return False
                else:
                    have[5] -= 1
                    have[10] += 1
            else:
                if have[10] >= 1 and have[5] >=1:
                    have[10] -= 1
                    have[5] -= 1

                elif have[5] >=3:
                    have[5] -= 3
                else:
                    return False

        return True