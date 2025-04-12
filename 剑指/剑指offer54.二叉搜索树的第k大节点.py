"""
某公司组织架构以二叉搜索树形式记录，节点值为处于该职位的员工编号。请返回第 cnt 大的员工编号。
"""

# 思路：后续便利，使用deque存储，append加入新的节点，返回[cnt-1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findTargetNode(self, root: Optional[TreeNode], cnt: int) -> int:
        candidate = deque()
        def post_order(root):
            if root is None:
                return
            post_order(root.right)
            candidate.append(root.val)
            post_order(root.left)
        post_order(root)
        return candidate[cnt-1]
        
        
