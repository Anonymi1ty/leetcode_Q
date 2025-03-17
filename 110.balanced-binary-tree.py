#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 平衡二叉树：左右子树的高度差不超过1
    #递归写法：1.左边是平衡二叉树，2.右边是平衡二叉树，3.且左右子树的高度差不超过1
    
# 返回类型定义,高度和是否平衡都是要使用的
class return_type:
    def __init__(self, height, is_balance):
        self.height = height
        self.is_balance = is_balance
        
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #调用process函数
        return self.process(root).is_balance
        
    #写一个返回值是return_type的处理函数
    def process(self, root) -> return_type:
        #递归终止条件
        if root is None:
            return return_type(0, True)
        # 递归左子树
        left = self.process(root.left)
        # 递归右子树
        right = self.process(root.right)
        # 高度是左右子树的最大值+1,+1指的是当前节点
        height = max(left.height, right.height) + 1
        # 判断左右子树是否平衡
        is_balance = left.is_balance and right.is_balance and abs(left.height - right.height) < 2
        return return_type(height, is_balance)
# @lc code=end

