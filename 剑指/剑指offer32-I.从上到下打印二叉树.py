"""
一棵圣诞树记作根节点为 root 的二叉树，节点值为该位置装饰彩灯的颜色编号。请按照从 左 到 右 的顺序返回每一层彩灯编号。

输入：root = [8,17,21,18,null,null,6]
输出：[8,17,21,18,6]
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
    def decorateRecord(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque()
        res = []
        q.appendleft(root)
        while q:
            node = q.pop()
            res.append(node.val)
            if node.left:
                q.appendleft(node.left)
            if node.right:
                q.appendleft(node.right)
        return res
            
        

            

            
            
        