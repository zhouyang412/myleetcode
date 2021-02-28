"""
    https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
    https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/xiong-mao-shua-ti-python3-xian-xu-zhao-gen-hua-fen/

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        if not preorder and not inorder: return 

        root = TreeNode(preorder[0])
        root_idx = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1: root_idx+1], inorder[: root_idx])
        root.right = self.buildTree(preorder[root_idx+1: ], inorder[root_idx+1: ])

        return root