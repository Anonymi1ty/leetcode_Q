# 题目：
"""
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
返回删除后的链表的头节点。

示例 1:

输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        # 设置一个指针,用来储存前一个的地址
        pre, cur = head, head.next
        # 循环找目标值
        while cur and cur.val != val:
            pre, cur = cur, cur.next
        # 找到后将前一个和后一个连起来
        if cur:
            pre.next = cur.next
        return head