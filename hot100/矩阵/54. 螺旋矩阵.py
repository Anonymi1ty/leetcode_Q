"""
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

"""

# 思路：
    # 1. 定义四个边界变量：上、下、左、右
    # 2. 使用 while 循环遍历矩阵，逐层收缩
    
from typing import List, Optional


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        result = []
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # 从左到右遍历上边界
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
            
            # 从上到下遍历右边界
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            
            if top <= bottom:
                # 从右到左遍历下边界
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            
            if left <= right:
                # 从下到上遍历左边界
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        
        return result
                