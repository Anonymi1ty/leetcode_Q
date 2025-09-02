"""
给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置
（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

不允许修改 链表。

输入：head = [3,2,0,-4]
输出：1 (解释：链表中有一个环，其尾部连接到第二个节点。)
"""

# 思路：
    # 使用快慢指针,当快指针追上慢指针的时候，在开头放入慢指针，相遇就是入口


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # 1) 找相遇点
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            # fast 到头了，无环
            return None

        # 2) 找入环点
        ptr = head
        while ptr != slow:
            ptr = ptr.next
            slow = slow.next

        return ptr
