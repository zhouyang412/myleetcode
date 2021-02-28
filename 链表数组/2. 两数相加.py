"""
    https://leetcode-cn.com/problems/add-two-numbers/
    https://leetcode-cn.com/problems/add-two-numbers/solution/zui-zhi-bai-de-xie-fa-by-meng-zhi-hen-n-2/
    https://leetcode-cn.com/problems/add-two-numbers/solution/hua-jie-suan-fa-2-liang-shu-xiang-jia-by-guanpengc/

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # pre始终指向0节点，cur会变动
        cur = pre = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            # 较短的链表将被补0
            if l1:
                l1_value = l1.val
            else:
                l1_value = 0

            if l2:
                l2_value = l2.val
            else:
                l2_value = 0
            
       
            s = l1_value + l2_value + carry
            # 下一个链表的值为当前和取余
            cur.next = ListNode(s % 10)
            cur = cur.next
            # 进位数为当前值除以10取正
            carry = s // 10

            if l1:
                l1 = l1.next
            else:
                l1 = None

            if l2:
                l2 = l2.next
            else:
                l2 = None

        return pre.next