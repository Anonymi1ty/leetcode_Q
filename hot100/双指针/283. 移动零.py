"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。

 

示例 1:

输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
示例 2:

输入: nums = [0]
输出: [0]
"""

# 思路：
    # 原本就有顺序，所以直接遍历存储即可
    # slow 作为第一个指针填写非零数字
    # fast 作为第二个指针遍历数组

    
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #
        slow = 0 
        for fast in range(len(nums)):
            if nums[fast] != 0:
                # 将fast指针指向的值写入slow
                nums[slow] = nums[fast]
                slow += 1
        
        # 将剩下部分全填成 0
        for i in range(slow, len(nums)):
            nums[i] = 0
        