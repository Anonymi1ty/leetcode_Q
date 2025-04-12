"""
请实现一个函数来判断整数数组 postorder 是否为二叉搜索树的后序遍历结果。

输入: postorder = [4,9,6,5,8]
输出: false 
解释：从上图可以看出这不是一颗二叉搜索树（左子树小于根节点，右子树大于根节点）
"""

# 思路：找到根节点 root = postorder[-1];
    # 在前面部分 [0 : len - 1] 中，找出第一个大于 root 的位置 m，它前面的都是左子树（值应该小于 root）。
    # 从 m 到 len - 2，都应该是右子树（值应该大于 root），如果有小于 root 的数，则不满足 BST 性质，返回 False。
    # 递归判断

class Solution:
    def verifyTreeOrder(self, postorder: List[int]) -> bool:
        def help(left, right):
            if left >= right: #终止条件： 当 left >= right ，说明此子树节点数量 ≤1 ，无需判别正确性，因此直接返回 true
                return True
            root = postorder[right] #确定当前的root
            m = left
            # 找出第一个比 root 大的位置，分出左右子树
            while postorder[m] < root:
                m += 1
            
            flag = m # 确定右子树的变量
            # # 右子树中的值必须都 > root
            while flag < right:
                if postorder[flag] < root:
                    return  False
                flag += 1
            return help(left, m - 1) and help(m, right - 1)
        
        return help(0, len(postorder) - 1)
                
        
