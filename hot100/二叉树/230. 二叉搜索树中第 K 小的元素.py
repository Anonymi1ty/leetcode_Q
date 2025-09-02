"""
给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 小的元素（从 1 开始计数）。

 

示例 1：


输入：root = [3,1,4,null,2], k = 1
输出：1
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 二叉搜索树中序遍历是递增序列；所以相当于找第k个数字即可
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def bfs(node):
            if not node:
                return
            bfs(node.left)
            self.k -= 1 # 自减1，直到0 为止
            if self.k == 0:
                self.res = node.val
                return #满足条件，终止递归
            bfs(node.right)
            
        self.k = k
        bfs(root)
        
        return self.res
            
        
        