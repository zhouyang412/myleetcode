"""
    https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
    https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/solution/hua-jie-suan-fa-104-er-cha-shu-de-zui-da-shen-du-b/
    https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/solution/er-cha-shu-de-zui-da-shen-du-by-leetcode-solution/
    
    节点为空时说明高度为 0，所以返回 0；节点不为空时则分别求左右子树的高度的最大值，同时加1表示当前节点的高度，返回该数值.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        left_count = self.maxDepth(root.left)
        right_count = self.maxDepth(root.right)
        # 1表示当前节点层
        return max(left_count, right_count) + 1