"""
    https://leetcode-cn.com/problems/reorder-list/
    https://leetcode-cn.com/problems/reorder-list/solution/zhong-pai-lian-biao-by-leetcode-solution/
    
    1.链表不能直接用下标访问，先遍历链表，将节点有顺序的放在list中，再利用双指针即可
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return 

        node_list = []
        node = head
        while node:
            node_list.append(node)
            node = node.next

        i, j = 0, len(node_list) - 1
        while i < j:
            tmp = node_list[i].next
            node_list[i].next = node_list[j]
            # 此时的i指向下一个节点
            i = i + 1
            # 若此时相遇则跳出
            if i == j:
                break
            node_list[j].next = tmp
            j = j - 1

        node_list[i].next = None
