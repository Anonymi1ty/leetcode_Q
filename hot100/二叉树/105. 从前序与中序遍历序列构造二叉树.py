"""
给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

 

示例 1:


输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]
"""

# 思路：preorder的第一个是根节点，它平分inorder中的数组；结束条件是根节点左右两侧都只剩一个node

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # 先序遍历的第一个元素是根节点
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # 在中序遍历中找到根节点的索引
        root_index = inorder.index(root_val)
        
        # 递归构造左子树和右子树
        root.left = self.buildTree(preorder[1:root_index+1], inorder[:root_index]) # +1是因为左闭右开,先序不+1会报错
        root.right = self.buildTree(preorder[root_index+1:], inorder[root_index+1:])

        return root
        