#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    # nums: List[int]的意思是nums是一个列表，列表中的元素都是int类型
    # -> None的意思是函数没有返回值
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mid = 1
        left = 0
        right = len(nums) - 1
        i = 0
        # 从左到右遍历,使用while，终止条件是i大于right
        while i <= right:
            # 如果i小于1，则和左侧指针的下一位换位置，并且左侧指针向右移动一位，i向右移动一位
            if nums[i] < mid:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            # 如果i大于1，则和左侧指针的下一位换位置，并且右侧指针向左移动一位，i不动
            elif nums[i] > mid:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
            # 如果i等于1，则i向右移动一位
            else:
                i += 1
        print(nums)   
# @lc code=end

