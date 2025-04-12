"""
给定一个二叉树 root ，返回其最大深度。

二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。

示例：
输入：root = [3,9,20,null,null,15,7]
输出：3
"""

# 思路：DFS深度优先遍历（不用回溯）
    # 可以将最底层记录为1，反向算最顶层的大小

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def DFS(node):
            if not node:
                return 0
            # 分别计算左右子树的深度，然后取最大值加1
            left_depth = DFS(node.left)
            right_depth = DFS(node.right)
            return max(left_depth, right_depth) + 1
        return DFS(root)
        
        
