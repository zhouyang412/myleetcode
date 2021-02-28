# #https://leetcode-cn.com/problems/linked-list-cycle/

"""
1.暴力：利用哈希表和set，记录访问过的所有节点放在set里，在遍历的过程中发现出现在set里那就是有环
2.快慢指针：链表中常用的方法，快慢指针重合就是有环
工程中不太会出现

"""

#暴力解法：
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        temp = dict()
        cur = head
        while cur:
            if cur in temp:
                return True
            else:
                temp[cur] = 1
                cur = cur.next
        return False
    
    
# 快慢指针
"""
快慢指正从第二步开始始终相差一格
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next
        # 若没有环 最后将指向null
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
            
        return False