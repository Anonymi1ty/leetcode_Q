"""
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？

输入：head = [4,2,1,3]
输出：[1,2,3,4]
"""

# 思路：
    # 1. 归并排序（题目要求时间空间复杂度分别为 O(nlogn) 和 O(1)，根据时间复杂度我们自然想到二分法，从而联想到归并排序；）
    # 2. 使用快慢指针找到中点，将链表分成两部分
        # 分割 cut 环节： 找到当前链表 中点，并从 中点 将链表断开（以便在下次递归 cut 时，链表片段拥有正确边界）；
            # 我们使用 fast,slow 快慢双指针法，奇数个节点找到中点，偶数个节点找到中心左边的节点。
            # 找到中点 slow 后，执行 slow.next = None 将链表切断。
            # 递归分割时，输入当前链表左端点 head 和中心节点 slow 的下一个节点 tmp(因为链表是从 slow 切断的)。
            # cut 递归终止条件： 当 head.next == None 时，说明只有一个节点了，直接返回此节点。
    # 3. 递归地对两部分进行排序
        # 双指针法合并，建立辅助 ListNode h 作为头部。
        # 设置两指针 left, right 分别指向两链表头部，比较两指针处节点值大小，由小到大加入合并链表头部，指针交替前进，直至添加完两个链表。
        # 返回辅助ListNode h 作为头部的下个节点 h.next。
        # 时间复杂度 O(l + r)，l, r 分别代表两个链表长度。
        
        # 当题目输入的 head == None 时，直接返回 None。
    
from typing import List, Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # 1. 分割 cut 环节
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 切断链表
        mid = slow.next
        slow.next = None

        # 2. 递归地对两部分进行排序
        left = self.sortList(head)
        right = self.sortList(mid)

        # 3. 合并两个已排序的链表
        return self.merge(left, right)
    
    def merge(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        h = ListNode(0)
        curr = h
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        curr.next = left if left else right
        return h.next