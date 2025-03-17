# 题目：
"""
给定一个头节点为 head 的链表用于记录一系列核心肌群训练项目编号，请查找并返回倒数第 cnt 个训练项目编号。

示例 1：

输入：head = [2,4,7,8], cnt = 1
输出：8
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def trainingPlan(self, head: Optional[ListNode], cnt: int) -> Optional[ListNode]:
        # temp = []
        # while head:
        #     temp.insert(0, head)
        #     head = head.next
        # return temp[cnt - 1]
        res = deque()
        while head:
            res.append(head)
            head = head.next
        return res[-cnt]