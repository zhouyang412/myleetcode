"""
    https://leetcode-cn.com/problems/n-queens/
    https://leetcode-cn.com/problems/n-queens/solution/liang-chong-shi-xian-xiang-xi-tu-jie-51-n-huang-ho/
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n < 1: return []

        self.result = []
        # 分别代表当前列，左45度斜线，右45度斜线
        self.cols, self.pie, self.na = set(), set(), set()
        self.DFS(n, 0, [])
        return self._generate_result(n)

    def DFS(self, n, row, cur_state):
        # n为棋盘尺寸
        # cur_state=[[1,3,0,2], [2,0,3,1]]
        # 列表下标代表row,对应元素值代表对应行皇后放置的位置下标
        if row >= n:
            self.result.append(cur_state)
            return 
        # 在当前层 遍历所有列
        for col in range(n):
            
            # 当前列若已经放置了一个皇后则当前列不可再放置
            # 当前位置的row + col 跟左45度斜线上的值都相等 --> y = x (y=-row, x=col) --> col + row = 0
            # 当前位置的row - col 跟右45度斜线上的值都相等 --> y = -x --> -row=-col --> row - col = 0
            if col in self.cols or row + col in self.pie or row - col in self.na:
                continue
            self.cols.add(col)
            self.pie.add(row + col)
            self.na.add(row - col)
            self.DFS(n, row + 1, cur_state + [col])
            # 把当前层当前列改变的状态给去除，否则会影响下一个列的结果
            self.cols.remove(col)
            self.pie.remove(row + col)
            self.na.remove(row - col)

    def _generate_result(self, n):
        board = []
        print(self.result)
        for res in self.result:
            for i in res:
                board.append("." * i + "Q" + "." * (n-i-1))

        return [board[i: i + n] for i in range(0, len(board), n)] 
    
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p == n:
                result.append(queens)
                return None

            # q-->col p-->row
            for q in range(n):
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                    DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])
        result = []
        DFS([], [], [])
        return [["."*i + "Q" + "."*(n-i-1)for i in sol] for sol in result]
