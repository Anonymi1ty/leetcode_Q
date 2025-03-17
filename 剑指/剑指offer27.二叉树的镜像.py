"""
给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点
"""

# 思路：直接拷贝

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #  当节点 root 为空时（即越过叶节点）,递归结束条件
        if not root: 
            return
        
        new_root = TreeNode(root.val)
        new_root.left = self.invertTree(root.right)
        new_root.right = self.invertTree(root.left)
        return new_root

            
            
        