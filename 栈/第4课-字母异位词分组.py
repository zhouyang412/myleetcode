"""
https://leetcode-cn.com/problems/group-anagrams/submissions/
https://leetcode-cn.com/problems/group-anagrams/solution/python-4xing-dai-ma-duo-chong-jie-fa-by-x62e3/

"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = {}
        strs_list = []
        n = 0
        
        for str_ in strs:
            # 字符串排序后进行hash
            str_sorted = str(sorted(str_))
            # 用n记录当前hash的字符串的在list中的下标
            if str_sorted not in strs_dict:
                strs_dict[str_sorted] = n
                strs_list.append([])
                n += 1
            strs_list[strs_dict[str_sorted]].append(str_)
                
        return strs_list