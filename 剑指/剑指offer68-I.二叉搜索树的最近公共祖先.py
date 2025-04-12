"""
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]

"""

# 思路：找到节点，如果两个节点分别位于树的两侧，那么则该节点为公共祖先

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 搜索二叉树可以使用比大小判断左右子树
        if p.val < root.val and q.val <root.val: # 两个点都位于左子树
            return self.lowestCommonAncestor(root.left, p, q) #比如加return，不然返回结果不对（需要将找到的公共祖先返回，即返回递归调用的最后一次else）
        if p.val > root.val and q.val > root.val: # 两个点都位于右子树
            return self.lowestCommonAncestor(root.right, p, q)
        else: # 两个节点分别位于树的两侧
            return root

            
            
        