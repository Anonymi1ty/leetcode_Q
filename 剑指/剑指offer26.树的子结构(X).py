"""
给定两棵二叉树 tree1 和 tree2，判断 tree2 是否以 tree1 的某个节点为根的子树具有 相同的结构和节点值 。
注意，空树 不会是以 tree1 的某个节点为根的子树具有 相同的结构和节点值 。
"""

# 思路：先序遍历，获得节点后对比

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSubStructure(self, A: Optional[TreeNode], B: Optional[TreeNode]) -> bool:
        # 如果 A 或 B 为空，则直接返回 False。
        if not A or not B:
            return False
        
        # 第一步：调用 match(A, B) 检查以当前节点 A 为起点，是否能匹配 B。
        # 第二步：如果第一步不成功，则递归地在 A 的左子树中查找是否存在匹配；
        # 第三步：如果左子树中也没有匹配，再递归地在 A 的右子树中查找匹配。
        return self.match(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B) # 每次调用isSubStructure都回调用match
    
    def match(self, A: Optional[TreeNode], B: Optional[TreeNode]) -> bool:
        # 如果 B 遍历完了（即 B 为 None），说明 B 的所有节点都已经成功匹配，返回 True。
        if not B:
            return True
        # 如果 A 为空（但 B 不为空），或当前 A 节点的值与 B 不相等，则匹配失败，返回 False。
        if not A or A.val != B.val:
            return False
        # 同时递归判断左右子树，只有两个方向都匹配，才能认为从当前节点开始匹配成功。
        return self.match(A.left, B.left) and self.match(A.right, B.right)

            
            
        