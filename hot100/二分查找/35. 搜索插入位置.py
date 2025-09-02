"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。

示例 1:

输入: nums = [1,3,5,6], target = 5
输出: 2

"""

# 思路：
    # 二分
    
from typing import List, Optional


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lens = len(nums)
        # 如果不存在，返回插入位置
        if lens == 0:
            return 0
        left, right = 0, lens - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left  # 返回插入位置