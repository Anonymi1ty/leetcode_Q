"""
将一个 二叉搜索树 就地转化为一个 已排序的双向循环链表 。
    “二叉搜索树”:其左子树所有节点的键值都小于该节点的键值，而右子树所有节点的键值都大于该节点的键值。
对于双向循环列表，你可以将左右孩子指针作为双向循环链表的前驱和后继指针，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

特别地，我们希望可以 就地 完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中最小元素的指针。
"""

# 思路：中序遍历；并且构成双向循环链表（提前存储head，并且存储pre；当前节点是pre的right,当前节点的left是pre；最后首尾相连）

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None

        # head 指向链表最小节点（即中序遍历的第一个节点）
        # prev 用来记录中序遍历过程中上一个处理的节点
        self.head = None
        self.prev = None

        # 定义中序遍历递归函数
        def inOrder(node: 'Node'):
            if not node:
                return
            inOrder(node.left)
            # 处理当前节点
            if self.prev:
                # 连接上一个节点和当前节点
                self.prev.right = node
                node.left = self.prev
            else:
                # 第一个节点即为链表头部
                self.head = node
            # 将当前节点转化为前一个节点
            self.prev = node
            inOrder(node.right)

        # 执行中序遍历
        inOrder(root)
        # 使链表成循环：头节点的左指针指向尾节点，尾节点的右指针指向头节点
        self.head.left = self.prev
        self.prev.right = self.head

        return self.head
