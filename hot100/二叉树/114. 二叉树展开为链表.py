"""
给你二叉树的根结点 root ，请你将它展开为一个单链表：

展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。
 

示例 1：


输入：root = [1,2,5,3,4,null,6]
输出：[1,null,2,null,3,null,4,null,5,null,6]
"""

# 思路：先序遍历树；res = []; res.append(node); node.left = None; node.right = res[i+1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 先序遍历树
        def preorder(node):
            if not node:
                return []
            # 先序遍历
            return [node] + preorder(node.left) + preorder(node.right)

        # 获取先序遍历结果
        nodes = preorder(root)
        # 重新链接成链表
        for i in range(len(nodes) - 1):
            nodes[i].left = None
            nodes[i].right = nodes[i + 1]
        if nodes:
            nodes[-1].left = None
            nodes[-1].right = None
        return root