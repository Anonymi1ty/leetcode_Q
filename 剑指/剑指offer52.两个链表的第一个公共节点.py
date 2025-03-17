"""
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
"""

    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 思路：使用哈希表，将一个链表的节点存入哈希表，再遍历另一个链表，如果有相同节点，就是交点
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        list = set()
        while headA:
            list.add(headA)
            headA = headA.next
        while headB:
            if headB in list:
                return headB
            headB = headB.next
        return None
        