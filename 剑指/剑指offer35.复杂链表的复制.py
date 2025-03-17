# 题目：
"""
给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。

构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。

例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random --> y 。

返回复制链表的头节点。

用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：

val：一个表示 Node.val 的整数。
random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
你的代码 只 接受原链表的头节点 head 作为传入参数。
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# 思路：拼接+拆分。考虑构建原节点 1 -> 新节点 1 -> 原节点 2 -> 新节点 2 -> …… 的拼接链表；
    # 如此便可在访问原节点的 random 指向节点的同时找到新对应新节点的 random 指向节点。
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # 1. 复制各节点，并构建拼接链表
        cur = head
        while cur:
            # 复制节点
            new_node = Node(cur.val)
            # new_node的next指向cur的next
            new_node.next = cur.next
            # cur的next指向new_node
            cur.next = new_node
            # 移动到下一个节点
            cur = new_node.next
        
        # 2. 构建各新节点的 random 指向
        cur = head
        while cur:
            # 获取random的指向节点
            temp = cur.random
            # 新节点的random指向random的指向节点的下一个（复制的random节点）
            if not temp:
                cur.next.random = temp
            else:
                cur.next.random = temp.next
            # 移动到下一个原节点
            cur = cur.next.next
        
        #3. 去掉原节点
        new_head = head.next
        cur = head
        while cur:
            temp = cur.next      # 新节点
            cur.next = temp.next # 恢复原链表
            if temp.next:
                temp.next = temp.next.next  # 建立新链表的连接
            cur = cur.next #到原有链表的下一个上面
        return new_head