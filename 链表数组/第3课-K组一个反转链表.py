## https://leetcode-cn.com/problems/reverse-nodes-in-k-group/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        tmp = head
        for _ in range(k):         # 判断从当前节点起，够不够k个节点   【递归的终止条件】
            if tmp == None:        # 不够则后续节点都不用变动
                return head
            tmp = tmp.next
            
        # 设置两个指针          # 经过上面的终止条件后，下面要做的就是将一段长度为k的链表反转
        p, rev = head, None   # 起始情况 rev   p      ➡       走一步后   rev   p 
        for _ in range(k):    #  None   p0->p1->...pk-1  None <- p0   p1->...pk-1
            rev, rev.next, p = p, rev, p.next # 最终指针p指向pk-1.next, 也就是下一段的入口
            # p现在是这一个小group的最后一个节点
        head.next = self.reverseKGroup(p, k)  # 进行递归             【递归入口】  
        return rev                 # rev恰好是原来长度为k的链表的末尾，也是当前这一段链表的头
    
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        tmp = head
        for _ in range(k):        
            if tmp == None:        
                return head
            tmp = tmp.next
            

        p, rev = head, None   
        for _ in range(k):    
            tmp = p.next
            p.next = rev
            rev = p
            p = tmp

        # 最开始的头结点将在翻转后在最后面
        head.next = self.reverseKGroup(p, k)  
        return rev   
    
# -------------------------------

class Solution:
    # 翻转一个子链表，并且返回新的头与尾
    # 类似翻转链表只不过这里的prev为原group的最后节点的下一个节点
    def reverse(self, head: ListNode, tail: ListNode):

        prev = tail.next
        p = head
        while prev != tail:

            nex = p.next
            p.next = prev
            prev = p
            p = nex
            
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # hair->1->2->3->4->5
        # k=2, 2->1->4->3->5
        # 1.即第一次执行
        
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            # 1.nex = 3
            nex = tail.next
            # 1.head=1, tail=2
            # 返回 2->1
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            # 1.hair->2->1
            pre.next = head
            # 1.hari->2->1->3
            tail.next = nex
            # 1.pre = 1
            pre = tail
            # 1.head = 3ß
            head = tail.next
        
        return hair.next
