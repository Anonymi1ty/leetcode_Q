"""
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。

输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
输出：[[1,0,1],[0,0,0],[1,0,1]]

"""

# 思路（标记法，原地实现）：
# -----------------------------------------------------------
# 1️⃣ 遍历矩阵，找出所有为 0 的元素。
#     - 若 matrix[i][j] == 0，则其所在的整行 i 和整列 j 都应被置为 0。
#     - 但若我们直接在遍历时修改，会导致“后续遍历被污染”
#       （即原本非 0 的元素可能因为前面被改为 0 而误触发）。
#
# 2️⃣ 为避免连锁污染，可以先用一个特殊标记（如 'x'）临时标记：
#     - 当遇到 0 时，把同一行、同一列中原本非 0 的元素标记为 'x'，
#       表示这些位置将来会被置为 0。
#
# 3️⃣ 遍历结束后，再进行第二次扫描：
#     - 把所有标记为 'x' 的元素真正修改为 0。
#
# 4️⃣ 时间复杂度：O(m×n×(m+n))（因每个 0 会导致一整行一整列扫描）
#     空间复杂度：O(1)（只使用原矩阵，符合“原地修改”要求）
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
            
                