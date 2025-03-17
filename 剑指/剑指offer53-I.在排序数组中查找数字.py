"""
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

 

示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
示例 2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
示例 3：

输入：nums = [], target = 0
输出：[-1,-1]
"""

# 思路：设计要求复杂度为 O(log n)，二分查找是最佳选择。但是这里要找的是开始位置和结束位置，所以需要分别找到左边界和右边界。

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #判断是否为空，nums为空的话它的值是False
        if not nums:
            return [-1, -1]
        left, right = 0, len(nums) -1
        while left <= right:
            mid = left + (right - left) //2
            # 如果找到了target就要找，左右边界
            if nums[mid] == target:
                flag_left = mid
                flag_right = mid
                
                # 左边界
                while nums[flag_left] == target:
                    flag_left -= 1
                    # 补充一下数组越界判断
                    if flag_left == -1:
                        break
                # 会多减一次
                left = flag_left + 1
                # 右边界
                while nums[flag_right] == target:
                    flag_right += 1
                    if flag_right == len(nums):
                        break
                # 会多加一次
                right = flag_right - 1
                return [left, right]
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1
        return [-1, -1]
        
