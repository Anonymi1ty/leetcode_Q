"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
"""

# 思路：
    # 1. 双指针,快指针先走 n 步
    # 2. 然后慢指针和快指针一起走，直到快指针到达链表末尾
    # 3. 此时慢指针正好指向要删除的节点

    
from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 添加虚拟头节点，方便写for循环和处理删除头节点的情况
        dummy = ListNode(0, head) # 创建一个值为 0 的新链表节点，这个节点的 next 指针指向 head（即原链表的头结点）
        slow, fast = dummy, dummy
        for _ in range(n + 1): # 添加了虚拟头节点，所以需要走 n + 1 步
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        # 删除慢指针的下一个节点
        slow.next = slow.next.next
        return dummy.next # 返回头节点

