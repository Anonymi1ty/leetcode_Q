"""
给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

 

示例 1：

输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出：3
解释：和等于 8 的路径有 3 条，如图所示。
"""

# 思路：前缀和 + 哈希表(key是前缀和， value是前缀和出现的次数，记录数量是因为有出现复数路径的可能)

from typing import Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # 前缀和计数字典：sum -> 出现次数
        prefix_cnt = {0: 1}   # 重要：空路径前缀和为0，确保从根开始的路径也能被计数
        self.ans = 0

        def dfs(node: Optional[TreeNode], cur_sum: int) -> None:
            if not node:
                return
            # 1) 更新当前前缀和
            cur_sum += node.val
            # 2) 查找以当前节点为结尾、和为targetSum的路径条数
            #    即有多少 earlier_sum 满足 earlier_sum = cur_sum - targetSum
            need = cur_sum - targetSum
            self.ans += prefix_cnt.get(need, 0)

            # 3) 将当前前缀和放入哈希表，供子树使用
            prefix_cnt[cur_sum] = prefix_cnt.get(cur_sum, 0) + 1

            # 4) 递归左右子树
            dfs(node.left, cur_sum)
            dfs(node.right, cur_sum)

            # 5) 回溯：离开该节点时，撤销当前前缀和的贡献
            prefix_cnt[cur_sum] -= 1

        dfs(root, 0)
        return self.ans
