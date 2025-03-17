# 题目：
"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例 1：

输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def trainningPlan(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 创建一个新的虚拟头节点和一个指针指向它,如果不要头结点的指针，在逻辑上会有漏洞（比如第一次和第二次）
        new_head = tail = ListNode(0)

        # 遍历两个链表，直到一个链表为空
        while l1 and l2:
            if l1.val < l2.val:
                # l1节点的值较小，将l1节点连接到tail
                tail.next = l1
                l1 = l1.next
            else:
                # l2节点的值较小或相等，将l2节点连接到tail
                tail.next = l2
                l2 = l2.next
            # 更新tail指向新添加的节点
            tail = tail.next

        # 如果有一个链表还有剩余节点，直接连接到tail后面
        tail.next = l1 if l1 else l2

        # 返回新链表的头节点，跳过虚拟头节点
        return new_head.next
