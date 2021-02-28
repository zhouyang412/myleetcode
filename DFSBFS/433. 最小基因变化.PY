"""
    https://leetcode-cn.com/problems/minimum-genetic-mutation/#/description
    https://leetcode-cn.com/problems/minimum-genetic-mutation/solution/shen-du-you-xian-yan-du-you-xian-shuang-xiang-yan-/
"""
# BFS：

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1

        change_map = {
            "A": "CGT",
            "C": "AGT",
            "G": "CAT",
            "T": "CGA",
        }

        queue = [(start, 0)]

        while queue:
            node, step = queue.pop(0)

            if node == end:
                return step

            # 遍历当前步的字符串，将每一个可修改的且存在在bank里的字符串添加到队列中
            # 队列中,越往左，修改的步数越小
            for i, s in enumerate(node):
                for c in change_map[s]:
                    new = node[:i] + c + node[i+1:]
                    if new in bank:
                        queue.append((new, step+1))
                        bank.remove(new)
        return -1

    
    
# DFS：

class Solution:

    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1

        change_map = {
            "A": "CGT",
            "C": "AGT",
            "G": "CAT",
            "T": "CGA",
        }

        min_count = len(bank) + 1

        def dfs(current, count, current_bank):
            # 只作用于嵌套作用域，而且只是作用在函数里面
            nonlocal min_count

            # terminator
            # 当前count大于之前的最小改变数
            if count > min_count:
                return
            # 当前字符串已经和end相等
            if current == end:
                if count < min_count:
                    min_count = count
                return
            # 基因库已为空
            if not current_bank:
                return

            # process
            for i, s in enumerate(current):
                for char in change_map[s]:
                    new = current[:i] + char + current[i + 1:]
                    if new not in current_bank:
                        continue
                    current_bank.remove(new)
                    # drill down
                    dfs(new, count + 1, current_bank)

                    # reverse state
                    # 这里之前将new删除，但是仅在当前状态下删除
                    # 其余状态不应该受到影响，这里需要将删除的元素加回来

                    current_bank.add(new)

        dfs(start, 0, bank)

        return min_count if min_count <= len(bank) else -1

