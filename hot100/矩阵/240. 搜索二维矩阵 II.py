"""
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。

示例 1：
输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
输出：true

"""

# 思路：
    # 1. 从右上角开始搜索
    # 2. 如果当前值等于目标值，返回 True
        # 3. 如果当前值大于目标值，向左移动一列
        # 4. 如果当前值小于目标值，向下移动一行
        # 5. 如果超出边界，返回 False

    
from typing import List, Optional


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, cols - 1 # 从右上角开始
        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        
        return False
