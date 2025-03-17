#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路：1. 1)先将整个树遍历，使用HashMap记录父节点 2)使用HashSet记录第一个点的整条链，遍历第二个点检查是否在HashSet上
    #2. 使用递归，每个头结点向自己的左右节点询问信息，终止条件是遇到None遇到p，遇到q直接返回
        # 成立条件：1)q或者q为对方的父亲结点，直接返回自己
            # 2)q和p没有公共部分，返回他们的公共部分
class Solution:
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     # 记录每个点直接的父节点
    #     FatherMap = {}
    #     # 加入头结点的父节点（自己
    #     FatherMap[root] = root
    #     self.process(root, FatherMap)
    #     # 记录p整条链的HashSet
    #     pMap = set()
    #     # 记录当前结点
    #     cur = p
    #     # cur != FatherMap[cur](只有头结点才等于自己)，意思是在头结点时停止
    #     while cur != FatherMap[cur]:
    #         # 添加pMap中的cur节点
    #         pMap.add(cur)
    #         # cur更新为父节点
    #         cur = FatherMap[cur]
    #     #加入头节点
    #     pMap.add(root)
    #     # 检查q中是否有重复节点
    #     cur = q
    #     while cur != FatherMap[cur]:
    #         if cur in pMap:
    #             return cur
    #         cur = FatherMap[cur]
    #     # 检查完后都没有,那么公共点就是root（cur）
    #     return cur
            
        
    # def process(self, root, FatherMap):
    #     if root is None:
    #         return
    #     if root.left is not None:
    #         FatherMap[root.left] = root
    #     if root.right is not None:
    #         FatherMap[root.right] = root
    #     self.process(root.left, FatherMap)
    #     self.process(root.right, FatherMap)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 设置递归结束条件
        if root == None or root == p or root == q:
            return root
        leftNode = self.lowestCommonAncestor(root.left, p ,q)
        rightNode = self.lowestCommonAncestor(root.right, p ,q)
        # 左右都不为空即：p和q不是各自的父节点，这种情况返回他们的父亲节点（情况1）
        if leftNode is not None and rightNode is not None:
            return root
        # 其他情况，如果左边有返回值，返回左边（q或者p互相为对应的父亲节点，返回这俩本身）
        if leftNode is not None:
            return leftNode
        # 如果右边有返回值，返回右边
        else:
            return rightNode
        
# @lc code=end

