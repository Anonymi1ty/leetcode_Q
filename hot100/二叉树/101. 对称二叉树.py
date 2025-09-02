"""
给你一个二叉树的根节点 root ， 检查它是否轴对称。

 

示例 1：


输入：root = [1,2,2,3,4,4,3]
输出：true
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 思路：两对称节点值相等，
        # 左子树的右孩子与右子树的左孩子是否相同，
        # 左子树的左孩子与右子树的左右孩子是否相同

# Definition for a binary tree node.
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            # 传入的左节点和右节点都没有,return True
            if not right and not left:
                return True
            # 传入的一边有一边没有,return False
            if not left or not right:
                return False
            return (left.val == right.val and
                    isMirror(left.left, right.right) and
                    isMirror(left.right, right.left)
                    )
        return isMirror(root, root)
        