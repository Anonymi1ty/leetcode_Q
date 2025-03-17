#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1.思路是将链表遍历放入栈内（先入后出，逆序），然后再遍历链表，与栈内元素比较，如果有不相等的元素则返回False，否则返回True
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         stack = []
#         # cur表示当前节点
#         cur = head
#         while cur:
#             stack.append(cur.val)
#             cur = cur.next
#         # 重新遍历链表
#         cur = head
#         while cur:
#             if cur.val != stack.pop():
#                 return False
#             cur = cur.next
#         return True

# 2.限制空间复杂度为O(1)：找到链表的中点，将后半部分反转，然后比较前半部分和后半部分是否相等，记得标记第一个点和最后一个点
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        slow = fast = head
        # 慢指针先走，找到中点
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # 反转后半段链表，使用双指针，temp保存
        pre = None
        # 当前指针移动到slow的下一个节点
        cur = slow.next
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        # 比较前半段和后半段是否相等(上述内容结束后，pre指向最后一个节点)
        while pre:
            if head.val != pre.val:
                return False
            head = head.next
            pre = pre.next
        return True
        
# @lc code=end

