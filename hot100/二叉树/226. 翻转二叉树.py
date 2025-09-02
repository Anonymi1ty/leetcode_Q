"""
给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。

 

示例 1：

输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
"""

# 思路：

    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #  当节点 root 为空时（即越过叶节点）,递归结束条件
        if not root: 
            return
        new_root = TreeNode(root.val)
        new_root.left = self.invertTree(root.right)
        new_root.right = self.invertTree(root.left)
        return new_root
        