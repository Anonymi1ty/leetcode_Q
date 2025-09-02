"""
给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

输入：head = [1,2,3,4]
输出：[2,1,4,3]
"""

# 思路：
    # 1. 使用递归来交换每一对节点
    # 2. 递归的终止条件是当前节点或下一个节点为空

    
from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
	def swapPairs(self, head):
		# 递归的终止条件
		if not head or not head.next:
			return head
		# 假设链表是 1->2->3->4
		# 这句就先保存节点2
		new_head = head.next
		# 继续递归，处理节点3->4
		# 当递归结束返回后，就变成了4->3
		# 于是head节点就指向了4，变成1->4->3
		head.next = self.swapPairs(new_head.next)
		# 将2节点指向1
		new_head.next = head
		return new_head