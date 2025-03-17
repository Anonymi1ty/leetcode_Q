#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 1. 使用哈希表，遍历链表，如果有环，一定会重复访问某个节点
# 2.用快慢指针，如果有环，快指针一定会追上慢指针
    #重要数学推导：快指针追上慢指针，快指针返回到起点，改为每次走一步，再次相遇的地方就是环的起点
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None or head.next.next == None:
            return False
        # 设定快慢指针，初始点没在0点是因为while循环里面的判断条件，如果在0点返回值就不是环开始点了
        fast = head.next.next
        slow = head.next        
        while slow != fast:
            if fast.next == None or fast.next.next == None:
                return False
            # 快指针每次走两步，慢指针每次走一步
            fast = fast.next.next
            slow = slow.next
        return True
# @lc code=end

