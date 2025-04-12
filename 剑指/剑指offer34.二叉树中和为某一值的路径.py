"""
给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

叶子节点 是指没有子节点的节点。

输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：[[5,4,11,2],[5,8,4,5]]
"""

# 思路：先序遍历+记录

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(node, target):
            if not node:
                return
            path.append(node.val)
            target -= node.val
            # 如果是叶子节点且路径和等于目标值，加入结果集
            if not node.left and not node.right and target == 0:
                res.append(path.copy())
            # 继续遍历左右子树
            dfs(node.left, target)
            dfs(node.right, target)
            
            # 回溯，移除当前节点
            path.pop()

        dfs(root, targetSum)
        return res
                
        
