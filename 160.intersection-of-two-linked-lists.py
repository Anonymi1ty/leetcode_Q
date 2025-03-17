#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 1. 使用哈希表，将一个链表的节点存入哈希表，再遍历另一个链表，如果有相同节点，就是交点
# 2. 分别遍历两个链表，记录长度，和两个链表最后的节点，如果不一样一定不相交
    # 如果一样，长的链表先走差值步，再一起走，相遇的地方就是交点
#3. 如果存在环，先参考141题，使用快慢指针，最后返回环的起点
    # 之后再判断两个链表是否相交，如果相交，返回相交的节点
        # 情况1：在环外面相交，使用下述代码
        # 情况2：在环内相交，跑一遍环，检查是否有环2的起点，如果有环内相交，没有不相交
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cur1 = headA
        cur2 = headB
        lena = 0
        lenb = 0
        # cur1.next作为循环条件可以使cur1指向最后一个节点
        while cur1.next:
            lena += 1
            cur1 = cur1.next
        while cur2.next:
            lenb += 1
            cur2 = cur2.next
        # 如果两个链表最后一个节点不一样，一定不相交
        if cur1 != cur2:
            return None
        # 如果两个链表最后一个节点一样，重新指向头节点
        cur1 = headA
        cur2 = headB
        # 长的链表先走差值步
        if lena > lenb:
            for _ in range(lena - lenb):
                cur1 = cur1.next
        else:
            for _ in range(lenb - lena):
                cur2 = cur2.next
        # 比较两个链表的节点，相等就是交点
        while cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1
        
# @lc code=end

