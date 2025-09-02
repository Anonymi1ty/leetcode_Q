"""
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。

输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
输出：[[1,0,1],[0,0,0],[1,0,1]]

"""

# 思路：
    # 1. 使用两个集合分别记录需要置零的行和列
    # 2. 遍历矩阵，找到所有需要置零的行和列
    # 3. 再次遍历矩阵，根据记录的行和列将对应元素置为 0
from typing import List, Optional


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # m*n 矩阵的行数和列数
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                # 如果当前元素为 0，则将其所在行和列的所有元素置为 0
                if matrix[i][j] == 0:
                    for k in range(n):
                        if matrix[i][k] != 0:
                            matrix[i][k] = 'x'
                    for k in range(m):
                        if matrix[k][j] != 0:
                            matrix[k][j] = 'x'
        # 再次遍历矩阵，将标记为 'x' 的元素置为 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 'x':
                    matrix[i][j] = 0
            
                