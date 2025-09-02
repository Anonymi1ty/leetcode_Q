"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
"""

# 思路：
    #  使用双指针法，比较两个链表的当前节点值，将较小的节点连接到新链表中，然后移动指针
    #  最后将剩余的链表连接到新链表的尾部


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 创建一个虚拟头节点，方便处理边界情况
        # tail指针用于构建新链表，new_head用于返回
        new_head = tail = ListNode(0)

        # 遍历两个链表，直到一个链表为空
        while list1 and list2:
            if list1.val < list2.val:
                # l1节点的值较小，将l1节点连接到tail
                tail.next = list1
                list1 = list1.next
            else:
                # l2节点的值较小或相等，将l2节点连接到tail
                tail.next = list2
                list2 = list2.next
            # 更新tail指向新添加的节点
            tail = tail.next

        # 如果有一个链表还有剩余节点，直接连接到tail后面
        tail.next = list1 if list1 else list2

        # 返回新链表的头节点，跳过虚拟头节点
        return new_head.next
