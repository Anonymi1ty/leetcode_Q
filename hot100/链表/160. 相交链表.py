"""
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。

"""

# 思路：
    # 遍历两个链表，记录第一个链表的每一个地址到set中
    # 如果第二个链表的节点在set中，说明相交了，返回该节点
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