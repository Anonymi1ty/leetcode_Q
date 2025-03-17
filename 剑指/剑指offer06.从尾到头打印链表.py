"""
书店店员有一张链表形式的书单，每个节点代表一本书，节点中的值表示书的编号。为更方便整理书架，店员需要将书单倒过来排列，就可以从最后一本书开始整理，逐一将书放回到书架上。请倒序返回这个书单链表。

 

示例 1：

输入：head = [3,6,4,1]

输出：[1,4,6,3]

"""



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# 思路：使用deque即可，遍历的时候从左边插入即可
from collections import deque

class Solution:
    def reverseBookList(self, head: Optional[ListNode]) -> List[int]:
        res = deque()
        while head:
            res.appendleft(head.val)
            head = head.next
        return list(res)

            
