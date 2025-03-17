# 题目：
"""
m*n 的二维数组 plants 记录了园林景观的植物排布情况，具有以下特性：

每行中，每棵植物的右侧相邻植物不矮于该植物；(右侧恒大于等于)
每列中，每棵植物的下侧相邻植物不矮于该植物。（下侧恒大于等于）
 

请判断 plants 中是否存在目标高度值 target。
"""
from typing import List

class Solution:
    def findTargetIn2DPlants(self, plants: List[List[int]], target: int) -> bool:
        if not plants or not plants[0]:
            return False

        # 二分查找函数，用于在每一行中查找目标值
        def binarySearch(row: List[int], target: int) -> bool:
            left, right = 0, len(row) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False

        # 遍历每一行
        for row in plants:
            # 如果目标值小于当前行的第一个元素，直接返回False
            if row[0] > target:
                return False
            # 如果目标值大于当前行的最后一个元素，跳过该行
            if row[-1] < target:
                continue
            # 否则，对该行进行二分查找
            if binarySearch(row, target):
                return True

        return False
