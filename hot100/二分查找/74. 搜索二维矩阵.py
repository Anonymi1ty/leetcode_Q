"""
给你一个满足下述两条属性的 m x n 整数矩阵：

每行中的整数从左到右按非严格递增顺序排列。
每行的第一个整数大于前一行的最后一个整数。
给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。

示例 1:

输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true

"""

# 思路：
    # 把矩阵当成一维数组来处理，使用二分查找
    
from typing import List, Optional


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        rows, cols = len(matrix), len(matrix[0])
        # 二分查找
        # 将二维矩阵看作一维数组
        left, right = 0, rows * cols - 1
        while left <= right:
            mid = (left + right) // 2
            mid_value = matrix[mid // cols][mid % cols] # 整除，得到 mid 在矩阵中的“行号”。 取余，得到 mid 在矩阵中的“列号”。
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
