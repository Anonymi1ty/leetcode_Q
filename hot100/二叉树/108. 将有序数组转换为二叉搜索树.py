"""
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 平衡 二叉搜索树。

 

示例 1：


输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]
解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：
"""

# 思路
    # 按照中序排列，
    # 每次取中点作为根，左半部分递归建左子树，右半部分递归建右子树。这样天然保证平衡（高度≈log n）
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 分治：区间[l, r]内构建平衡BST
        def build(l: int, r: int) -> Optional[TreeNode]:
            if l > r:
                return None
            mid = (l + r) // 2          # 取中点作为根
            root = TreeNode(nums[mid])
            root.left  = build(l, mid - 1) # 递归构建左
            root.right = build(mid + 1, r) # 递归构建右
            return root

        return build(0, len(nums) - 1)        
        