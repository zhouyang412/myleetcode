"""
    https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/
    https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/solution/ncha-shu-de-ceng-xu-bian-li-python3yan-du-you-xian/
    
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        queue = [root]
        res = []
        while queue:
            # 先从左往右的输出当前层的节点值
            res.append(node.val for node in queue)
            # 更新队列，先从左往右遍历queue中的节点，再遍历从左往右遍历节点的孩子节点
            queue = [child for node in queue for child in node.children]
        return res