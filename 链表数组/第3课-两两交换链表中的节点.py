## https://leetcode-cn.com/problems/swap-nodes-in-pairs/
## 题解：https://leetcode-cn.com/problems/swap-nodes-in-pairs/solution/bi-jiao-zhi-jie-gao-xiao-de-zuo-fa-han-tu-jie-by-w/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        pre = ListNode(-1)
        pre.next = head
        cur = pre

        while cur.next and cur.next.next:
            a, b = cur.next, cur.next.next
            cur.next = b
            a.next = b.next
            b.next = a
            cur = cur.next.next
        return pre.next