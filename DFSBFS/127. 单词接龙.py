"""
    https://leetcode-cn.com/problems/word-ladder/description/
    https://leetcode-cn.com/problems/word-ladder/solution/python3-bfshe-shuang-xiang-bfsshi-xian-dan-ci-jie-/
    https://leetcode-cn.com/problems/word-ladder/solution/python-shen-du-jiang-jie-bfsde-jie-gou-by-allen-23/
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        import string

        if endWord not in wordList: return 0
        wordList = {i:1 for i in wordList}
        queue = [(beginWord, 1)]

        while queue:
            word, step = queue.pop(0)

            if word == endWord:
                return step
            
            for idx, c in enumerate(word):
                for w in string.ascii_lowercase:
                    if w == c:
                        continue
                    search_c = word[: idx] + w + word[idx+1: ] 
                    if search_c in wordList:
                        queue.append((search_c, step+1))
                        wordList.pop(search_c)

        return 0