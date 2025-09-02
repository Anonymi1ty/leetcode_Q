"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。 

输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
"""

# 思路：
    # 1. 初始化一个虚拟头节点和一个游标指针，用于构建结果链表
    # 2. 使用一个进位变量来处理两位数相加的情况
    # 3. 遍历两个链表，逐位相加，并更新进位
    

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 创建虚拟头节点，方便最后返回结果
        dummy = ListNode(0)
        curr = dummy     # 游标，用于构建结果链表
        carry = 0        # 进位标志，初始 0
        
        # 当两个链表还有节点或有进位时，继续处理
        while l1 or l2 or carry:
            # 取当前位的值，若对应链表已遍历完则视为 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # 计算本位和，并更新进位
            total = v1 + v2 + carry
            carry = total // 10      # 新的进位（0 或 1）
            digit = total % 10       # 本位结果
            
            # 创建新节点并接到结果链表
            curr.next = ListNode(digit)
            curr = curr.next
        
            # 推进 l1 和 l2
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # 返回跳过虚拟头的实际结果链表
        return dummy.next

            
                