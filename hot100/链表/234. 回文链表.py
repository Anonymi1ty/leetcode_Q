"""
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。

输入：head = [1,2,2,1]
输出：true
"""

# 思路：


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        record = []
        while head:
            record.append(head.val)
            head = head.next
        # 判断 record 是否为回文：将 record 反转后与原列表比较，相等则为回文
            # record[::-1]：这是 Python 的切片语法，表示将 record 列表倒序
        return record == record[::-1]
        