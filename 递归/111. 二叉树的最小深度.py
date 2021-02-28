"""
    https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
    https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/solution/leetcode111di-gui-jie-jue-by-yimingen/
    相比于最大深度，最小深度需要对0做一些处理和区分。

"""

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root : return 0
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)
        childDepth = min(leftDepth, rightDepth) if leftDepth and rightDepth else leftDepth or rightDepth
        return 1 + childDepth

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:

        if root is None:
            return 0

        left_count = self.minDepth(root.left)
        right_count = self.minDepth(root.right)

        if left_count and right_count:
            return min(left_count, right_count) + 1
        if left_count or right_count:
            if left_count:
                return left_count + 1
            else:
                return right_count + 1
                
        if not left_count and not right_count:
            return 1
