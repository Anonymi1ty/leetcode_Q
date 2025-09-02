"""
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：

节点的左子树只包含 严格小于 当前节点的数。
节点的右子树只包含 严格大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
 

示例 1：


输入：root = [2,1,3]
输出：true
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归检验（左子树小，右子树大，通过设置上下界进行验证）
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower = float('-inf'), upper = float('inf')) -> bool:
            # NULL也是可以接受的
            if not node:
                return True
            
            val = node.val
            if val <= lower or val >= upper:
                return False
            
            # 判断右子树时，将下界设为父节点
            if not helper(node.right, val, upper):
                return False
            # 判断左子树时，将上界设为父节点
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)
        
        