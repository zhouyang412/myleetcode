"""
    https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
    https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/236-er-cha-shu-de-zui-jin-gong-gong-zu-xian-hou-xu/

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == q or root == p or not root:
            return root

        left = self.lowestCommonAncestor(root.left ,p ,q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left and not right:
            return 
        if not left:
            return right
        if not right:
            return left
        return root

