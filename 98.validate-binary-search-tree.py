#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 1.搜索二叉树问题，使用中序遍历，判断是否是升序排列，并且没有重复元素
# 2.使用递归解法：1)左右树都是搜索二叉树 2)左边最大值不大于结点，右边最小值不小于结点 3)结束条件：x == None, return None
class Solution:
    def in_order(self, root, result):
        if root is None:
            return
        self.in_order(root.left, result)
        result.append(root.val)
        self.in_order(root.right, result)
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = []
        self.in_order(root, result)
        # 判断是否是升序排列，并且没有重复元素
        for i in range(1, len(result)):
            if result[i-1] >= result[i]:
                return False
        return True
        
# @lc code=end

