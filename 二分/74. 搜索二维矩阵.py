"""
    https://leetcode-cn.com/problems/search-a-2d-matrix/
    https://leetcode-cn.com/problems/search-a-2d-matrix/solution/er-fen-cha-zhao-ji-bai-9977-by-yi-wen-statistics/
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if matrix is None: return False

        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m * n - 1

        while left <= right:

            mid = int((left + right) / 2)

            mid_row = mid // n
            mid_col = mid % n
            mid_val = matrix[mid_row][mid_col]

            if mid_val == target:
                return True
            if mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
