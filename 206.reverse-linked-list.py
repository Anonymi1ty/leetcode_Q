#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #定义一个新的ListNode,无头结点（也可以理解成插入一个none的指针）
        new_head = None
        #遍历链表
        while head:
            #将head的下一个节点保存到temp中
            temp = head.next
            #头插法，将head插入到new_head的前面
            head.next = new_head
            # 更新头结点new_head,指向第一个节点及head
            new_head = head
            # 更新原链表的头结点，head=head.next
            head = temp
        return new_head
        
# @lc code=end

