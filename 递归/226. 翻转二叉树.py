"""
    https://leetcode-cn.com/problems/invert-binary-tree/
    https://leetcode-cn.com/problems/invert-binary-tree/solution/fan-zhuan-er-cha-shu-by-leetcode-solution/
    https://leetcode-cn.com/problems/invert-binary-tree/solution/dong-hua-yan-shi-liang-chong-shi-xian-226-fan-zhua/
    
    将递归到叶子节点，先从叶子节点开始反转，然后往上回溯，直到root节点

"""




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return 

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left, root.right = right, left
        return root