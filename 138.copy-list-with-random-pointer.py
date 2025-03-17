#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# 使用哈希表存储原节点和新节点的映射关系，然后再遍历链表，将新节点的next和random指针指向新节点
# 也可以不使用哈希表，将复制节点存在原节点的后面，然后再遍历链表，将新节点的random指针指向新节点的random指针的next（跟哈希表原理一样）
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # 哈希表存储原节点和新节点的映射关系
        Map = {}
        cur = head
        # 遍历链表，将新节点的next和random指针指向新节点
        while cur:
            # 在字典上存储 key=cur节点 和value =cur的新Node
            Map[cur] = Node(cur.val)
            cur = cur.next
        # 再次遍历，拷贝关系
        cur = head
        while cur:
        # cur是老节点
        # Map.get(cur)是新节点
            # 新节点的next值，是老节点下一个的哈希值
            if cur.next:
                Map[cur].next = Map[cur.next]
            # 新节点的rand值，是老节点rand对应的哈希值
            if cur.random:
                Map[cur].random = Map[cur.random]
            cur = cur.next
        return Map[head]
# @lc code=end

