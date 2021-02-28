"""
    https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
    https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/er-cha-shu-de-zhong-xu-bian-li-by-leetcode-solutio/
    https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/
    https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/pythongai-bian-yi-xing-dai-ma-shi-xian-er-cha-shu-/

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
使用颜色标记节点的状态，新节点为白色，已访问的节点为灰色。
如果遇到的节点为白色，则将其标记为灰色，然后将其右子节点、自身、左子节点依次入栈。
如果遇到的节点为灰色，则将节点的值输出。

按照访问左子树——根节点——右子树的方式遍历这棵树，而在访问左子树或者右子树的时候我们按照同样的方式遍历，直到遍历完整棵树。因此整个遍历过程天然具有递归的性质，我们可以直接用递归函数来模拟这一过程。

入栈方式是右中左， 出栈为 左中右
"""
# 前序遍历 中左右
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        white, gray = 0, 1

        res = []
        stack = [(white, root)]

        while stack:
            color, node = stack.pop()
            if node is None: continue

            if color == white:
                stack.append((white, node.right))
                stack.append((white, node.left))
                stack.append((gray, node))
            else:
                res.append(node.val)
        return res



# 中序遍历 左中右
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        white, gray = 0, 1
        res = []
        stack = [(white, root)]
        
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == white:
                stack.append((white, node.right))
                stack.append((gray, node))
                stack.append((white, node.left))
            else:
                res.append(node.val)
                
        return res
                
# 后序遍历 左右中
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        white, gray = 0, 1
        res = []
        stack = [(white, root)]
        
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == white:
                stack.append((gray, node))
                stack.append((white, node.right))
                stack.append((white, node.left))
            else:
                res.append(node.val)
                
        return res

             
                
# 递归
# 前序
def __init__(self):
    self.out = []


def preorderTraversal(self, root):
    if root is None: return []
    self.out.extend([root.val])
    self.preorderTraversal(root.left)
    self.preorderTraversal(root.right)
    return self.out


# 中序
def __init__(self):
    self.out = []


def inorderTraversal(self, root):
    if root is None: return [] 
    self.inorderTraversal(root.left)
    self.out.extend([root.val])
    self.inorderTraversal(root.right)
    return self.out


# 后序
def __init__(self):
    self.out = []


def postorderTraversal(self, root):
    if root is None: return []
    self.postorderTraversal(root.left)
    self.postorderTraversal(root.right)
    self.out.extend([root.val])
    return self.out
