"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

 

示例 1：


输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
"""

# 思路：后序遍历，递归遇到p和q点返回对应的p和q；
    #如果同时返回了p和q，则返回root（找到了公共节点）
    #如果左边有返回值右边没有，返回left
    #如果右边有返回值左边没有，返回right
    #左右都没有，返回None（递归终止条件）

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 判断当前节点是否为空
        if root is None:
            return None
        # 如果当前节点等于p或q，则直接返回当前节点
        if root == p or root == q:
            return root
        
        # 分别在左子树和右子树中查找
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # 如果左右子树都返回了非空值，则当前节点就是最近公共祖先
        if left and right:
            return root
        
        # 如果左子树没有返回值，则说明两节点均在右子树中
        if left is None:
            return right
        
        # 否则，返回左子树的结果
        return left
