"""
    https://leetcode-cn.com/problems/reverse-linked-list-ii/
    https://leetcode-cn.com/problems/reverse-linked-list-ii/solution/fan-zhuan-lian-biao-ii-by-leetcode/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        if not head:
            return None

        cur, prev = head, None
        # 循环结束prev将指向m之前位置的节点,cur将指向第m个位置的节点
        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m - 1, n - 1

        # tail将指向第m个节点,con指向m之前一个节点
        tail, con = cur, prev

        # cur在开始的时候指向第m个节点,最终将指向原链表第m+1个节点
        # prev在循环结束后指向原来第n个节点
        while n:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1
        
        # 原来第m-1个节点指向原来第n个节点
        # 如果m==1,那么head就是翻转后的链表的头节点
        if con:
            con.next = prev
        else:
            head = prev
        # 原来第m个节点指向原来第m+1个节点
        tail.next = cur
        return head





        
        
        
            

                