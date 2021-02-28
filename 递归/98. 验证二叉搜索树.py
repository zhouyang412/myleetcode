"""
    https://leetcode-cn.com/problems/validate-binary-search-tree/
    https://leetcode-cn.com/problems/validate-binary-search-tree/solution/yan-zheng-er-cha-sou-suo-shu-by-leetcode-solution/
    
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def helper(root, lower=float('-inf'), upper=float('inf')):
            if root is None:
                return True

            val = root.val
            if val <= lower or val >= upper:
                return False
            # 若当前val大于lower，则若是一颗正常的二叉搜索树，他的右节点毕竟也大于当前下界
            # 而如果是一颗正常的二叉搜索树，右子树的值需要大于当前节点，所以改变下界为当前节点
            if not helper(root.right, lower=val, upper=upper):
                return False

            if not helper(root.left, lower=lower, upper=val):
                return False

            return True

        return helper(root)