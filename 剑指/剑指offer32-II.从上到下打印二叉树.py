"""
一棵圣诞树记作根节点为 root 的二叉树，节点值为该位置装饰彩灯的颜色编号。请按照从 左 到 右 的顺序返回每一层彩灯编号。

输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]
"""

# 思路：层次遍历二叉树

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            level_size = len(q)
            level_nodes = []
            for _ in range(level_size):
                node = q.pop()  # 从队列右侧侧取出节点（先入先出）
                level_nodes.append(node.val)
                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)
            res.append(level_nodes)
        return res

            

            
            
        