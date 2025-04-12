"""
给定一个二叉树，判断它是否是 平衡二叉树 （左右子树高度不能相差超过 1 ） 

示例：
输入：root = [3,9,20,null,null,15,7]
输出：true
"""

# 思路：后序遍历，底层高度为0开始递归，但是加上height的检查条件

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def post_order(node):
            if not node:
                return 0 #递归结束条件，当没有node后返回树的高度为0
            
            left_height = post_order(node.left)
            
            if left_height == -1:
                return -1  # 左子树不平衡，直接返回 -1
            right_height = post_order(node.right)
            if right_height == -1:
                return -1 # 右子树不平衡，直接返回 -1
            
            # 如果当前节点左右子树高度差大于 1，则不平衡
            if abs(left_height - right_height) > 1:
                return -1
            return  max(left_height, right_height) + 1
        return post_order(root) != -1
        
        
