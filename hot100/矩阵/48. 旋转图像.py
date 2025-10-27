"""
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[7,4,1],[8,5,2],[9,6,3]]

"""

# 思路（旋转90°和转置不一样）：
    # 1. 先将矩阵进行转置：zip(*matrix)
    # 2. 再将每一行进行反转（或者理解为倒着写入）

    
from typing import List, Optional


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 1. 得到转置并倒序每行
        new_mat = [list(row)[::-1] for row in zip(*matrix)] #zip(*matrix) 将行和列交换,但是返回的是一个迭代器，所以需要转换成列表
        # 2. 写回原 matrix，实现 in-place
        for i in range(n):
            matrix[i] = new_mat[i]
