"""
    https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/
    https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/solution/589ncha-shu-de-qian-xu-bian-li-by-821218213/
    

"""
# 前序
# 递归

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        res = [root.val]
        for node in root.children:
            res.extend(self.preorder(node))
        return res
    
# white, gray

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        white, gray = 0, 1
        stack = [(white, root)]
        res = []

        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == white:
                for c in reversed(node.children):
                    stack.append((white, c))
                stack.append((gray, node))
            else:
                res.append(node.val)
        return res
    
    
# 后序遍历
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []

        res = []
        for node in (root.children):
            res.extend(self.postorder(node))
        res.append(root.val)
        return res
    
    
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        white, gray = 0, 1
        res = []
        stack = [(white, root)]

        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == white:
                stack.append((gray, node))
                for c in reversed(node.children):
                    stack.append((white, c))
            else:
                res.append(node.val)

        return res

    
   
# 通用模板
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# N叉树简洁递归
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        res = [root.val]
        for node in root.children:
            res.extend(self.preorder(node))
        return res



# N叉树通用递归模板
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def helper(root):
            if not root:
                return
            res.append(root.val)
            for child in root.children:
                helper(child)
        helper(root)
        return res



# N叉树迭代方法
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        s = [root]
        # s.append(root)
        res = []
        while s:
            node = s.pop()
            res.append(node.val)
            # for child in node.children[::-1]:
            #     s.append(child)
            s.extend(node.children[::-1])
        return res

 
