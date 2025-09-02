"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
"""

# 思路：
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        while head:
            temp = head.next
            # 头插法
                # 当前结点下一个节点指向空(作为新链表的尾结点)
            head.next = new_head
                # new_head指向当前结点
            new_head = head
                # head 更新，向右移动到head.next
            head = temp
        return new_head
        