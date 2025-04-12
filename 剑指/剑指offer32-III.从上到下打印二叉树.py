"""
一棵圣诞树记作根节点为 root 的二叉树，节点值为该位置装饰彩灯的颜色编号。请按照如下规则记录彩灯装饰结果：

第一层按照从左到右的顺序记录
除第一层外每一层的记录顺序均与上一层相反。即第一层为从左到右，第二层为从右到左。

输入：root = [8,17,21,18,null,null,6]
输出：[[8],[21,17],[18,6]]
"""

# 思路：层次遍历二叉树，每层便利顺序一样，但是level_nodes加入顺序改变即可

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from collections import deque
class Solution:
    def decorateRecord(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        res = []
        flag = True
        while q:
            level_size = len(q)
            level_nodes = deque()
            if flag:
                for _ in range(level_size):
                    node = q.pop()  # 从队列右侧侧取出节点（先入先出）
                    level_nodes.append(node.val)
                    if node.left:
                        q.appendleft(node.left)
                    if node.right:
                        q.appendleft(node.right)
                res.append(list(level_nodes))
                flag = False
            else:
                for _ in range(level_size):
                    node = q.pop()
                    level_nodes.appendleft(node.val)  #唯一不一样的地方
                    if node.left:
                        q.appendleft(node.left)
                    if node.right:
                        q.appendleft(node.right)
                res.append(list(level_nodes))
                flag = True
        return res
            
        

            

            
            
        